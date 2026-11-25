# -*- coding: utf-8 -*-
"""Ilustración de la portada: micro:bit V2 en vista tres cuartos sobre la mesa,
con cables de cocodrilo, LED, pulsadores y una resistencia (dibujo propio en SVG)."""
import math
from placa import frente, _nested, CORAZON

def _led3d(x, y, col, rot=0, glow=False, uid='a'):
    g = 'lg' + uid
    s = '<g transform="translate(%.1f %.1f) rotate(%s)">' % (x, y, rot)
    s += '<ellipse cx="4" cy="34" rx="22" ry="7" fill="#2b2118" opacity=".2" filter="url(#hpblur)"/>'
    s += ('<defs><linearGradient id="%s" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="%s"/>'
          '<stop offset=".42" stop-color="#ffffff" stop-opacity=".6"/><stop offset=".6" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>') % (g, col, col, col)
    s += '<path d="M-4 16 V34 l-9 6 M4 16 V30 l11 8" stroke="#a9adb3" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    if glow:
        s += '<circle cx="0" cy="-6" r="28" fill="%s" opacity=".16"/>' % col
    s += '<ellipse cx="0" cy="16" rx="13.5" ry="4" fill="%s"/><rect x="-13.5" y="11" width="27" height="5" fill="%s"/>' % (col, col)
    s += '<ellipse cx="0" cy="11" rx="13.5" ry="4" fill="%s" opacity=".85"/>' % col
    s += '<path d="M-10.5 11 V-8 a10.5 10.5 0 0 1 21 0 V11 Z" fill="url(#%s)" opacity=".95"/>' % g
    s += '<path d="M-6 -9 a6 7 0 0 1 4 -6" stroke="#fff" stroke-width="2.4" fill="none" opacity=".85" stroke-linecap="round"/>'
    return s + '</g>'

def _boton3d(x, y, cap, rot=0):
    s = '<g transform="translate(%.1f %.1f) rotate(%s)">' % (x, y, rot)
    s += '<ellipse cx="6" cy="20" rx="30" ry="9" fill="#2b2118" opacity=".22" filter="url(#hpblur)"/>'
    s += '<path d="M-19 6 l-7 9 M19 6 l7 9 M-19 -8 l-7 -5 M19 -8 l7 -5" stroke="#a9adb3" stroke-width="2.2" stroke-linecap="round"/>'
    s += '<path d="M-21 -6 L0 -17 L21 -6 L21 4 L0 15 L-21 4 Z" fill="#1d2126"/>'
    s += '<path d="M-21 -6 L0 -17 L21 -6 L0 5 Z" fill="#3d434c"/><path d="M0 5 L21 -6 L21 4 L0 15Z" fill="#121418"/>'
    s += '<ellipse cx="0" cy="-5" rx="9.5" ry="5" fill="#000" opacity=".35"/>'
    s += '<path d="M-9.5 -10 v4 a9.5 5 0 0 0 19 0 v-4" fill="%s"/><path d="M-9.5 -10 v4 a9.5 5 0 0 0 19 0 v-4" fill="#000" opacity=".25"/>' % cap
    s += '<ellipse cx="0" cy="-10" rx="9.5" ry="5" fill="%s"/><ellipse cx="-2.5" cy="-11.5" rx="4" ry="1.6" fill="#fff" opacity=".5"/>' % cap
    return s + '</g>'

def _resistencia3d(x, y, rot=0):
    s = '<g transform="translate(%.1f %.1f) rotate(%s)">' % (x, y, rot)
    s += '<ellipse cx="4" cy="12" rx="38" ry="5" fill="#2b2118" opacity=".2" filter="url(#hpblur)"/>'
    s += '<path d="M-46 0 H46" stroke="#a9adb3" stroke-width="2" stroke-linecap="round"/>'
    s += '<path d="M-20 -7 h40 a6 7 0 0 1 0 14 h-40 a6 7 0 0 1 0 -14z" fill="url(#hpres)"/>'
    for bx, c in ((-14, '#c0392b'), (-7, '#c0392b'), (0, '#5b3a29'), (13, '#c8a24a')):
        s += '<rect x="%d" y="-7" width="3.6" height="14" fill="%s"/>' % (bx, c)
    s += '<path d="M-20 -4 h40" stroke="#fff" stroke-opacity=".45" stroke-width="2" stroke-linecap="round"/>'
    return s + '</g>'

