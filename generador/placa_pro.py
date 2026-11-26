# -*- coding: utf-8 -*-
"""Ilustración de la portada con una perspectiva coherente: una sola proyección (cámara ortográfica
girada 20° y elevada unos 33°) para la mesa, la placa, su grosor, los cables y los componentes."""
import math
from placa import frente, _nested, CORAZON, _defs

TH, K, CZ = math.radians(20), 0.55, 0.835      # giro en la mesa, escorzo (sen elevación) y altura (cos elevación)
UX, UY = math.cos(TH), math.sin(TH) * K        # eje u (largo de la placa) en pantalla
VX, VY = -math.sin(TH), math.cos(TH) * K       # eje v (fondo → frente) en pantalla
S = 0.60                                        # escala (10,5 unidades = 1 mm)
X0, Y0 = 330, 140                                # origen del plano en pantalla

def P(u, v, z=0.0):
    return (X0 + S * (u * UX + v * VX), Y0 + S * (u * UY + v * VY) - S * z * CZ)

def M(z=0.0):
    return 'matrix(%.5f %.5f %.5f %.5f %.2f %.2f)' % (S * UX, S * UY, S * VX, S * VY, X0, Y0 - S * z * CZ)

def poly(pts, fill, extra=''):
    return '<path d="M%s Z" fill="%s"%s/>' % (' L'.join('%.1f %.1f' % p for p in pts), fill, extra)

BT = 12      # grosor de la placa (unidades del plano)


LETRA_H = {(r, 0) for r in range(5)} | {(r, 3) for r in range(5)} | {(2, 1), (2, 2)}

def _cara(lit=LETRA_H, u='pro'):
    """Anverso de la micro:bit V2 para la portada, con proporciones de la placa real (51,6 × 42 mm):
    matriz cuadrada de LED con paso de unos 4 mm, cuatro esquinas redondeadas, serigrafía blanca y muescas del conector."""
    x0, y0, bw, bh = 20, 18, 500, 407
    k = bw / 51.6                      # unidades por milímetro
    ey = y0 + bh - 8 * k               # el conector ocupa unos 8 mm
    s = _defs(u)
    xs = [x0 + bw * f for f in (0.2, 0.4, 0.6, 0.8)]
    d = 'M%d %d h%d a24 24 0 0 1 24 24 V%d a14 14 0 0 1 -14 14' % (x0 + 24, y0, bw - 48, y0 + bh - 14)
    for xn in reversed(xs):
        d += ' H%.1f v-10 a5 5 0 0 0 -10 0 v10' % (xn + 5)
    d += ' H%d a14 14 0 0 1 -14 -14 V%d a24 24 0 0 1 24 -24z' % (x0 + 14, y0 + 24)
    s += '<path d="%s" fill="url(#pcb%s)"/>' % (d, u)
    s += '<path d="%s" fill="none" stroke="#000" stroke-opacity=".5" stroke-width="2"/>' % d
    # pistas muy discretas
    s += '<g stroke="#2a2f36" stroke-width="2.4" fill="none"><path d="M70 110 h50 l18 18 v60"/><path d="M470 110 h-50 l-18 18 v60"/><path d="M160 318 h220"/></g>'
    # logotipo táctil (cara) y LED del micrófono
    lx, ly = x0 + bw / 2, y0 + 6.2 * k
    s += '<rect x="%.1f" y="%.1f" width="84" height="46" rx="23" fill="none" stroke="url(#au%s)" stroke-width="8"/>' % (lx - 42, ly - 23, u)
    s += '<circle cx="%.1f" cy="%.1f" r="6" fill="url(#au%s)"/><circle cx="%.1f" cy="%.1f" r="6" fill="url(#au%s)"/>' % (lx - 16, ly, u, lx + 16, ly, u)
    s += '<circle cx="%.1f" cy="%.1f" r="4.5" fill="#050608" stroke="#8a9099" stroke-width="1.4"/>' % (lx + 78, ly)
    s += '<rect x="%.1f" y="%.1f" width="10" height="7" rx="1.5" fill="#f1f3f5"/>' % (lx + 92, ly - 3.5)
    # botones A y B (pulsador cuadrado metálico con botón negro)
    by = y0 + 17 * k
    for bx, lab in ((x0 + 6.6 * k, 'A'), (x0 + bw - 6.6 * k, 'B')):
        s += '<rect x="%.1f" y="%.1f" width="60" height="60" rx="5" fill="url(#mk%s)" stroke="#7d838c"/>' % (bx - 30, by - 30, u)
        for dx, dy in ((-24, -24), (24, -24), (-24, 24), (24, 24)):
            s += '<circle cx="%.1f" cy="%.1f" r="2.6" fill="#9aa0a8"/>' % (bx + dx, by + dy)
        s += '<circle cx="%.1f" cy="%.1f" r="19" fill="url(#bt%s)"/>' % (bx, by, u)
        s += '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="19" font-weight="700" fill="#fff">%s</text>' % (bx, by + 54, lab)
    # matriz 5 × 5: paso de unos 4 mm en las dos direcciones
    st = 4.0 * k
    mx, my = lx - 2 * st, y0 + 14.2 * k
    for r in range(5):
        for c in range(5):
            cx, cy = mx + c * st, my + r * st
            if (r, c) in lit:
                s += '<rect x="%.1f" y="%.1f" width="11" height="17" rx="2" fill="#ff3b30" filter="url(#gl%s)"/>' % (cx - 5.5, cy - 8.5, u)
                s += '<rect x="%.1f" y="%.1f" width="5" height="9" rx="1.5" fill="#ffd2cc"/>' % (cx - 2.5, cy - 4.5)
            else:
                s += '<rect x="%.1f" y="%.1f" width="11" height="17" rx="2" fill="#cfc9bf"/><rect x="%.1f" y="%.1f" width="5" height="9" fill="#e9e5de"/>' % (cx - 5.5, cy - 8.5, cx - 2.5, cy - 4.5)
    # conector de borde: tiras finas y 5 anillos con agujero
    for i in range(56):
        fx = x0 + 14 + i * (bw - 28) / 55.0
        s += '<rect x="%.1f" y="%.1f" width="3.4" height="%.1f" rx="1" fill="url(#au%s)"/>' % (fx, ey + 10, y0 + bh - ey - 14, u)
    for lab, f in (('0', 0.1), ('1', 0.3), ('2', 0.5), ('3V', 0.7), ('GND', 0.9)):
        cx = x0 + bw * f
        s += '<rect x="%.1f" y="%.1f" width="56" height="%.1f" rx="8" fill="url(#au%s)"/>' % (cx - 28, ey + 2, y0 + bh - ey - 6, u)
        s += '<circle cx="%.1f" cy="%.1f" r="15" fill="#e3e8ee" stroke="#9c7420" stroke-width="2"/>' % (cx, ey + 32)
        s += '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="15" font-weight="700" fill="#fff">%s</text>' % (cx, ey - 9, lab)
    return s

