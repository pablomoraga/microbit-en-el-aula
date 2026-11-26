# -*- coding: utf-8 -*-
"""Motor de ilustración en perspectiva (proyección ortográfica única, como la portada).
Coordenadas del plano de la mesa: u (izquierda → derecha), v (fondo → frente), z (altura). 10,5 unidades ≈ 1 mm."""
import math, html
from placa import frente, _nested
e = html.escape

DEFS = ('<defs><filter id="isb" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>'
        '<linearGradient id="isau" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6d985"/><stop offset="1" stop-color="#9c6f17"/></linearGradient>'
        '<linearGradient id="ismetal" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8d939b"/><stop offset=".45" stop-color="#f1f3f5"/><stop offset="1" stop-color="#7c828a"/></linearGradient>'
        '<radialGradient id="isbg" cx=".5" cy=".55" r=".5"><stop offset="0" stop-color="#fff8ec"/><stop offset=".8" stop-color="#f6ead6"/><stop offset="1" stop-color="#f6ead6" stop-opacity="0"/></radialGradient>'
        '</defs>')

def mix(c, k):
    """Oscurece (k < 1) o aclara (k > 1) un color #rrggbb."""
    c = c.lstrip('#'); r, g, b = int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)
    f = (lambda x: max(0, min(255, int(x * k)))) if k <= 1 else (lambda x: int(x + (255 - x) * (k - 1)))
    return '#%02x%02x%02x' % (f(r), f(g), f(b))