def _pinza3d(x, y, ang, col, uid):
    s = '<g transform="translate(%.1f %.1f) rotate(%.1f)">' % (x, y, ang)
    s += ('<defs><linearGradient id="pz%s" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="%s"/><stop offset=".33" stop-color="#ffffff" stop-opacity=".4"/>'
          '<stop offset=".5" stop-color="%s"/><stop offset="1" stop-color="#000" stop-opacity=".45"/></linearGradient></defs>') % (uid, col, col)
    s += '<path d="M-7 -2 L-5 -34 Q0 -41 5 -34 L7 -2 Z" fill="url(#hpmetal)" stroke="#6b7078" stroke-width=".8"/>'
    s += '<path d="M-4.6 -30 h9.2 M-4.9 -24 h9.8 M-5.2 -18 h10.4" stroke="#6b7078" stroke-width="1.2"/>'
    s += '<path d="M-10 0 Q-12.5 30 -9 58 Q0 65 9 58 Q12.5 30 10 0 Q0 -4 -10 0Z" fill="%s"/>' % col
    s += '<path d="M-10 0 Q-12.5 30 -9 58 Q0 65 9 58 Q12.5 30 10 0 Q0 -4 -10 0Z" fill="url(#pz%s)"/>' % uid
    s += '<path d="M-6 8 Q0 6 6 8 M-6.5 16 Q0 14 6.5 16 M-7 24 Q0 22 7 24" stroke="#000" stroke-opacity=".2" stroke-width="1.4" fill="none"/>'
    return s + '</g>'