def _placa():
    s = ''
    # sombra sobre la mesa
    s += '<g transform="%s"><rect x="30" y="40" width="540" height="450" rx="26" fill="#3b2a20" opacity=".35" filter="url(#hpshadow)"/></g>' % M(0)
    # cantos visibles: frente (v = 425) y lado derecho (u = 520)
    s += poly([P(20, 425, 0), P(520, 425, 0), P(520, 425, BT), P(20, 425, BT)], '#0c0e11')
    s += poly([P(520, 40, 0), P(520, 425, 0), P(520, 425, BT), P(520, 40, BT)], '#1a1e24')
    # dedos dorados del conector en el canto frontal
    for i in range(56):
        u = 34 + i * (472 / 55.0)
        s += poly([P(u, 425, 1), P(u + 3.4, 425, 1), P(u + 3.4, 425, BT), P(u, 425, BT)], 'url(#hpgold)')
    for f in (0.1, 0.3, 0.5, 0.7, 0.9):
        u = 20 + 500 * f - 27
        s += poly([P(u, 425, 0.5), P(u + 54, 425, 0.5), P(u + 54, 425, BT), P(u, 425, BT)], 'url(#hpgold)')
    # cara superior
    s += '<g transform="%s">%s</g>' % (M(BT), _cara())
    return s

