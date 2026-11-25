# -*- coding: utf-8 -*-
"""Ilustraciones propias de la micro:bit V2 (esquemas simplificados, no a escala)."""

BOARD = '#1f2a37'
GOLD = '#d9a93b'

def _edge(x0, y0, w):
    """Conector de borde con 5 anillos grandes (0, 1, 2, 3V, GND) y pines pequeños."""
    out = ''
    # pines finos
    for i in range(60):
        x = x0 + 8 + i * (w - 16) / 59.0
        out += '<rect x="%.1f" y="%d" width="3" height="34" fill="%s" opacity=".9"/>' % (x, y0 + 12, GOLD)
    rings = [('0', 0.10), ('1', 0.30), ('2', 0.50), ('3V', 0.70), ('GND', 0.90)]
    for lab, f in rings:
        cx = x0 + w * f
        out += '<rect x="%.1f" y="%d" width="46" height="46" rx="6" fill="%s"/>' % (cx - 23, y0 + 2, GOLD)
        out += '<circle cx="%.1f" cy="%d" r="11" fill="#fff"/>' % (cx, y0 + 20)
        out += '<text x="%.1f" y="%d" text-anchor="middle" font-size="12" font-weight="700" fill="%s">%s</text>' % (cx, y0 + 43, BOARD, lab)
    return out

def _call(n, x, y):
    return ('<g class="pt"><circle cx="%d" cy="%d" r="13" fill="#ff5a36" stroke="#fff" stroke-width="2.5"/>'
            '<text x="%d" y="%d" text-anchor="middle" font-size="13" font-weight="800" fill="#fff">%d</text></g>' % (x, y, x, y + 4.5, n))

CORAZON = {(0, 1), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (4, 2)}
SONRISA = {(1, 1), (1, 3), (3, 0), (3, 4), (4, 1), (4, 2), (4, 3)}

def _defs(u):
    return ('<defs>'
            '<linearGradient id="pcb%s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2b2f35"/><stop offset="1" stop-color="#16191d"/></linearGradient>'
            '<linearGradient id="au%s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f3d27a"/><stop offset=".55" stop-color="#d4a437"/><stop offset="1" stop-color="#a9791c"/></linearGradient>'
            '<radialGradient id="bt%s" cx=".4" cy=".35" r=".7"><stop offset="0" stop-color="#4a4f57"/><stop offset="1" stop-color="#121417"/></radialGradient>'
            '<linearGradient id="mk%s" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f4f5f7"/><stop offset="1" stop-color="#b9bec6"/></linearGradient>'
            '<filter id="gl%s" x="-60%%" y="-60%%" width="220%%" height="220%%"><feGaussianBlur stdDeviation="3.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
            '<filter id="sh%s" x="-10%%" y="-10%%" width="120%%" height="130%%"><feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#000" flood-opacity=".28"/></filter>'
            '</defs>') % ((u,) * 6)