class Escena:
    def __init__(self, W, H, s=0.5, x0=None, y0=None, giro=20, escorzo=0.55):
        th = math.radians(giro)
        self.W, self.H, self.S = W, H, s
        self.UX, self.UY = math.cos(th), math.sin(th) * escorzo
        self.VX, self.VY = -math.sin(th), math.cos(th) * escorzo
        self.CZ = math.sqrt(1 - escorzo ** 2)
        self.X0 = W * 0.42 if x0 is None else x0
        self.Y0 = H * 0.18 if y0 is None else y0
        self.capas = []
        self.puntos = []
        self._bb = []

    # ---------------------------------------------------------- proyección
    def P(self, u, v, z=0.0, caja=True):
        S = self.S
        p = (self.X0 + S * (u * self.UX + v * self.VX), self.Y0 + S * (u * self.UY + v * self.VY) - S * z * self.CZ)
        if caja: self._bb.append(p)
        return p

    def M(self, z=0.0):
        S = self.S
        return 'matrix(%.5f %.5f %.5f %.5f %.2f %.2f)' % (S * self.UX, S * self.UY, S * self.VX, S * self.VY, self.X0, self.Y0 - S * z * self.CZ)

    def frontal(self, u0, v, z0):
        """Transformación para dibujar en la cara vertical que mira al frente (x hacia la derecha, y hacia abajo)."""
        S = self.S; x, y = self.P(u0, v, z0)
        return 'matrix(%.5f %.5f 0 %.5f %.2f %.2f)' % (S * self.UX, S * self.UY, S * self.CZ, x, y)

    def lateral(self, u, v0, z0):
        """Cara vertical que mira a la derecha (x hacia el frente, y hacia abajo)."""
        S = self.S; x, y = self.P(u, v0, z0)
        return 'matrix(%.5f %.5f 0 %.5f %.2f %.2f)' % (S * self.VX, S * self.VY, S * self.CZ, x, y)

    def poly(self, pts, fill, extra=''):
        return '<path d="M%s Z" fill="%s"%s/>' % (' L'.join('%.1f %.1f' % self.P(*p) for p in pts), fill, extra)

    def add(self, svg):
        self.capas.append(svg); return self

    # ---------------------------------------------------------- piezas
    def sombra(self, u, v, w, d, r=20, op=.28):
        return self.add('<g transform="%s"><rect x="%d" y="%d" width="%d" height="%d" rx="%d" fill="#3b2a20" opacity="%.2f" filter="url(#isb)"/></g>' % (
            self.M(0), u + 14, v + 18, w, d, r, op))

    def caja(self, u, v, w, d, h, color, z=0, sombra=True, rx=0, tapa=None, borde=None):
        """Prisma rectangular apoyado en z: tapa, cara frontal (v + d) y cara derecha (u + w)."""
        if sombra and z == 0: self.sombra(u, v, w, d)
        st = ' stroke="%s" stroke-width="1.2"' % borde if borde else ''
        self.add(self.poly([(u, v + d, z), (u + w, v + d, z), (u + w, v + d, z + h), (u, v + d, z + h)], mix(color, .72), st))
        self.add(self.poly([(u + w, v, z), (u + w, v + d, z), (u + w, v + d, z + h), (u + w, v, z + h)], mix(color, .55), st))
        self.add('<g transform="%s"><rect x="%d" y="%d" width="%d" height="%d" rx="%d" fill="%s"%s/></g>' % (self.M(z + h), u, v, w, d, rx, tapa or color, st))
        return self

    def cilindro(self, u, v, r, h, color, z=0, tapa=None, paso=3):
        for du, dv in ((-r, 0), (r, 0), (0, -r), (0, r)):
            self.P(u + du, v + dv, z); self.P(u + du, v + dv, z + h)
        self.add('<g transform="%s"><circle cx="%d" cy="%d" r="%d" fill="#3b2a20" opacity=".25" filter="url(#isb)"/></g>' % (self.M(0), u + 10, v + 14, r))
        zz = z
        while zz < z + h:
            self.add('<g transform="%s"><circle cx="%d" cy="%d" r="%d" fill="%s"/></g>' % (self.M(zz), u, v, r, mix(color, .7)))
            zz += paso
        return self.add('<g transform="%s"><circle cx="%d" cy="%d" r="%d" fill="%s"/></g>' % (self.M(z + h), u, v, r, tapa or color))

    def microbit(self, u, v, ancho=540, z=0, lit=None, uid='m'):
        """micro:bit tumbada con su grosor y los dedos dorados del conector en el canto frontal."""
        k = ancho / 540.0; bt = 12 * k
        for a, b in ((0, 0), (540, 0), (0, 450), (540, 450)): self.P(u + a * k, v + b * k, z + bt)
        x = lambda a: u + a * k
        y = lambda b: v + b * k
        if z == 0: self.sombra(u, v, ancho, 450 * k, 26 * k)
        self.add(self.poly([(x(20), y(425), z), (x(520), y(425), z), (x(520), y(425), z + bt), (x(20), y(425), z + bt)], '#0c0e11'))
        self.add(self.poly([(x(520), y(40), z), (x(520), y(425), z), (x(520), y(425), z + bt), (x(520), y(40), z + bt)], '#1a1e24'))
        for f in (0.1, 0.3, 0.5, 0.7, 0.9):
            a = 20 + 500 * f - 27
            self.add(self.poly([(x(a), y(425), z + .5), (x(a + 54), y(425), z + .5), (x(a + 54), y(425), z + bt), (x(a), y(425), z + bt)], 'url(#isau)'))
        board = frente(callouts=False, lit=lit if lit is not None else set(), uid=uid)
        return self.add('<g transform="%s"><g transform="translate(%.1f %.1f) scale(%.4f)">%s</g></g>' % (
            self.M(z + bt), u, v, k, _nested(board, 0, 0, 540, 450)))

    def anillo(self, u, v, ancho, cual):
        """Posición (u, v) de un anillo del conector de una micro:bit dibujada en (u, v) con ese ancho."""
        f = {'P0': .1, 'P1': .3, 'P2': .5, '3V': .7, 'GND': .9}[cual]
        k = ancho / 540.0
        return u + (20 + 500 * f) * k, v + 381 * k

    def cable(self, a, b, color, z=6, grosor=14, curva=180):
        """Cable apoyado en la mesa entre dos puntos del plano (u, v)."""
        (u1, v1), (u2, v2) = a, b
        d = 'M%.0f %.0f C %.0f %.0f, %.0f %.0f, %.0f %.0f' % (u1, v1, u1, v1 + curva, u2, v2 + curva * .4, u2, v2)
        self.add('<g transform="%s"><path d="%s" stroke="#3b2a20" stroke-opacity=".22" stroke-width="%d" fill="none" filter="url(#isb)"/></g>' % (self.M(0), d, grosor + 8))
        return self.add('<g transform="%s"><path d="%s" stroke="%s" stroke-width="%d" fill="none" stroke-linecap="round"/>'
                        '<path d="%s" stroke="#fff" stroke-opacity=".3" stroke-width="%d" fill="none" transform="translate(-3 -3)"/></g>' % (
                            self.M(z), d, color, grosor, d, max(2, grosor // 4)))

    def pinza(self, u, v, color, z=14, largo=150, ang=0):
        g = '<g transform="%s"><g transform="translate(%.0f %.0f) rotate(%d)">' % (self.M(z), u, v, ang)
        g += '<path d="M0 10 l-12 -56 q12 -13 24 0 l-12 56z" fill="url(#ismetal)" stroke="#6b7078" stroke-width="1.5"/>'
        g += '<rect x="-20" y="6" width="40" height="%d" rx="18" fill="%s"/><rect x="-20" y="6" width="14" height="%d" rx="7" fill="#fff" opacity=".22"/>' % (largo, color, largo)
        return self.add(g + '</g></g>')

    def ondas(self, u, v, z, n=3, color='#2e78d6', r0=30):
        x, y = self.P(u, v, z)
        s = ''
        for i in range(n):
            r = r0 + i * 22
            s += '<path d="M%.1f %.1f a%d %d 0 0 1 %d 0" stroke="%s" stroke-width="4" fill="none" stroke-linecap="round" opacity="%.2f" transform="translate(%d 0)"/>' % (
                x - r, y, r, r * .8, 2 * r, color, .9 - i * .22, 0)
        return self.add(s)

    def punto(self, u, v, z, titulo, texto):
        """Marca numerada sobre la escena y entrada de la leyenda."""
        self.puntos.append((self.P(u, v, z, caja=False), titulo, texto))
        return self

    # ---------------------------------------------------------- salida
    def svg(self, etiqueta, fondo=True, margen=44):
        s = '<svg viewBox="0 0 %d %d" role="img" aria-label="%s" font-family="system-ui,sans-serif">%s' % (self.W, self.H, e(etiqueta), DEFS)
        if fondo:
            s += '<ellipse cx="%d" cy="%d" rx="%d" ry="%d" fill="url(#isbg)"/>' % (self.W / 2, self.H * .54, self.W * .5, self.H * .46)
        # encuadre automático: centrar y escalar lo dibujado dentro del lienzo
        xs = [p[0] for p in self._bb] + [p[0][0] for p in self.puntos]
        ys = [p[1] for p in self._bb] + [p[0][1] for p in self.puntos]
        x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
        k = min((self.W - 2 * margen) / (x1 - x0), (self.H - 2 * margen) / (y1 - y0))
        dx = (self.W - k * (x1 + x0)) / 2.0
        dy = (self.H - k * (y1 + y0)) / 2.0
        s += '<g transform="translate(%.1f %.1f) scale(%.4f)">' % (dx, dy, k)
        s += ''.join(self.capas) + '</g>'
        # marcas numeradas fuera del grupo escalado: mismo tamaño en todas las escenas
        for i, ((x, y), t, _) in enumerate(self.puntos, 1):
            x, y = dx + k * x, dy + k * y
            mx, my = x - 24, y - 24
            s += ('<g class="pt"><title>%s</title><path d="M%.1f %.1f L%.1f %.1f" stroke="#15202b" stroke-width="2"/><circle cx="%.1f" cy="%.1f" r="4" fill="#15202b"/>'
                  '<circle cx="%.1f" cy="%.1f" r="14" fill="#ff5a36" stroke="#fff" stroke-width="2.5"/>'
                  '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="15" font-weight="800" fill="#fff">%d</text></g>') % (
                e(t), x, y, mx, my, x, y, mx, my, mx, my + 5, i)
        return s + '</svg>'

    def figura(self, etiqueta, fuente=''):
        ley = ''.join('<li><span class="n">%d</span><b>%s</b>%s</li>' % (i, t, d) for i, (_, t, d) in enumerate(self.puntos, 1))
        pie = e(etiqueta) + ((' · Fuente: ' + fuente) if fuente else '')
        return '<figure class="escena">%s<figcaption>%s</figcaption></figure><ol class="leyenda">%s</ol>' % (self.svg(etiqueta), pie, ley)