def _cable(u_ring, col, fin, uid):
    """Pinza sobre el anillo (u_ring, 381) y cable que sale hacia delante y gira a la derecha, apoyado en la mesa."""
    v0 = 381
    g = '<g transform="%s">' % M(BT + 2)
    g += '<path d="M%d %d l-13 -60 q13 -14 26 0 l-13 60z" fill="url(#hpmetal)" stroke="#6b7078" stroke-width="1.5"/>' % (u_ring, v0 + 14)
    g += '<path d="M%d %d h18 M%d %d h22 M%d %d h26" stroke="#6b7078" stroke-width="2"/>' % (u_ring - 9, v0 - 30, u_ring - 11, v0 - 16, u_ring - 13, v0 - 2)
    g += '<rect x="%d" y="%d" width="44" height="170" rx="20" fill="%s"/><rect x="%d" y="%d" width="44" height="170" rx="20" fill="url(#hpboot)"/>' % (
        u_ring - 22, v0 + 8, col, u_ring - 22, v0 + 8)
    g += '</g>'
    path = 'M%d %d C %d %d, %d %d, %d %d' % (u_ring, v0 + 175, u_ring, v0 + 300, fin[0] - 260, fin[1], fin[0], fin[1])
    c = '<g transform="%s"><path d="%s" stroke="#3b2a20" stroke-opacity=".25" stroke-width="22" fill="none" filter="url(#hpblur)"/></g>' % (M(0), path)
    c += '<g transform="%s"><path d="%s" stroke="%s" stroke-width="20" fill="none" stroke-linecap="round"/>' % (M(9), path, col)
    c += '<path d="%s" stroke="#fff" stroke-opacity=".35" stroke-width="5" fill="none" transform="translate(-4 -4)"/></g>' % path
    return c + g

def _led(u, v, ang, col, glow=False):
    """LED de 5 mm tumbado sobre la mesa (dibujado en el plano y elevado su radio)."""
    sh = '<g transform="%s"><g transform="translate(%d %d) rotate(%d)"><rect x="-30" y="-30" width="140" height="60" rx="30" fill="#3b2a20" opacity=".28" filter="url(#hpblur)"/></g></g>' % (M(0), u, v, ang)
    g = '<g transform="%s"><g transform="translate(%d %d) rotate(%d)">' % (M(26), u, v, ang)
    g += '<path d="M60 -10 H300 M60 10 H260" stroke="#a9adb3" stroke-width="6" stroke-linecap="round"/>'
    if glow:
        g += '<ellipse cx="0" cy="0" rx="80" ry="70" fill="%s" opacity=".16"/>' % col
    g += '<path d="M-26 -26 H48 V26 H-26 A26 26 0 0 1 -26 -26Z" fill="%s"/><rect x="48" y="-31" width="12" height="62" rx="3" fill="%s"/>' % (col, col)
    g += '<path d="M-22 -14 H38" stroke="#fff" stroke-width="8" stroke-linecap="round" opacity=".55"/></g></g>'
    return sh + g

def _pulsador(u, v, cap):
    """Pulsador de 12 mm apoyado en la mesa: caja con tapa y botón redondo."""
    w, h = 126, 40
    s = '<g transform="%s"><rect x="%d" y="%d" width="%d" height="%d" rx="8" fill="#3b2a20" opacity=".3" filter="url(#hpblur)"/></g>' % (M(0), u + 6, v + 10, w + 10, w + 10)
    for du, dv in ((-24, 22), (w + 24, 22), (-24, w - 22), (w + 24, w - 22)):
        a, b = P(u + du, v + dv, 0), P(u + (0 if du < 0 else w), v + dv, 3)
        s += '<path d="M%.1f %.1f L%.1f %.1f" stroke="#a9adb3" stroke-width="3" stroke-linecap="round"/>' % (a[0], a[1], b[0], b[1])
    s += poly([P(u, v + w, 0), P(u + w, v + w, 0), P(u + w, v + w, h), P(u, v + w, h)], '#15181c')
    s += poly([P(u + w, v, 0), P(u + w, v + w, 0), P(u + w, v + w, h), P(u + w, v, h)], '#22262c')
    s += '<g transform="%s"><rect x="%d" y="%d" width="%d" height="%d" rx="3" fill="#3d434c"/></g>' % (M(h), u, v, w, w)
    cx, cy = u + w / 2, v + w / 2
    s += '<g transform="%s"><circle cx="%.1f" cy="%.1f" r="38" fill="#000" opacity=".35"/></g>' % (M(h), cx, cy)
    for z in range(h, h + 22, 3):          # cilindro del botón (capas apiladas)
        s += '<g transform="%s"><circle cx="%.1f" cy="%.1f" r="34" fill="%s"/><circle cx="%.1f" cy="%.1f" r="34" fill="#000" opacity=".18"/></g>' % (M(z), cx, cy, cap, cx, cy)
    s += '<g transform="%s"><circle cx="%.1f" cy="%.1f" r="34" fill="%s"/><circle cx="%.1f" cy="%.1f" r="34" fill="#fff" opacity=".25"/></g>' % (M(h + 22), cx, cy, cap, cx - 8, cy - 8)
    return s

