# -*- coding: utf-8 -*-
"""Esquemas de conexión con cables de cocodrilo (dibujos propios en SVG)."""
import html
e = html.escape

W = 640
RX = {'P0': 80, 'P1': 200, 'P2': 320, '3V': 440, 'GND': 560}      # centro de cada anillo
RY = 112
COL = {'rojo': '#d63b2f', 'amarillo': '#e2a400', 'verde': '#2e9d4f', 'azul': '#2e78d6', 'negro': '#2b2f36', 'naranja': '#ef7d1a', 'marron': '#7a4a26', 'blanco': '#c9ced6'}

def _placa():
    s = ('<defs><linearGradient id="cxau" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f3d27a"/><stop offset="1" stop-color="#a9791c"/></linearGradient></defs>'
         '<path d="M20 26 h600 v118 h-600z" fill="#1f242b"/><text x="320" y="52" text-anchor="middle" font-size="15" font-weight="800" fill="#c9d2dc">micro:bit · conector de borde</text>')
    for i in range(52):
        s += '<rect x="%.1f" y="98" width="3" height="46" fill="url(#cxau)"/>' % (34 + i * 11.3)
    for lab, x in RX.items():
        s += '<rect x="%d" y="80" width="64" height="64" rx="8" fill="url(#cxau)"/><circle cx="%d" cy="%d" r="15" fill="#fff" stroke="#9c7420" stroke-width="2"/>' % (x - 32, x, RY)
        s += '<text x="%d" y="74" text-anchor="middle" font-size="15" font-weight="800" fill="#fff">%s</text>' % (x, lab)
    return s

def _cable(ring, x, y, color, dy=0):
    rx = RX[ring]
    c = COL[color]
    s = '<path d="M%d %d C %d %d, %d %d, %d %d" stroke="%s" stroke-width="6" fill="none" stroke-linecap="round"/>' % (rx, RY + 20, rx, RY + 110 + dy, x, y - 90, x, y, c)
    # pinza sobre el anillo
    s += ('<g transform="translate(%d %d)"><path d="M-9 4 L-12 34 Q0 40 12 34 L9 4Z" fill="%s"/><path d="M-5 4 L-4 -16 Q0 -20 4 -16 L5 4Z" fill="#c9ced6" stroke="#7c828a"/></g>') % (rx, RY + 4, c)
    return s

def _etiqueta(x, y, t):
    return '<text x="%d" y="%d" text-anchor="middle" font-size="14" font-weight="700" fill="#15202b">%s</text>' % (x, y, e(t))

def _fruta(x, y, color, t):
    return ('<circle cx="%d" cy="%d" r="30" fill="%s"/><path d="M%d %d q6 -14 16 -16" stroke="#5a3d1e" stroke-width="3" fill="none"/>'
            '<ellipse cx="%d" cy="%d" rx="9" ry="5" fill="#fff" opacity=".35"/>' % (x, y + 26, color, x, y - 2, x - 10, y + 14)) + _etiqueta(x, y + 78, t)

def _mano(x, y, t):
    return ('<path d="M%d %d c-14 0 -22 -12 -22 -26 v-22 c0 -5 8 -5 8 0 v14 v-30 c0 -5 8 -5 8 0 v26 v-30 c0 -5 8 -5 8 0 v30 v-26 c0 -5 8 -5 8 0 v30 v-12 c0 -5 8 -5 8 0 v22 c0 16 -10 24 -18 24z"'
            ' fill="#f6c9a8" stroke="#a86a45" stroke-width="2" transform="translate(0 24)"/>' % (x + 4, y + 30)) + _etiqueta(x, y + 78, t)

def _led(x, y, color, t, resistencia=True):
    c = COL[color]
    s = ''
    if resistencia:
        s += ('<rect x="%d" y="%d" width="14" height="34" rx="5" fill="#d9c39a" stroke="#8a6d3b"/><path d="M%d %d h14 M%d %d h14 M%d %d h14" stroke="#c0392b" stroke-width="3"/>'
              % (x - 7, y - 4, x - 7, y + 4, x - 7, y + 11, x - 7, y + 18))
        s += '<text x="%d" y="%d" font-size="11" fill="#5b6675">220 Ω</text>' % (x + 12, y + 16)
        y += 46
    s += '<path d="M%d %d v-14 M%d %d v-14" stroke="#9aa1aa" stroke-width="3"/>' % (x, y - 2, x + 0, y - 2)
    s += '<path d="M%d %d v30 M%d %d v22" stroke="#9aa1aa" stroke-width="3"/>' % (x - 5, y + 30, x + 5, y + 30)
    s += '<path d="M%d %d v-18 a12 12 0 0 1 24 0 v18z" fill="%s"/><rect x="%d" y="%d" width="28" height="5" rx="1" fill="%s"/>' % (x - 12, y + 30, c, x - 14, y + 28, c)
    s += '<text x="%d" y="%d" font-size="11" fill="#5b6675">+ larga</text>' % (x - 46, y + 50)
    return s + _etiqueta(x, y + 82, t)

