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

def hero():
    W, H = 700, 560
    s = ('<svg class="placa-svg hero-pro" viewBox="0 0 %d %d" role="img" aria-label="Ilustración de una micro:bit V2 sobre la mesa '
         'con dos cables de cocodrilo, LED, pulsadores y una resistencia">' % (W, H))
    s += ('<defs><filter id="hpblur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5"/></filter>'
          '<filter id="hpshadow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="18"/></filter>'
          '<radialGradient id="hpbg" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#fff8ec"/><stop offset=".75" stop-color="#f7ead4"/><stop offset="1" stop-color="#f7ead4" stop-opacity="0"/></radialGradient>'
          '<linearGradient id="hpgold" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6d985"/><stop offset="1" stop-color="#9c6f17"/></linearGradient>'
          '<linearGradient id="hpmetal" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8d939b"/><stop offset=".45" stop-color="#f1f3f5"/><stop offset="1" stop-color="#7c828a"/></linearGradient>'
          '<linearGradient id="hpboot" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#000" stop-opacity=".25"/><stop offset=".35" stop-color="#fff" stop-opacity=".35"/><stop offset=".6" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".3"/></linearGradient>'
          '<linearGradient id="hpres" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4e3bd"/><stop offset=".55" stop-color="#d9bd88"/><stop offset="1" stop-color="#a78755"/></linearGradient>'
          '</defs>')
    # halo cálido y retícula de la mesa, en el mismo plano
    s += '<ellipse cx="350" cy="330" rx="350" ry="230" fill="url(#hpbg)"/>'
    s += '<g transform="%s" opacity=".55">' % M(0)
    for u in range(-260, 900, 40):
        for v in range(-120, 760, 40):
            x, y = P(u, v, 0)
            if ((x - 350) / 330.0) ** 2 + ((y - 330) / 215.0) ** 2 < 1:
                s += '<circle cx="%d" cy="%d" r="2.2" fill="#d6bf94"/>' % (u, v)
    s += '</g>'
    # la placa
    s += _placa()
    # cables y pinzas (3V y GND) hacia la derecha
    s += _cable(370, '#c0392b', (980, 560), 'r') + _cable(470, '#262a30', (1000, 700), 'k')
    # componentes delante, a la izquierda, desordenados
    s += _resistencia(70, 570, 14)
    s += _pulsador(-210, 500, '#e0a83a') + _led(-70, 700, -28, '#e74c3c', True) + _led(-250, 770, 20, '#27ae60')
    s += _pulsador(130, 700, '#c0392b') + _led(320, 880, -70, '#2e86de', True)
    return s + '</svg>'