def _resistencia(u, v, ang):
    sh = '<g transform="%s"><g transform="translate(%d %d) rotate(%d)"><rect x="-80" y="-18" width="160" height="36" rx="18" fill="#3b2a20" opacity=".22" filter="url(#hpblur)"/></g></g>' % (M(0), u, v, ang)
    g = '<g transform="%s"><g transform="translate(%d %d) rotate(%d)"><path d="M-170 0 H170" stroke="#a9adb3" stroke-width="5" stroke-linecap="round"/>' % (M(12), u, v, ang)
    g += '<rect x="-34" y="-13" width="68" height="26" rx="12" fill="url(#hpres)"/>'
    for x, c in ((-22, '#c0392b'), (-11, '#c0392b'), (0, '#5b3a29'), (17, '#c8a24a')):
        g += '<rect x="%d" y="-13" width="6" height="26" fill="%s"/>' % (x, c)
    return sh + g + '<path d="M-30 -6 H30" stroke="#fff" stroke-width="3" opacity=".45" stroke-linecap="round"/></g></g>'

HEART = [(0, 1), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (4, 2)]

def _corazon(x, y, k, col):
    """Corazón de 5 × 5 puntos (para dentro de los bloques)."""
    return ''.join('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="1" fill="%s"/>' % (x + c * k, y + f * k, k * .8, k * .8, col) for f, c in HEART)

def _tarjeta(x, y, w, h, titulo, color, cuerpo):
    s = '<g transform="translate(%d %d) scale(1.25)">' % (x, y)
    s += '<rect x="0" y="6" width="%d" height="%d" rx="14" fill="#15202b" opacity=".16" filter="url(#hpblur)"/>' % (w, h)
    s += '<rect width="%d" height="%d" rx="14" fill="#fff" stroke="#15202b" stroke-width="1.5"/>' % (w, h)
    s += '<circle cx="18" cy="18" r="5" fill="%s"/><text x="30" y="22.5" font-size="12.5" font-weight="700" fill="#15202b" font-family="ui-monospace,Consolas,monospace">%s</text>' % (color, titulo)
    s += '<path d="M0 34 H%d" stroke="#d5dbe3"/>' % w
    return s + cuerpo + '</g>'

def _bloque(x, y, w, color, txt, hat=False, cadena=None):
    """Bloque de programación estilizado (tapa redondeada si es un evento) con un hueco de texto opcional."""
    h = 30
    if hat:
        d = 'M%d %d q0 -14 34 -14 h%d q34 0 34 14 v%d h-%d z' % (x, y, w - 68, h, w)
    else:
        d = 'M%d %d h%d v%d h-%d z' % (x, y, w, h, w)
    s = '<path d="%s" fill="%s"/>' % (d, color)
    s += '<text x="%d" y="%d" font-size="13" font-weight="700" fill="#fff" font-family="system-ui,sans-serif">%s</text>' % (x + 10, y + 20, txt)
    if cadena:
        s += '<rect x="%d" y="%d" width="86" height="22" rx="11" fill="#fff"/>' % (x + w - 92, y + 4)
        s += '<text x="%d" y="%d" text-anchor="middle" font-size="12" fill="#15202b" font-family="system-ui,sans-serif">%s</text>' % (x + w - 49, y + 19.5, cadena)
    return s

