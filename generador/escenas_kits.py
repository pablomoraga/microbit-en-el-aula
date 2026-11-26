# -*- coding: utf-8 -*-
"""Kits y robots en perspectiva (dibujos propios). Solo se señalan elementos y pines que aparecen en la
documentación oficial del fabricante o en el código de su extensión oficial de MakeCode."""
from iso import Escena, mix
from placa import SONRISA, CORAZON

WIKI = {
    'cutebot': '<a href="https://wiki.elecfreaks.com/en/microbit/microbit-smart-car/microbit-smart-cutebot/" target="_blank" rel="noopener">wiki de ELECFREAKS</a>',
    'maqueen': '<a href="https://wiki.dfrobot.com/rob0148-en/" target="_blank" rel="noopener">wiki de DFRobot</a> y extensión oficial pxt-maqueen',
    'maqueenplus': '<a href="https://wiki.dfrobot.com/mbt0021-en/" target="_blank" rel="noopener">wiki de DFRobot</a> y extensión oficial pxt-DFRobot_MaqueenPlus_v20',
    'wonder': '<a href="https://wiki.elecfreaks.com/en/microbit/building-blocks/wonder-building-kit/" target="_blank" rel="noopener">wiki de ELECFREAKS</a>',
    'agri': '<a href="https://wiki.elecfreaks.com/en/microbit/wisdom-life/microbit-smart-agriculture-kit/" target="_blank" rel="noopener">wiki de ELECFREAKS</a>',
}

def _rueda(s, u, vc, r, ancho, color='#2b2f36'):
    """Rueda vertical vista de lado (eje paralelo a u), construida por capas."""
    x = u
    while x < u + ancho:
        s.add('<g transform="%s"><circle cx="%.1f" cy="%.1f" r="%d" fill="%s"/></g>' % (s.lateral(x, 0, 0), vc, -r, r, mix(color, .8)))
        x += 4
    s.add('<g transform="%s"><circle cx="%.1f" cy="%.1f" r="%d" fill="%s"/><circle cx="%.1f" cy="%.1f" r="%d" fill="#9aa1aa"/>'
          '<circle cx="%.1f" cy="%.1f" r="%d" fill="none" stroke="#4a5059" stroke-width="6" stroke-dasharray="10 8"/></g>' % (
              s.lateral(u + ancho, 0, 0), vc, -r, r, color, vc, -r, r * .38, vc, -r, r * .8))
    s.P(u, vc - r, 0); s.P(u + ancho, vc + r, 0); s.P(u, vc, 2 * r); s.P(u + ancho, vc, 2 * r)

def _robot(s, color, w=560, d=600, h=150, z0=60, rueda=120, faros=None):
    """Chasis apoyado sobre dos ruedas traseras; el frente mira hacia el espectador (v grande)."""
    vc = d * .30
    _rueda(s, -60, vc, rueda, 50)                              # rueda izquierda (detrás del chasis)
    s.sombra(-20, 0, w + 40, d)
    s.caja(0, 0, w, d, h, color, z=z0, rx=40, sombra=False)
    _rueda(s, w + 6, vc, rueda, 50)                            # rueda derecha
    _faros(s, w, d, z0, h, faros)
    return z0 + h

def _ultra(s, w, d, top):
    """Sensor de ultrasonidos en el borde delantero (se dibuja después de la placa)."""
    z0, h = top, 0
    if True:
        s.caja(w / 2 - 150, d - 70, 300, 60, 120, '#2e78d6', z=z0 + h, sombra=False)
        for du in (60, 240):
            for k in range(0, 24, 4):
                s.add('<g transform="%s"><circle cx="%d" cy="-60" r="44" fill="%s"/></g>' % (s.frontal(w / 2 - 150, d - 10 + k, z0 + h), du, '#9aa1aa' if k < 20 else '#c9ced6'))
            s.add('<g transform="%s"><circle cx="%d" cy="-60" r="26" fill="#2b2f36"/></g>' % (s.frontal(w / 2 - 150, d + 14, z0 + h), du))