def frente(callouts=True, lit=SONRISA, uid='f'):
    """Anverso de la micro:bit V2 con proporciones reales (51,6 × 42 mm)."""
    u = uid
    W, H = 540, 450
    s = ('<svg class="placa-svg" viewBox="0 0 %d %d" role="img" aria-label="Anverso de la micro:bit V2%s" font-family="system-ui,sans-serif">'
         % (W, H, ' con sus partes numeradas' if callouts else ''))
    s += _defs(u)
    x0, y0, bw, bh = 20, 18, 500, 407
    ey = y0 + bh - 78          # comienzo del conector
    # contorno: esquinas superiores redondeadas y muescas en el borde inferior (V2)
    notch = ''
    xs = [x0 + bw * f for f in (0.2, 0.4, 0.6, 0.8)]
    d = 'M%d %d h%d a22 22 0 0 1 22 22 V%d' % (x0 + 22, y0, bw - 44, y0 + bh)
    for xn in reversed(xs):
        d += ' H%.1f v-9 h-10 v9' % (xn + 5)
    d += ' H%d V%d a22 22 0 0 1 22 -22z' % (x0, y0 + 22)
    s += '<path d="%s" fill="url(#pcb%s)" filter="url(#sh%s)"/>' % (d, u, u)
    # pistas del circuito (decorativas)
    s += '<g stroke="#3a4049" stroke-width="2" fill="none" opacity=".75">'
    s += '<path d="M60 120 h60 l20 20 v70"/><path d="M480 120 h-60 l-20 20 v70"/><path d="M150 300 h240"/><path d="M110 260 v40 h40"/><path d="M430 260 v40 h-40"/></g>'
    # logotipo táctil
    lx, ly = x0 + bw / 2, y0 + 50
    s += '<rect x="%.1f" y="%.1f" width="74" height="40" rx="20" fill="none" stroke="url(#au%s)" stroke-width="7.5"/>' % (lx - 37, ly - 20, u)
    s += '<circle cx="%.1f" cy="%.1f" r="5.5" fill="url(#au%s)"/><circle cx="%.1f" cy="%.1f" r="5.5" fill="url(#au%s)"/>' % (lx - 14, ly, u, lx + 14, ly, u)
    # orificio del micrófono y LED del micrófono
    s += '<circle cx="%.1f" cy="%.1f" r="4" fill="#050608" stroke="#7d838c" stroke-width="1.4"/>' % (lx + 72, ly)
    s += '<rect x="%.1f" y="%.1f" width="9" height="6" rx="1.5" fill="#e9ecef"/>' % (lx + 84, ly - 3)
    # botones A y B
    by = y0 + 190
    for bx, lab in ((x0 + 62, 'A'), (x0 + bw - 62, 'B')):
        s += '<rect x="%.1f" y="%.1f" width="58" height="58" rx="7" fill="url(#mk%s)" stroke="#8b919a"/>' % (bx - 29, by - 29, u)
        s += '<circle cx="%.1f" cy="%.1f" r="18" fill="url(#bt%s)"/>' % (bx, by, u)
        s += '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="20" font-weight="800" fill="#f2f2f2">%s</text>' % (bx, by + 58, lab)
    # matriz 5 × 5
    mx, my, step = x0 + bw / 2 - 50, y0 + 112, 25
    s += '<g>'
    for r in range(5):
        for c in range(5):
            cx, cy = mx + c * step, my + r * 33
            on = (r, c) in lit
            s += '<rect x="%.1f" y="%.1f" width="8" height="14" rx="1.5" fill="%s"%s/>' % (
                cx - 4, cy - 7, '#ff4632' if on else '#3a2a2a', (' filter="url(#gl%s)"' % u) if on else '')
    s += '</g>'
    # conector de borde: dedos finos y 5 anillos
    s += '<rect x="%d" y="%d" width="%d" height="2" fill="#3a4049"/>' % (x0 + 10, ey - 4, bw - 20)
    for i in range(56):
        fx = x0 + 14 + i * (bw - 28) / 55.0
        s += '<rect x="%.1f" y="%d" width="3.4" height="62" rx="1" fill="url(#au%s)"/>' % (fx, ey + 12, u)
    for lab, f in (('0', 0.1), ('1', 0.3), ('2', 0.5), ('3V', 0.7), ('GND', 0.9)):
        cx = x0 + bw * f
        s += '<rect x="%.1f" y="%d" width="54" height="72" rx="7" fill="url(#au%s)"/>' % (cx - 27, ey + 4, u)
        s += '<circle cx="%.1f" cy="%d" r="14" fill="var(--hole,#eef1f5)" stroke="#9c7420" stroke-width="2"/>' % (cx, ey + 34)
        s += '<text x="%.1f" y="%d" text-anchor="middle" font-size="12" font-weight="800" fill="#f2f2f2">%s</text>' % (cx, ey - 10, lab)
    if callouts:
        s += ''.join(_call(n, x, y) for n, x, y in [(1, mx - 22, my - 22), (2, x0 + 30, by - 44), (3, x0 + bw - 30, by - 44),
                                                    (4, lx - 50, ly - 22), (5, lx + 78, ly - 24), (6, x0 + 30, ey + 12)])
        s += '<text x="%d" y="446" text-anchor="middle" font-size="13" fill="#5b6675">Anverso · esquema simplificado</text>' % (W // 2)
    return s + '</svg>'

def reves():
    W, H = 520, 430
    s = '<svg class="placa-svg" viewBox="0 0 %d %d" role="img" aria-label="Reverso de la micro:bit V2 con sus partes numeradas" font-family="system-ui,sans-serif">' % (W, H)
    s += ('<path d="M30 20 h460 a20 20 0 0 1 20 20 v330 h-14 l-6 10 h-12 l-6 -10 h-436 l-6 10 h-12 l-6 -10 h-12 v-330 a20 20 0 0 1 20 -20z" fill="%s"/>' % BOARD)
    # USB, botón de reinicio y conector de pilas en el borde superior
    s += '<rect x="214" y="20" width="62" height="32" rx="4" fill="#b9c0ca"/><rect x="226" y="30" width="38" height="12" rx="3" fill="#69717d"/>'
    s += '<rect x="292" y="26" width="32" height="32" rx="5" fill="#c9ced6"/><circle cx="308" cy="42" r="9" fill="#2b2f36"/>'
    s += '<rect x="346" y="20" width="56" height="40" rx="4" fill="#efe9dc"/><rect x="354" y="30" width="40" height="20" rx="3" fill="#d6cdb8"/>'
    # LED de alimentación (rojo) y LED de USB (amarillo)
    s += '<circle cx="196" cy="70" r="6" fill="#ff3b30"/><circle cx="196" cy="90" r="6" fill="#ffcc00"/>'
    # procesador, chip de interfaz, sensor de movimiento
    s += '<rect x="96" y="120" width="86" height="86" rx="6" fill="#0d1117" stroke="#3b4757"/><text x="139" y="168" text-anchor="middle" font-size="11" fill="#9aa6b5">nRF52833</text>'
    s += '<rect x="330" y="96" width="56" height="56" rx="5" fill="#0d1117" stroke="#3b4757"/><text x="358" y="128" text-anchor="middle" font-size="9" fill="#9aa6b5">interfaz</text>'
    s += '<rect x="112" y="238" width="44" height="34" rx="4" fill="#0d1117" stroke="#3b4757"/><text x="134" y="259" text-anchor="middle" font-size="9" fill="#9aa6b5">mov.</text>'
    # altavoz y micrófono
    s += '<rect x="230" y="150" width="70" height="70" rx="8" fill="#0d1117" stroke="#3b4757"/><circle cx="265" cy="185" r="22" fill="#262d36"/><circle cx="265" cy="185" r="6" fill="#0d1117"/>'
    s += '<rect x="410" y="78" width="26" height="20" rx="3" fill="#b9c0ca"/>'
    # antena
    s += '<path d="M392 230 h40 v-14 h16 v14 h14" fill="none" stroke="%s" stroke-width="3"/>' % GOLD
    s += _edge(30, 315, 460)
    s += ''.join(_call(n, x, y) for n, x, y in [(7, 139, 108), (8, 245, 14), (9, 308, 82), (10, 374, 14), (11, 178, 60), (12, 265, 138), (13, 423, 66),
                                              (14, 134, 226), (15, 455, 248), (16, 358, 84)])
    s += '<text x="260" y="425" text-anchor="middle" font-size="13" fill="#5b6675">Reverso · esquema simplificado, no a escala</text>'
    return s + '</svg>'

def pines():
    """Esquema del conector de borde con los pines más usados."""
    W, H = 760, 230
    s = '<svg class="placa-svg ancho" viewBox="0 0 %d %d" role="img" aria-label="Conector de borde de la micro:bit con los pines principales" font-family="system-ui,sans-serif">' % (W, H)
    s += '<rect x="10" y="10" width="740" height="120" rx="10" fill="%s"/>' % BOARD
    rings = [('P0', 0.10), ('P1', 0.30), ('P2', 0.50), ('3V', 0.70), ('GND', 0.90)]
    for i in range(60):
        x = 24 + i * 712 / 59.0
        s += '<rect x="%.1f" y="70" width="5" height="52" fill="%s"/>' % (x, GOLD)
    for lab, f in rings:
        cx = 10 + 740 * f
        s += '<rect x="%.1f" y="38" width="76" height="86" rx="8" fill="%s"/><circle cx="%.1f" cy="70" r="19" fill="#fff"/>' % (cx - 38, GOLD, cx)
        s += '<text x="%.1f" y="30" text-anchor="middle" font-size="17" font-weight="800" fill="#fff">%s</text>' % (cx, lab)
    notes = [(0.10, 'digital · analógico · táctil'), (0.30, 'digital · analógico · táctil'), (0.50, 'digital · analógico · táctil'),
             (0.70, 'alimentación 3 V'), (0.90, 'tierra (0 V)')]
    for f, t in notes:
        s += '<text x="%.1f" y="155" text-anchor="middle" font-size="13" fill="#1d2b3a">%s</text>' % (10 + 740 * f, t)
    s += '<text x="380" y="190" text-anchor="middle" font-size="13" fill="#5b6675">Entre los anillos hay pines pequeños (P3 a P20). Para usarlos hace falta una placa de expansión.</text>'
    s += '<text x="380" y="212" text-anchor="middle" font-size="13" fill="#5b6675">Algunos comparten función con la pantalla y los botones; P19 y P20 son el bus I²C.</text>'
    return s + '</svg>'

LEYENDA_FRENTE = [
    ('Pantalla de 25 LED (5 × 5)', 'Muestra números, letras, iconos y animaciones. Los LED también sirven para medir la luz ambiente.'),
    ('Botón A', 'Entrada. El programa puede reaccionar cuando se pulsa, se mantiene o se pulsa a la vez que B.'),
    ('Botón B', 'Igual que el A. Con dos botones ya se pueden hacer contadores, menús y juegos.'),
    ('Logotipo táctil', 'Sensor capacitivo: detecta cuándo lo tocas con el dedo. Funciona como un tercer botón.'),
    ('Orificio y LED del micrófono', 'Por el orificio entra el sonido hasta el micrófono. El LED se enciende cuando el micrófono está midiendo.'),
    ('Conector de borde', '25 contactos dorados. Los anillos grandes 0, 1 y 2 sirven para conectar cables de cocodrilo; 3V y GND dan alimentación.'),
]
LEYENDA_REVES = [
    ('Procesador nRF52833', 'El «cerebro»: ejecuta el programa. También integra la radio y el sensor de temperatura.'),
    ('Conector micro USB', 'Para cargar programas desde el ordenador y alimentar la placa.'),
    ('Botón de reinicio y encendido', 'Una pulsación reinicia el programa. Si lo mantienes pulsado, la placa entra en reposo; otra pulsación la despierta.'),
    ('Conector de pilas', 'Para el portapilas de dos pilas AAA. Así la micro:bit funciona sin ordenador.'),
    ('LED de alimentación y LED de USB', 'El rojo indica que la placa recibe energía. El amarillo parpadea cuando se comunica con el ordenador.'),
    ('Altavoz', 'Reproduce tonos, melodías y efectos de sonido sin necesidad de conectar nada.'),
    ('Micrófono', 'Mide el nivel de sonido y detecta sonidos fuertes, como una palmada.'),
    ('Acelerómetro y brújula', 'Un mismo chip detecta movimientos, inclinación y gestos (agitar, girar…) y el campo magnético.'),
    ('Antena', 'Para la radio entre micro:bits y para Bluetooth.'),
    ('Chip de interfaz USB', 'Gestiona la conexión USB: hace que la placa aparezca como una unidad llamada MICROBIT.'),
]


def _nested(svg, x, y, w, h):
    """Mete un SVG completo dentro de otro, en la posición y el tamaño indicados."""
    inner = svg[svg.index('>') + 1:svg.rindex('</svg>')]
    return '<svg x="%s" y="%s" width="%s" height="%s" viewBox="0 0 540 450">%s</svg>' % (x, y, w, h, inner)

def _clip(x, y, ang, color):
    """Pinza de cocodrilo: funda de color y mandíbulas metálicas."""
    return ('<g transform="translate(%s %s) rotate(%s)">'
            '<path d="M-9 0 L-13 46 Q0 54 13 46 L9 0 Z" fill="%s" stroke="rgba(0,0,0,.25)"/>'
            '<path d="M-6 -2 L-4 -30 L0 -34 L4 -30 L6 -2Z" fill="#c9ced6" stroke="#8b919a"/>'
            '<path d="M-4 -26 h8 M-4 -20 h8 M-4 -14 h8" stroke="#8b919a" stroke-width="1.4"/>'
            '<path d="M-7 16 h14 M-8 24 h16 M-9 32 h18" stroke="rgba(255,255,255,.25)" stroke-width="2"/></g>') % (x, y, ang, color)

def _led(x, y, color, glow=False):
    s = '<g transform="translate(%s %s)">' % (x, y)
    s += '<path d="M-3 18 v34 M3 18 v26" stroke="#9aa1aa" stroke-width="2.4" stroke-linecap="round"/>'
    if glow: s += '<circle cx="0" cy="-2" r="22" fill="%s" opacity=".22"/>' % color
    s += '<path d="M-11 18 v-20 a11 11 0 0 1 22 0 v20 z" fill="%s" opacity=".92"/><rect x="-13" y="14" width="26" height="5" rx="1.5" fill="%s"/>' % (color, color)
    s += '<path d="M-6 -4 a6 6 0 0 1 5 -6" stroke="#fff" stroke-width="2.2" fill="none" opacity=".7" stroke-linecap="round"/></g>'
    return s

def _boton(x, y, cap):
    return ('<g transform="translate(%s %s)"><path d="M-14 14 l-5 10 M14 14 l5 10 M-14 -14 l-5 -10 M14 -14 l5 -10" stroke="#9aa1aa" stroke-width="2.4"/>'
            '<rect x="-17" y="-17" width="34" height="34" rx="4" fill="#2b2f36"/><rect x="-13" y="-13" width="26" height="26" rx="3" fill="#3d434c"/>'
            '<circle r="9.5" fill="%s"/><circle r="9.5" fill="none" stroke="rgba(0,0,0,.25)" stroke-width="2"/></g>') % (x, y, cap)

def hero():
    """Portada: la placa con cables de cocodrilo detrás y componentes debajo."""
    W, H = 640, 600
    s = '<svg class="placa-svg" viewBox="0 0 %d %d" role="img" aria-label="Ilustración de una micro:bit V2 conectada con cables de cocodrilo a LED y pulsadores">' % (W, H)
    # cables (detrás de la placa): salen de los anillos y bajan hacia los componentes
    bx, by, bw, bh = 70, 30, 500, 417
    sc = bw / 540.0
    ring = lambda f: (bx + (20 + 500 * f) * sc, by + 381 * sc)
    cables = [(0.1, '#e53935', (120, 520), -18), (0.3, '#fbc02d', (250, 540), -6), (0.5, '#43a047', (390, 540), 8), (0.9, '#263238', (520, 520), 20)]
    for f, col, (ex, ey), ang in cables:
        rx, ry = ring(f)
        s += '<path d="M%.1f %.1f C %.1f %.1f, %.1f %.1f, %d %d" stroke="%s" stroke-width="7" fill="none" stroke-linecap="round"/>' % (
            rx, ry - 160, rx - 120 * (0.5 - f), ry + 40, ex, ey - 120, ex, ey - 46, col)
    # cables que asoman por detrás, arriba
    s += '<path d="M40 110 C 0 40, 120 0, 190 40" stroke="#1e88e5" stroke-width="7" fill="none" stroke-linecap="round"/>'
    s += '<path d="M600 150 C 640 60, 520 10, 460 46" stroke="#e53935" stroke-width="7" fill="none" stroke-linecap="round"/>'
    s += _clip(40, 110, 200, '#1e88e5') + _clip(600, 150, 160, '#e53935')
    # la placa
    s += _nested(frente(callouts=False, lit=CORAZON, uid='hero'), bx, by, bw, bh)
    # pinzas sobre los anillos
    for f, col, _, ang in cables:
        rx, ry = ring(f)
        s += _clip(rx, ry + 30, 180 + ang * .3, col)
    # componentes debajo
    s += _led(120, 520, '#ff3b30', True) + _boton(250, 548, '#fbc02d') + _boton(390, 548, '#43a047') + _led(520, 520, '#40c4ff', True)
    return s + '</svg>'

def anatomia():
    """Anatomía de la placa: la micro:bit en el centro y sus partes señaladas con líneas."""
    W, H = 900, 500
    bx, by, bw, bh = 230, 40, 440, 367
    k = bw / 540.0
    P = lambda x, y: (bx + x * k, by + y * k)
    s = '<svg class="placa-svg anat" viewBox="0 0 %d %d" role="img" aria-label="Anatomía de la micro:bit V2" font-family="system-ui,sans-serif">' % (W, H)
    s += _nested(frente(callouts=False, lit=SONRISA, uid='an'), bx, by, bw, bh)
    partes = [  # (texto, subtítulo, punto en la placa, lado, y de la etiqueta)
        ('Logotipo táctil', 'un botón más, sin piezas', (270, 68), 'L', 60),
        ('Botón A', 'entrada', (82, 208), 'L', 190),
        ('Pines 0, 1 y 2', 'cables de cocodrilo', (70, 381), 'L', 400),
        ('Micrófono y su LED', 'mide el sonido', (342, 68), 'R', 60),
        ('Pantalla de 25 LED', 'también mide la luz', (320, 200), 'R', 150),
        ('Botón B', 'entrada', (458, 208), 'R', 250),
        ('3V y GND', 'alimentación', (420, 381), 'R', 400),
    ]
    for t, sub, (px, py), side, ly in partes:
        x, y = P(px, py)
        lx = 210 if side == 'L' else 690
        s += '<path d="M%.1f %.1f L%d %d H%d" stroke="#15202b" stroke-width="1.6" fill="none" stroke-dasharray="4 3"/>' % (x, y, lx + (-10 if side == 'L' else 10), ly, lx)
        s += '<circle cx="%.1f" cy="%.1f" r="5" fill="#ff5a36" stroke="#fff" stroke-width="2"/>' % (x, y)
        anchor, tx = ('end', lx - 8) if side == 'L' else ('start', lx + 8)
        s += '<text x="%d" y="%d" text-anchor="%s" font-size="17" font-weight="800" fill="#15202b">%s</text>' % (tx, ly + 2, anchor, t)
        s += '<text x="%d" y="%d" text-anchor="%s" font-size="13" fill="#5b6675">%s</text>' % (tx, ly + 20, anchor, sub)
    s += '<text x="450" y="490" text-anchor="middle" font-size="13" fill="#5b6675">micro:bit V2 · anverso</text>'
    return s + '</svg>'


def hero():
    """Portada (estilo vintage): la placa en perspectiva sobre una mesa, dos cocodrilos a la derecha
    y LED y pulsadores sueltos delante, a la izquierda."""
    import math
    W, H = 680, 560
    ink = '#3b2a20'
    s = ('<svg class="placa-svg hero-vintage" viewBox="0 0 %d %d" role="img" aria-label="Ilustración de estilo vintage: una micro:bit sobre una mesa '
         'con dos cables de cocodrilo y varios LED y pulsadores">' % (W, H))
    s += ('<defs>'
          '<filter id="vint" x="-5%" y="-5%" width="110%" height="110%">'
          '<feColorMatrix type="matrix" values=".85 .12 .03 0 .04  .08 .80 .08 0 .03  .06 .10 .62 0 .02  0 0 0 1 0" result="c"/>'
          '<feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="4" result="n"/>'
          '<feColorMatrix in="n" type="matrix" values="0 0 0 0 .23  0 0 0 0 .16  0 0 0 0 .1  0 0 0 .16 0" result="g"/>'
          '<feComposite in="g" in2="c" operator="in" result="g2"/><feMerge><feMergeNode in="c"/><feMergeNode in="g2"/></feMerge></filter>'
          '<filter id="somb" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="9"/></filter>'
          '<pattern id="cuad" width="22" height="22" patternUnits="userSpaceOnUse"><path d="M22 0H0V22" fill="none" stroke="#c9b48c" stroke-width="1"/></pattern>'
          '</defs><g filter="url(#vint)">')
    # mesa: tapete de dibujo en perspectiva
    s += '<path d="M60 150 L640 110 L670 520 L20 545 Z" fill="#efe2c4" stroke="%s" stroke-width="2"/>' % ink
    s += '<path d="M60 150 L640 110 L670 520 L20 545 Z" fill="url(#cuad)" opacity=".7"/>'
    s += '<path d="M78 168 L622 130 L648 505 L40 528 Z" fill="none" stroke="#b5482e" stroke-width="1.5" stroke-dasharray="7 5" opacity=".7"/>'
    # transformación de la placa: girada y aplastada para simular que está tumbada
    bw = 380.0; k = bw / 540.0; ang = math.radians(-12); sy = .74; X, Y = 340, 250
    def T(x, y):
        px, py = (x - 270) * k, (y - 225) * k
        rx = px * math.cos(ang) - py * math.sin(ang); ry = px * math.sin(ang) + py * math.cos(ang)
        return X + rx, Y + ry * sy
    tr = 'translate(%d %d) scale(1 %.2f) rotate(%.1f) translate(%.1f %.1f)' % (X, Y, sy, math.degrees(ang), -bw / 2, -450 * k / 2)
    # sombra de la placa
    s += '<g transform="%s"><rect x="10" y="22" width="%.0f" height="%.0f" rx="18" fill="#5a4030" opacity=".45" filter="url(#somb)"/></g>' % (tr, bw, 450 * k)
    # cables (detrás de las pinzas): salen hacia la derecha
    for f, col, end in ((0.7, '#b5482e', (700, 210)), (0.9, '#2f2a26', (700, 330))):
        x, y = T(20 + 500 * f, 395)
        s += '<path d="M%.1f %.1f C %.1f %.1f, %.1f %.1f, %d %d" stroke="%s" stroke-width="8" fill="none" stroke-linecap="round"/>' % (
            x + 30, y + 22, x + 120, y + 70, end[0] - 120, end[1] + 40, end[0], end[1], col)
        s += '<path d="M%.1f %.1f C %.1f %.1f, %.1f %.1f, %d %d" stroke="#fff" stroke-opacity=".25" stroke-width="2" fill="none"/>' % (
            x + 30, y + 20, x + 120, y + 66, end[0] - 120, end[1] + 36, end[0], end[1])
    # la placa
    s += '<g transform="%s">%s</g>' % (tr, _nested(frente(callouts=False, lit=CORAZON, uid='hv'), 0, 0, bw, 450 * k))
    # pinzas de cocodrilo sobre 3V y GND
    for f, col in ((0.7, '#b5482e'), (0.9, '#2f2a26')):
        x, y = T(20 + 500 * f, 385)
        s += '<g transform="translate(%.1f %.1f) scale(1.45) translate(%.1f %.1f)">%s</g>' % (x + 12, y + 6, -(x + 12), -(y + 6), _clip(x + 12, y + 6, 238, col))
    # componentes sueltos delante, a la izquierda
    s += '<g stroke="%s" stroke-width="1.2">' % ink
    for cx, cy in ((110, 470), (205, 505), (300, 480), (165, 410), (60, 400)):
        s += '<ellipse cx="%d" cy="%d" rx="20" ry="6" fill="#5a4030" opacity=".25" stroke="none"/>' % (cx + 6, cy + 30)
    s += '</g>'
    s += '<g transform="rotate(-18 110 455)">%s</g>' % '<g transform="translate(110 455) scale(1.4) translate(-110 -455)">' + _led(110, 455, '#c8553d') + '</g>'
    s += '<g transform="rotate(64 205 500)">%s</g>' % '<g transform="translate(205 500) scale(1.4) translate(-205 -500)">' + _led(205, 500, '#e0a83a') + '</g>'
    s += '<g transform="rotate(10 60 385)">%s</g>' % '<g transform="translate(60 385) scale(1.4) translate(-60 -385)">' + _led(60, 385, '#3d8b87') + '</g>'
    s += '<g transform="rotate(14 300 482)">%s</g>' % '<g transform="translate(300 482) scale(1.4) translate(-300 -482)">' + _boton(300, 482, '#e0a83a') + '</g>'
    s += '<g transform="rotate(-22 165 412)">%s</g>' % '<g transform="translate(165 412) scale(1.4) translate(-165 -412)">' + _boton(165, 412, '#c8553d') + '</g>'
    # una resistencia
    s += ('<g transform="rotate(-30 330 410)"><path d="M290 410 H370" stroke="#9aa1aa" stroke-width="2.4"/>'
          '<rect x="312" y="403" width="36" height="14" rx="6" fill="#d9c39a" stroke="%s" stroke-width="1"/>'
          '<path d="M320 403v14M327 403v14M334 403v14M341 403v14" stroke-width="3" stroke="#b5482e"/></g>') % ink
    return s + '</g></svg>'
