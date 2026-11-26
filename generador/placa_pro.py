# -*- coding: utf-8 -*-
"""Ilustración de la portada con una perspectiva coherente: una sola proyección (cámara ortográfica
girada 20° y elevada unos 33°) para la mesa, la placa, su grosor, los cables y los componentes."""
import math
from placa import frente, _nested, CORAZON

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
    s += '<g transform="%s">%s</g>' % (M(BT), _nested(frente(callouts=False, lit=CORAZON, uid='pro'), 0, 0, 540, 450))
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

def _bloque(x, y, w, color, txt, hat=False, heart=False):
    """Bloque de programación estilizado (tapa redondeada si es un evento)."""
    h = 30
    top = 'M%d %d q0 -14 %d -14 h%d q%d 0 %d 14' % (x, y, 34, w - 68, 34, 34) if hat else 'M%d %d h%d' % (x, y, w)
    d = '%s v%d h-%d z' % (top, h, w) if hat else 'M%d %d h%d v%d h-%d z' % (x, y, w, h, w)
    s = '<path d="%s" fill="%s"/>' % (d, color)
    s += '<text x="%d" y="%d" font-size="13" font-weight="700" fill="#fff" font-family="system-ui,sans-serif">%s</text>' % (x + 10, y + 20, txt)
    if heart:
        s += '<rect x="%d" y="%d" width="24" height="24" rx="4" fill="#fff" opacity=".95"/>' % (x + w - 32, y + 3) + _corazon(x + w - 29, y + 6.5, 3.6, '#e3204b')
    return s

def hero():
    global S, X0, Y0
    W, H = 720, 560
    S, X0, Y0 = 0.78, 250, 236
    s = ('<svg class="placa-svg hero-pro" viewBox="0 0 %d %d" role="img" aria-label="La micro:bit V2 muestra un corazón; alrededor, el mismo programa '
         'en MakeCode, MicroBlocks y Python">' % (W, H))
    s += ('<defs><filter id="hpblur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>'
          '<filter id="hpshadow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="16"/></filter>'
          '<filter id="hpglow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="22"/></filter>'
          '<radialGradient id="hpbg" cx=".5" cy=".55" r=".55"><stop offset="0" stop-color="#ffffff"/><stop offset=".7" stop-color="#e6edf5"/><stop offset="1" stop-color="#e6edf5" stop-opacity="0"/></radialGradient>'
          '<linearGradient id="hpgold" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6d985"/><stop offset="1" stop-color="#9c6f17"/></linearGradient>'
          '</defs>')
    s += '<ellipse cx="360" cy="320" rx="360" ry="250" fill="url(#hpbg)"/>'
    # retícula de puntos en el plano de la mesa
    s += '<g transform="%s" opacity=".5">' % M(0)
    for u in range(-300, 900, 40):
        for v in range(-160, 700, 40):
            x, y = P(u, v, 0)
            if ((x - 360) / 340.0) ** 2 + ((y - 330) / 220.0) ** 2 < 1:
                s += '<circle cx="%d" cy="%d" r="2" fill="#b8c4d2"/>' % (u, v)
    s += '</g>'
    # brillo del corazón y placa
    gx, gy = P(270, 215, BT)
    s += _placa()
    s += '<ellipse cx="%.0f" cy="%.0f" rx="70" ry="44" fill="#ff3b5c" opacity=".22" filter="url(#hpglow)"/>' % (gx, gy)
    # líneas de las tarjetas a la pantalla
    for (x, y) in ((250, 160), (520, 150), (560, 400)):
        s += '<path d="M%d %d Q %.0f %.0f %.0f %.0f" stroke="#15202b" stroke-width="1.6" stroke-dasharray="5 6" fill="none" opacity=".55"/>' % (
            x, y, (x + gx) / 2, min(y, gy) - 30, gx, gy)
    # tarjetas: el mismo programa en los tres editores
    s += _tarjeta(4, 8, 220, 120, 'MakeCode', '#1E90FF',
                  _bloque(14, 54, 120, '#1E90FF', 'al iniciar', hat=True) + _bloque(26, 84, 180, '#1E90FF', 'mostrar ícono', heart=True))
    s += _tarjeta(430, 0, 226, 120, 'MicroBlocks', '#D18C25',
                  _bloque(14, 54, 124, '#D18C25', 'al empezar', hat=True) + _bloque(26, 84, 186, '#4852BF', 'muestra imagen', heart=True))
    py = ('<text x="16" y="60" font-size="12.5" fill="#15202b" font-family="ui-monospace,Consolas,monospace">'
          '<tspan fill="#c2185b">from</tspan> microbit <tspan fill="#c2185b">import</tspan> *</text>'
          '<text x="16" y="84" font-size="12.5" fill="#15202b" font-family="ui-monospace,Consolas,monospace">display.show(</text>'
          '<text x="16" y="104" font-size="12.5" fill="#0f8a72" font-family="ui-monospace,Consolas,monospace">    Image.HEART)</text>')
    s += _tarjeta(456, 396, 204, 120, 'Python', '#0f8a72', py)
    return s + '</svg>'