def _faros(s, w, d, z0, h, faros):
    if faros:
        for du in (70, w - 70):
            s.add('<g transform="%s"><circle cx="%d" cy="%d" r="24" fill="#fff"/><circle cx="%d" cy="%d" r="24" fill="none" stroke="%s" stroke-width="8"/></g>' % (
                s.frontal(0, d, z0 + h), du, h / 2, du, h / 2, faros))

def cutebot():
    s = Escena(760, 520, s=0.5)
    top = _robot(s, '#2e78d6', faros='#ffcc00')
    s.caja(140, 20, 280, 160, 70, '#20252c', z=top, sombra=False)          # portapilas 3 × AA
    for i in range(3):
        s.add('<g transform="%s"><rect x="%d" y="%d" width="240" height="34" rx="16" fill="#c79a3a"/></g>' % (s.M(top + 72), 160, 36 + i * 46))
    s.microbit(130, 215, 300, z=top, lit=CORAZON, uid='cb')
    _ultra(s, 560, 600, top)
    s.punto(280, 600, top + 120, 'Ultrasonidos HC-SR04', 'Delante (P8 y P12). Mide distancias de 2 a 400 cm.')
    s.punto(70, 600, 135, 'Faros RGB', 'Dos, uno a cada lado del frente.')
    s.punto(616, 260, 120, 'Ruedas motrices', 'Micromotores de 300 RPM.')
    s.punto(280, 330, top + 12, 'micro:bit', 'Se inserta en la ranura del robot.')
    s.punto(280, 80, top + 72, 'Portapilas 3 × AA', 'Con puertos I2C, servo S1-S2, P1 y P2.')
    s.punto(280, 600, 90, 'Debajo del chasis', 'Sensores de línea en P13 (izquierdo) y P14 (derecho) y dos LED de colores en P15. Detrás, el receptor de infrarrojos (P16).')
    return s.figura('Cutebot (esquema en perspectiva)', WIKI['cutebot'])

def maqueen():
    s = Escena(760, 520, s=0.5)
    top = _robot(s, '#c0392b', w=520, d=560, faros='#e74c3c')
    for i in range(3):
        s.caja(120 + i * 100, 20, 70, 40, 30, '#2b2f36', z=top, sombra=False)
    s.microbit(110, 140, 300, z=top, lit=SONRISA, uid='mq')
    _ultra(s, 520, 560, top)
    s.punto(260, 560, top + 120, 'Ultrasonidos', 'TRIG en P1 y ECHO en P2 (extensión maqueen).')
    s.punto(70, 560, 135, 'Luces LED', 'Izquierda en P8 y derecha en P12.')
    s.punto(576, 250, 120, 'Motores M1 y M2', 'Izquierdo y derecho.')
    s.punto(260, 260, top + 12, 'micro:bit', 'Se inserta en la ranura del robot.')
    s.punto(220, 40, top + 30, 'Puertos Gravity', 'P0, P1 y P2.')
    s.punto(260, 560, 90, 'Sensores de línea (debajo)', 'P13 y P14. Dan 0 sobre negro y 1 sobre blanco.')
    return s.figura('Maqueen Lite (esquema en perspectiva)', WIKI['maqueen'])

def maqueen_plus():
    s = Escena(760, 520, s=0.5)
    top = _robot(s, '#2b2f36', w=600, d=600, h=170)
    s.cilindro(520, 100, 30, 14, '#e0a83a', z=top)
    s.microbit(150, 160, 300, z=top, lit=SONRISA, uid='mqp')
    _ultra(s, 600, 600, top)
    s.punto(300, 600, top + 120, 'Ultrasonidos', 'TRIG en P13 y ECHO en P14.')
    s.punto(656, 260, 120, 'Motores', 'Izquierdo y derecho.')
    s.punto(300, 280, top + 12, 'micro:bit', 'Se inserta en la ranura del robot.')
    s.punto(520, 100, top + 14, 'Botón de calibración', 'Para los sensores de línea.')
    s.punto(300, 600, 100, '5 sensores de línea (debajo)', 'L2, L1, M, R1 y R2. Dan 1 sobre negro.')
    return s.figura('Maqueen Plus V2 (esquema en perspectiva)', WIKI['maqueenplus'])