def hero():
    global S, X0, Y0
    W, H = 720, 580
    S, X0, Y0 = 0.62, 340, 205
    s = ('<svg class="placa-svg hero-pro" viewBox="0 0 %d %d" role="img" aria-label="Una micro:bit V2 escribe Hola clase en su pantalla; alrededor, el mismo '
         'programa en MakeCode, MicroBlocks y Python, y sobre la mesa unos LED, pulsadores y una resistencia">' % (W, H))
    s += ('<defs><filter id="hpblur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5"/></filter>'
          '<filter id="hpshadow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="16"/></filter>'
          '<filter id="hpglow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="20"/></filter>'
          '<radialGradient id="hpbg" cx=".52" cy=".56" r=".5"><stop offset="0" stop-color="#fff" stop-opacity=".95"/><stop offset=".45" stop-color="#fff" stop-opacity=".55"/>'
          '<stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>'
          '<radialGradient id="hpfade" cx=".52" cy=".58" r=".5"><stop offset="0" stop-color="#fff"/><stop offset=".6" stop-color="#fff" stop-opacity=".6"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>'
          '<mask id="hpmask"><rect width="720" height="580" fill="url(#hpfade)"/></mask>'
          '<linearGradient id="hpgold" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6d985"/><stop offset="1" stop-color="#9c6f17"/></linearGradient>'
          '<linearGradient id="hpmetal" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8d939b"/><stop offset=".45" stop-color="#f1f3f5"/><stop offset="1" stop-color="#7c828a"/></linearGradient>'
          '<linearGradient id="hpboot" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#000" stop-opacity=".25"/><stop offset=".35" stop-color="#fff" stop-opacity=".35"/><stop offset=".6" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".3"/></linearGradient>'
          '<linearGradient id="hpres" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4e3bd"/><stop offset=".55" stop-color="#d9bd88"/><stop offset="1" stop-color="#a78755"/></linearGradient>'
          '</defs>')
    # luz suave, sin bordes, y retícula de la mesa que se desvanece
    s += '<rect width="%d" height="%d" fill="url(#hpbg)"/>' % (W, H)
    s += '<g mask="url(#hpmask)"><g transform="%s" opacity=".7">' % M(0)
    for u in range(-500, 1100, 40):
        for v in range(-200, 900, 40):
            s += '<circle cx="%d" cy="%d" r="2.2" fill="#b3bfcd"/>' % (u, v)
    s += '</g></g>'
    # placa, cables y componentes
    gx, gy = P(270, 215, BT)
    s += _placa()
    s += '<ellipse cx="%.0f" cy="%.0f" rx="60" ry="36" fill="#ff3b30" opacity=".16" filter="url(#hpglow)"/>' % (gx, gy)
    s += _cable(370, '#c0392b', (980, 560), 'r') + _cable(470, '#262a30', (1000, 700), 'k')
    s += _resistencia(70, 570, 14)
    s += _pulsador(-210, 500, '#e0a83a') + _led(-70, 700, -28, '#e74c3c', True) + _led(-250, 770, 20, '#27ae60')
    s += _pulsador(130, 700, '#c0392b') + _led(320, 880, -70, '#2e86de', True)
    # líneas de las tarjetas a la pantalla
    for (x, y) in ((250, 160), (540, 150)):
        s += '<path d="M%d %d Q %.0f %.0f %.0f %.0f" stroke="#15202b" stroke-width="1.6" stroke-dasharray="5 6" fill="none" opacity=".5"/>' % (
            x, y, (x + gx) / 2, min(y, gy) - 30, gx, gy)
    # tarjetas: el mismo programa en los tres editores
    s += _tarjeta(2, 8, 246, 120, 'MakeCode', '#1E90FF',
                  _bloque(14, 54, 120, '#1E90FF', 'al iniciar', hat=True) + _bloque(22, 84, 214, '#1E90FF', 'mostrar cadena', cadena='Hola clase!'))
    s += _tarjeta(408, 0, 246, 120, 'MicroBlocks', '#D18C25',
                  _bloque(14, 54, 124, '#D18C25', 'al empezar', hat=True) + _bloque(22, 84, 214, '#4852BF', 'anima el texto', cadena='Hola clase!'))
    py = ('<text x="14" y="62" font-size="12.5" fill="#15202b" font-family="ui-monospace,Consolas,monospace">'
          '<tspan fill="#c2185b">from</tspan> microbit <tspan fill="#c2185b">import</tspan> *</text>'
          '<text x="14" y="90" font-size="12.5" fill="#15202b" font-family="ui-monospace,Consolas,monospace">display.scroll(</text>'
          '<text x="14" y="108" font-size="12.5" fill="#0f8a72" font-family="ui-monospace,Consolas,monospace">  "Hola clase!")</text>')
    s += _tarjeta(456, 424, 204, 120, 'Python', '#0f8a72', py)
    return s + '</svg>'