def _aluminio(x, y, w, t):
    return ('<rect x="%d" y="%d" width="%d" height="34" rx="3" fill="#d4d9df" stroke="#8b939c"/><path d="M%d %d l%d 10 M%d %d l%d -8" stroke="#fff" stroke-width="2" opacity=".8"/>'
            % (x - w // 2, y, w, x - w // 2 + 6, y + 8, w // 3, x, y + 26, w // 3)) + _etiqueta(x, y + 58, t)

def _clavos(x, y, t):
    s = ('<path d="M%d %d h150 l-18 80 h-114z" fill="#8a5a33"/><path d="M%d %d h150" stroke="#5e3b1f" stroke-width="10"/>'
         '<ellipse cx="%d" cy="%d" rx="72" ry="8" fill="#5b3a1f"/>' % (x - 75, y + 20, x - 75, y + 20, x, y + 22))
    for dx in (-30, 30):
        s += '<rect x="%d" y="%d" width="5" height="58" fill="#9aa1aa"/><rect x="%d" y="%d" width="15" height="5" rx="2" fill="#9aa1aa"/>' % (x + dx - 2, y - 6, x + dx - 7, y - 8)
    s += '<path d="M%d %d c-8 -14 -4 -30 10 -36 c4 12 2 26 -10 36z M%d %d c6 -14 18 -20 30 -16 c-4 12 -18 18 -30 16z" fill="#2e9d4f"/>' % (x - 4, y + 16, x, y + 16)
    return s + _etiqueta(x, y + 124, t)

def _potenciometro(x, y, t):
    s = '<rect x="%d" y="%d" width="90" height="50" rx="8" fill="#2e78d6"/><circle cx="%d" cy="%d" r="18" fill="#dfe3e8" stroke="#8b939c" stroke-width="2"/>' % (x - 45, y, x, y + 25)
    s += '<path d="M%d %d v-12" stroke="#2b2f36" stroke-width="4" stroke-linecap="round"/>' % (x, y + 25)
    for dx in (-30, 0, 30):
        s += '<rect x="%d" y="%d" width="6" height="18" fill="#9aa1aa"/>' % (x + dx - 3, y - 16)
    return s + _etiqueta(x, y + 76, t)

def _servo(x, y, t):
    s = ('<rect x="%d" y="%d" width="110" height="56" rx="6" fill="#2e78d6"/><rect x="%d" y="%d" width="140" height="10" rx="3" fill="#2e78d6"/>'
         '<circle cx="%d" cy="%d" r="12" fill="#f2f2f2"/><path d="M%d %d h60" stroke="#f2f2f2" stroke-width="10" stroke-linecap="round"/>'
         % (x - 55, y, x - 70, y + 12, x + 25, y + 18, x + 25, y + 18))
    return s + _etiqueta(x, y + 82, t)

def _anilla(x, y, t):
    return ('<circle cx="%d" cy="%d" r="18" fill="none" stroke="#9aa1aa" stroke-width="5"/><path d="M%d %d v44" stroke="#9aa1aa" stroke-width="5"/>'
            '<rect x="%d" y="%d" width="14" height="30" rx="5" fill="#ef7d1a"/>' % (x, y + 18, x, y + 36, x - 7, y + 64)) + _etiqueta(x, y + 116, t)

def _alambre(x, y, t):
    return ('<path d="M%d %d q30 -40 60 0 t60 0 t60 0" stroke="#9aa1aa" stroke-width="5" fill="none"/><rect x="%d" y="%d" width="200" height="16" rx="4" fill="#a67c52"/>'
            % (x - 90, y + 30, x - 100, y + 34)) + _etiqueta(x, y + 76, t)

def _svg(body, h, label):
    return '<figure class="conexion"><svg viewBox="0 0 %d %d" role="img" aria-label="%s" font-family="system-ui,sans-serif">%s</svg><figcaption>%s</figcaption></figure>' % (
        W, h, e(label), body, e(label))

# ------------------------------------------------------------------ esquemas
def piano():
    b = _placa()
    b += _cable('P0', 90, 300, 'rojo') + _cable('P1', 230, 300, 'amarillo') + _cable('P2', 370, 300, 'verde') + _cable('GND', 540, 300, 'negro')
    b += _fruta(90, 300, '#d9412e', 'Do · P0') + _fruta(230, 300, '#f0a030', 'Mi · P1') + _fruta(370, 300, '#8cc63f', 'Sol · P2') + _mano(540, 300, 'GND: sujétalo')
    return _svg(b, 400, 'Piano de frutas: cada fruta a un pin (P0, P1, P2) y la mano sujetando el cable de GND')

def semaforo():
    b = _placa()
    b += _cable('P0', 120, 290, 'rojo') + _cable('P1', 260, 290, 'amarillo') + _cable('P2', 400, 290, 'verde')
    for x, c, t in ((120, 'rojo', 'rojo · P0'), (260, 'amarillo', 'amarillo · P1'), (400, 'verde', 'verde · P2')):
        b += _led(x, 290, c, t)
    b += '<path d="M115 418 H560" stroke="#2b2f36" stroke-width="5"/>'
    b += _cable('GND', 560, 418, 'negro', dy=60)
    b += '<text x="470" y="440" font-size="12" fill="#5b6675">patas cortas a GND</text>'
    return _svg(b, 470, 'Semáforo: cada LED con su resistencia de 220 Ω a P0, P1 y P2; las patas cortas juntas a GND')

def pulso():
    b = _placa() + _cable('P0', 160, 290, 'naranja') + _cable('GND', 470, 300, 'negro')
    b += _anilla(160, 290, 'anilla · P0') + _alambre(470, 300, 'camino de alambre · GND')
    return _svg(b, 420, 'Juego del pulso: la anilla a P0 y el camino de alambre a GND')

def alarma():
    b = _placa() + _cable('P1', 220, 300, 'azul') + _cable('GND', 420, 300, 'negro')
    b += _aluminio(220, 300, 150, 'aluminio en la puerta · P1') + _aluminio(420, 300, 150, 'aluminio en el marco · GND')
    b += '<text x="320" y="392" text-anchor="middle" font-size="13" fill="#5b6675">con la puerta cerrada, las dos láminas se tocan</text>'
    return _svg(b, 410, 'Alarma de puerta: una lámina de aluminio a P1 y otra a GND')

def humedad():
    b = _placa() + _cable('3V', 290, 296, 'rojo') + _cable('P1', 350, 296, 'azul')
    b += _clavos(320, 300, 'dos clavos en la tierra: 3V y P1')
    return _svg(b, 440, 'Humedad de la tierra: un clavo a 3V y el otro a P1')

def potenciometro():
    b = _placa() + _cable('3V', 290, 304, 'rojo') + _cable('P2', 320, 304, 'azul') + _cable('GND', 350, 304, 'negro')
    b += _potenciometro(320, 320, 'potenciómetro: 3V · P2 · GND')
    return _svg(b, 420, 'Potenciómetro: patas de los extremos a 3V y GND, pata central a P2')

def servo():
    b = _placa() + _cable('P0', 300, 300, 'naranja') + _cable('3V', 320, 300, 'rojo') + _cable('GND', 340, 300, 'marron')
    b += '<rect x="290" y="300" width="60" height="16" rx="3" fill="#2b2f36"/>'
    b += _servo(320, 340, 'servo: naranja P0 · rojo 3V · marrón GND')
    return _svg(b, 450, 'Microservo: señal (naranja) a P0, rojo a 3V y marrón a GND')

def invernadero():
    b = _placa() + _cable('3V', 180, 296, 'rojo') + _cable('P1', 240, 296, 'azul')
    b += _clavos(210, 300, 'humedad: 3V y P1')
    b += _cable('P0', 450, 330, 'naranja') + _cable('3V', 470, 330, 'rojo') + _cable('GND', 490, 330, 'marron')
    b += _servo(470, 360, 'servo de la ventana: P0, 3V y GND')
    return _svg(b, 470, 'Invernadero: clavos de humedad a 3V y P1; servo de la ventana a P0, 3V y GND')


def _led_r(x, y, color, t):
    """LED con resistencia en serie: cable → resistencia → pata larga (+); pata corta (−) → línea de GND."""
    c = COL[color]
    s = '<rect x="%d" y="%d" width="14" height="34" rx="5" fill="#d9c39a" stroke="#8a6d3b"/>' % (x - 37, y - 10)
    s += '<path d="M%d %d h14 M%d %d h14 M%d %d h14" stroke="#c0392b" stroke-width="3"/>' % (x - 37, y - 2, x - 37, y + 5, x - 37, y + 12)
    s += '<text x="%d" y="%d" text-anchor="end" font-size="11" fill="#5b6675">220 Ω</text>' % (x - 42, y + 10)
    s += '<path d="M%d %d V%d H%d V%d" stroke="#9aa1aa" stroke-width="3" fill="none"/>' % (x - 30, y + 24, y + 66, x - 5, y + 30)   # pata larga
    s += '<path d="M%d %d V%d" stroke="#9aa1aa" stroke-width="3"/>' % (x + 5, y + 30, y + 74)                                   # pata corta
    s += '<path d="M%d %d v-18 a12 12 0 0 1 24 0 v18z" fill="%s"/><rect x="%d" y="%d" width="28" height="5" rx="1" fill="%s"/>' % (x - 12, y + 30, c, x - 14, y + 28, c)
    s += '<text x="%d" y="%d" font-size="11" fill="#5b6675">+</text><text x="%d" y="%d" font-size="11" fill="#5b6675">−</text>' % (x - 18, y + 60, x + 9, y + 60)
    return s + _etiqueta(x - 12, y + 100, t)

def semaforo():
    b = _placa()
    for ring, x, c, t in (('P0', 130, 'rojo', 'rojo · P0'), ('P1', 270, 'amarillo', 'amarillo · P1'), ('P2', 410, 'verde', 'verde · P2')):
        b += _cable(ring, x - 30, 276, c) + _led_r(x, 290, c, t)
    b += '<path d="M135 364 H560" stroke="#2b2f36" stroke-width="5"/><circle cx="135" cy="364" r="4" fill="#2b2f36"/>'
    b += _cable('GND', 560, 364, 'negro')
    b += '<text x="470" y="384" font-size="12" fill="#5b6675">patas cortas (−) a GND</text>'
    return _svg(b, 410, 'Semáforo: cada LED con una resistencia de 220 Ω entre el pin y su pata larga (+); las patas cortas (−) juntas a GND')


def _pila(x, y, t):
    """Pila AA tumbada: + a la izquierda, − a la derecha."""
    s = ('<rect x="%d" y="%d" width="150" height="46" rx="8" fill="#2b2f36"/><rect x="%d" y="%d" width="46" height="46" rx="8" fill="#c99a2e"/>'
         '<rect x="%d" y="%d" width="8" height="20" rx="2" fill="#9aa1aa"/>' % (x - 75, y, x - 75, y, x - 83, y + 13))
    s += '<text x="%d" y="%d" font-size="20" font-weight="800" fill="#fff">+</text>' % (x - 60, y + 30)
    s += '<text x="%d" y="%d" font-size="20" font-weight="800" fill="#fff">−</text>' % (x + 52, y + 30)
    s += '<text x="%d" y="%d" text-anchor="middle" font-size="13" font-weight="700" fill="#fff">1,5 V</text>' % (x + 8, y + 28)
    return s + _etiqueta(x, y + 76, t)

def pila():
    b = _placa() + _cable('P1', 150, 300, 'rojo') + _cable('GND', 470, 330, 'negro')
    # resistencia de protección entre el cable de P1 y el polo +
    b += '<rect x="143" y="300" width="14" height="40" rx="5" fill="#d9c39a" stroke="#8a6d3b"/><path d="M143 309 h14 M143 317 h14 M143 325 h14" stroke="#8b4513" stroke-width="3"/>'
    b += '<text x="164" y="326" font-size="11" fill="#5b6675">1 kΩ</text><path d="M150 340 V352 H237" stroke="#9aa1aa" stroke-width="3" fill="none"/>'
    b += '<path d="M470 330 V352 H403" stroke="#9aa1aa" stroke-width="3" fill="none"/>'
    b += _pila(320, 330, 'pila de 1,5 V: + con la resistencia a P1, − a GND')
    return _svg(b, 440, 'Comprobador de pilas: el polo + de la pila a P1 a través de una resistencia de 1 kΩ y el polo − a GND')

def _objeto(x, y, t):
    """Objeto para probar (una moneda) con las dos pinzas tocándolo."""
    s = '<ellipse cx="%d" cy="%d" rx="70" ry="22" fill="#b88a2d"/><ellipse cx="%d" cy="%d" rx="70" ry="22" fill="#e0b34a" stroke="#9c7420" stroke-width="2"/>' % (x, y + 30, x, y + 24)
    s += '<ellipse cx="%d" cy="%d" rx="44" ry="12" fill="none" stroke="#b88a2d" stroke-width="2"/>' % (x, y + 24)
    return s + _etiqueta(x, y + 82, t)

def conduce():
    b = _placa() + _cable('P0', 270, 300, 'naranja') + _cable('GND', 370, 300, 'negro')
    b += _objeto(320, 300, 'el objeto que pruebas, tocado por las dos pinzas')
    b += '<text x="320" y="410" text-anchor="middle" font-size="13" fill="#5b6675">si conduce, une P0 con GND y la placa lo detecta</text>'
    return _svg(b, 430, '¿Conduce la electricidad?: una pinza de P0 y otra de GND tocando el objeto, sin que se toquen entre ellas')