def wonder_moto():
    s = Escena(760, 480, s=0.5)
    s.sombra(120, 80, 180, 700)
    _rueda(s, 170, 140, 150, 60)                                           # rueda trasera
    s.caja(250, 120, 90, 120, 90, '#8a8f97', z=105, sombra=False)          # motor 1
    s.caja(150, 260, 140, 260, 200, '#e8e8e8', z=110, sombra=False, borde='#9aa1aa')   # chasis de piezas
    for i in range(3):
        for j in range(2):
            s.cilindro(175 + j * 70, 290 + i * 80, 18, 10, '#e8e8e8', z=310)
    s.caja(120, 290, 200, 190, 30, '#2e78d6', z=320, sombra=False)          # placa WuKong
    s.microbit(130, 300, 180, z=350, lit=CORAZON, uid='wk')
    s.caja(250, 540, 90, 120, 90, '#8a8f97', z=105, sombra=False)          # motor 2
    _rueda(s, 170, 640, 150, 60)                                           # rueda delantera
    s.punto(295, 180, 195, 'Motor 1', 'Conectado a M1 de la placa WuKong.')
    s.punto(295, 600, 195, 'Motor 2', 'Conectado a M2.')
    s.punto(220, 375, 362, 'Placa WuKong con la micro:bit', 'A: adelante · B: atrás · A+B: parar.')
    s.punto(290, 500, 200, 'Piezas compatibles con LEGO', 'Montaje según la guía del caso «The Motorcycle».')
    return s.figura('Wonder Building Kit · la moto (esquema)', WIKI['wonder'])

def smart_agri():
    s = Escena(760, 480, s=0.5)
    s.caja(-60, -40, 1220, 780, 16, '#e9dcc0', sombra=False, tapa='#efe4cc')
    z0 = 16
    s.cilindro(200, 220, 130, 150, '#b5653a', z=z0, tapa='#6b4226')         # maceta con tierra
    for (a, b, c) in ((-70, 40, '#2e9d4f'), (0, 90, '#3fb562'), (60, 20, '#2e9d4f')):
        s.add(s.poly([(200, 220, z0 + 150), (200 + a, 220 + b, z0 + 230), (200 + a * .5, 220 + b * .5, z0 + 290)], c))
    s.add(s.poly([(250, 260, z0 + 120), (290, 260, z0 + 120), (290, 260, z0 + 230), (250, 260, z0 + 230)], '#e2a400'))   # sensor de humedad clavado
    s.caja(520, 60, 220, 220, 260, '#bfe3ff', z=z0, tapa='#6fb6f0', borde='#2e78d6')   # depósito
    s.add(s.poly([(600, 280, z0 + 40), (650, 280, z0 + 40), (650, 280, z0 + 240), (600, 280, z0 + 240)], '#e2a400'))  # sensor de nivel
    s.caja(420, 360, 110, 70, 60, '#2e78d6', z=z0)                          # servo (válvula)
    s.cable((290, 300), (860, 560), '#c0392b', z=z0 + 3, grosor=10, curva=120)
    s.cable((650, 300), (920, 560), '#262a30', z=z0 + 3, grosor=10, curva=100)
    s.cable((530, 420), (980, 560), '#e2a400', z=z0 + 3, grosor=10, curva=80)
    s.caja(820, 320, 320, 280, 50, '#20252c', z=z0)                          # IoT:bit
    s.microbit(850, 330, 260, z=z0 + 50, lit=GOTA_K, uid='ag')
    s.punto(270, 260, z0 + 200, 'Sensor de humedad del suelo', 'Puerto P1 de la IoT:bit.')
    s.punto(625, 280, z0 + 160, 'Sensor de nivel de agua', 'Puerto P2.')
    s.punto(475, 430, z0 + 50, 'Servo (válvula)', 'Puerto P9.')
    s.punto(980, 440, z0 + 62, 'IoT:bit con la micro:bit', 'Placa de expansión del kit.')
    return s.figura('Smart Agriculture Kit · riego automático (esquema)', WIKI['agri'])

GOTA_K = {(0, 2), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3)}