def hero():
    W, H = 700, 580
    sc = 0.92
    ax, ay, bx, by = .86 * sc, .13 * sc, -.30 * sc, .56 * sc      # ejes del plano de la mesa
    X, Y = 215, 34
    P = lambda u, v: (X + u * ax + v * bx, Y + u * ay + v * by)
    M = 'matrix(%.4f %.4f %.4f %.4f %.1f %.1f)' % (ax, ay, bx, by, X, Y)
    s = ('<svg class="placa-svg hero-pro" viewBox="0 0 %d %d" role="img" aria-label="Ilustración de una micro:bit V2 sobre la mesa '
         'con dos cables de cocodrilo, LED, pulsadores y una resistencia">' % (W, H))
    s += ('<defs><filter id="hpblur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4"/></filter>'
          '<filter id="hpshadow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="16"/></filter>'
          '<radialGradient id="hpbg" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#fff8ec"/><stop offset=".75" stop-color="#f7ead4"/>'
          '<stop offset="1" stop-color="#f7ead4" stop-opacity="0"/></radialGradient>'
          '<linearGradient id="hpedge" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0b0d10"/><stop offset="1" stop-color="#262b32"/></linearGradient>'
          '<linearGradient id="hpgold" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6d985"/><stop offset="1" stop-color="#9c6f17"/></linearGradient>'
          '<linearGradient id="hpwire" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".5"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
          '<linearGradient id="hpmetal" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8d939b"/><stop offset=".45" stop-color="#f1f3f5"/><stop offset="1" stop-color="#7c828a"/></linearGradient>'
          '<linearGradient id="hpres" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4e3bd"/><stop offset=".55" stop-color="#d9bd88"/><stop offset="1" stop-color="#a78755"/></linearGradient>'
          '</defs>')
    # halo cálido y rejilla de puntos
    s += '<ellipse cx="350" cy="320" rx="350" ry="255" fill="url(#hpbg)"/>'
    s += ''.join('<circle cx="%d" cy="%d" r="1.3" fill="#d6bf94" opacity=".6"/>' % (x, y) for x in range(60, 650, 26) for y in range(120, 560, 26)
                 if ((x - 350) / 325.0) ** 2 + ((y - 330) / 220.0) ** 2 < 1)
    # sombra de la placa
    s += '<g transform="translate(22 38) %s"><rect x="20" y="30" width="500" height="400" rx="30" fill="#3b2a20" opacity=".42" filter="url(#hpshadow)"/></g>' % M
    # canto de la placa (grosor)
    s += '<g transform="translate(0 12) %s"><path d="M42 18 h456 a22 22 0 0 1 22 22 V425 H20 V40 a22 22 0 0 1 22 -22z" fill="url(#hpedge)"/></g>' % M
    # dedos dorados en el canto frontal
    for i in range(56):
        x0, y0 = P(34 + i * (472 / 55.0), 425)
        s += '<path d="M%.1f %.1f l%.2f %.2f v11 l%.2f %.2f z" fill="url(#hpgold)"/>' % (x0, y0, 3.4 * ax, 3.4 * ay, -3.4 * ax, -3.4 * ay)
    for f in (0.1, 0.3, 0.5, 0.7, 0.9):
        x0, y0 = P(20 + 500 * f - 27, 425)
        s += '<path d="M%.1f %.1f l%.2f %.2f v12 l%.2f %.2f z" fill="url(#hpgold)"/>' % (x0, y0, 54 * ax, 54 * ay, -54 * ax, -54 * ay)
    # cara de la placa
    s += '<g transform="%s">%s</g>' % (M, _nested(frente(callouts=False, lit=CORAZON, uid='pro'), 0, 0, 540, 450))
    s += '<g transform="%s"><path d="M42 18 h280 L110 425 H20 V40 a22 22 0 0 1 22 -22z" fill="#fff" opacity=".045"/></g>' % M
    # cables de cocodrilo desde 3V y GND hacia la derecha
    n = math.hypot(bx, by); dx, dy = bx / n, by / n            # dirección «hacia delante» en la mesa
    vang = math.degrees(math.atan2(dy, dx)) - 90
    for f, col, end, uid in ((0.7, '#c0392b', (712, 440), 'r'), (0.9, '#262a30', (712, 510), 'k')):
        rx, ry = P(20 + 500 * f, 381)
        sx, sy = rx + dx * 84, ry + dy * 84
        path = 'M%.1f %.1f C %.1f %.1f, %.1f %.1f, %d %d' % (sx, sy, sx + dx * 55, sy + dy * 55, end[0] - 170, end[1] + 6, end[0], end[1])
        s += '<path d="%s" stroke="#3b2a20" stroke-opacity=".28" stroke-width="9" fill="none" transform="translate(6 10)" filter="url(#hpblur)"/>' % path
        s += '<path d="%s" stroke="%s" stroke-width="8" fill="none" stroke-linecap="round"/>' % (path, col)
        s += '<path d="%s" stroke="url(#hpwire)" stroke-width="3" fill="none" transform="translate(-1 -2)"/>' % path
        s += '<g transform="translate(%.1f %.1f) scale(1.3) translate(%.1f %.1f)">%s</g>' % (rx, ry, -rx, -ry, _pinza3d(rx, ry, vang, col, uid))
    # componentes sueltos delante, a la izquierda
    for f, args in ((_resistencia3d, (290, 500, -14)), (_boton3d, (95, 420, '#e0a83a', 8)), (_boton3d, (205, 530, '#c0392b', -12)),
                    (_led3d, (55, 505, '#e74c3c', -20, True, 'r')), (_led3d, (160, 462, '#27ae60', 14, False, 'g')), (_led3d, (380, 535, '#2e86de', 62, True, 'b'))):
        x, y = args[0], args[1]
        s += '<g transform="translate(%d %d) scale(1.25) translate(%d %d)">%s</g>' % (x, y, -x, -y, f(*args))
    return s + '</svg>'
