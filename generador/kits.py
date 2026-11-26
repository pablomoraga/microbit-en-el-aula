# -*- coding: utf-8 -*-
"""Anatomía de los kits (dibujos propios). Solo se señalan elementos y pines que aparecen
en la documentación oficial del fabricante o en el código de su extensión oficial."""
import html
from placa import frente, _nested, SONRISA
e = html.escape
INK = '#15202b'

def _anat(body, W, H, partes, label, fuente):
    OX = 90                     # margen a cada lado para las etiquetas
    TW = W + 2 * OX
    s = '<svg viewBox="0 0 %d %d" role="img" aria-label="%s" font-family="system-ui,sans-serif"><g transform="translate(%d 0)">%s</g>' % (TW, H, e(label), OX, body)
    for t, sub, (px, py), side, ly in partes:
        px += OX
        lx = 240 if side == 'L' else TW - 240
        s += '<path d="M%.0f %.0f L%d %d H%d" stroke="%s" stroke-width="1.5" fill="none" stroke-dasharray="4 3"/>' % (px, py, lx + (-8 if side == 'L' else 8), ly, lx, INK)
        s += '<circle cx="%.0f" cy="%.0f" r="5" fill="#ff5a36" stroke="#fff" stroke-width="2"/>' % (px, py)
        anchor, tx = ('end', lx - 6) if side == 'L' else ('start', lx + 6)
        s += '<text x="%d" y="%d" text-anchor="%s" font-size="15" font-weight="800" fill="%s">%s</text>' % (tx, ly + 1, anchor, INK, e(t))
        if sub:
            s += '<text x="%d" y="%d" text-anchor="%s" font-size="12" fill="#5b6675">%s</text>' % (tx, ly + 17, anchor, e(sub))
    s += '</svg>'
    return '<figure class="anat-fig kit">%s<figcaption>%s · Fuente: %s</figcaption></figure>' % (s, e(label), fuente)

def _rueda(x, y, w=26, h=56):
    return '<rect x="%d" y="%d" width="%d" height="%d" rx="8" fill="#2b2f36"/><path d="M%d %d h%d M%d %d h%d M%d %d h%d" stroke="#4a5059" stroke-width="3"/>' % (
        x, y, w, h, x + 4, y + 12, w - 8, x + 4, y + 28, w - 8, x + 4, y + 44, w - 8)

def _mb(x, y, w):
    return _nested(frente(callouts=False, lit=SONRISA, uid='k%d' % x), x, y, w, w * 450 / 540.0)

WIKI_EF = '<a href="%s" target="_blank" rel="noopener">wiki de ELECFREAKS</a>'
WIKI_DF = '<a href="%s" target="_blank" rel="noopener">wiki de DFRobot</a>'

def cutebot():
    W, H = 760, 440
    b = ''
    # chasis (vista desde arriba, el frente arriba)
    b += '<path d="M260 60 Q380 20 500 60 L520 360 Q380 400 240 360 Z" fill="#2e78d6"/>'
    b += _rueda(212, 250) + _rueda(522, 250)
    b += '<rect x="330" y="40" width="100" height="34" rx="6" fill="#3d434c"/><circle cx="356" cy="57" r="12" fill="#c9ced6"/><circle cx="404" cy="57" r="12" fill="#c9ced6"/>'
    b += '<circle cx="282" cy="92" r="10" fill="#fff" stroke="#ffcc00" stroke-width="4"/><circle cx="478" cy="92" r="10" fill="#fff" stroke="#ffcc00" stroke-width="4"/>'
    b += _mb(318, 100, 124)
    b += '<rect x="300" y="215" width="160" height="96" rx="8" fill="#20252c"/><rect x="310" y="225" width="140" height="22" rx="10" fill="#c79a3a"/><rect x="310" y="252" width="140" height="22" rx="10" fill="#c79a3a"/><rect x="310" y="279" width="140" height="22" rx="10" fill="#c79a3a"/>'
    b += '<rect x="360" y="352" width="40" height="16" rx="3" fill="#20252c"/><circle cx="420" cy="360" r="6" fill="#2fb44a"/>'
    partes = [
        ('Ultrasonidos HC-SR04', 'mide distancias de 2 a 400 cm', (380, 57), 'L', 40),
        ('Faros RGB', 'dos, uno a cada lado del frente', (282, 92), 'L', 110),
        ('Ruedas motrices', 'micromotores de 300 RPM', (225, 280), 'L', 290),
        ('Sensores de línea (debajo)', 'P13 izquierdo · P14 derecho', (330, 175), 'L', 200),
        ('micro:bit', 'se inserta en la ranura', (380, 150), 'R', 150),
        ('Portapilas 3 × AA', 'con puertos I2C, servo S1-S2, P1 y P2', (450, 262), 'R', 245),
        ('Receptor de infrarrojos', 'en la parte trasera · P16', (380, 360), 'R', 340),
        ('Interruptor y LED', 'encendido y apagado', (420, 360), 'R', 385),
        ('LED de colores (debajo)', 'dos, a P15', (500, 320), 'R', 300),
    ]
    return _anat(b, W, H, partes, 'Anatomía de Cutebot (vista desde arriba, frente arriba)',
                 WIKI_EF % 'https://wiki.elecfreaks.com/en/microbit/microbit-smart-car/microbit-smart-cutebot/')

def maqueen_lite():
    W, H = 760, 420
    b = '<rect x="262" y="60" width="236" height="300" rx="60" fill="#c0392b"/>'
    b += _rueda(232, 210) + _rueda(502, 210)
    b += '<rect x="330" y="44" width="100" height="34" rx="6" fill="#3d434c"/><circle cx="356" cy="61" r="12" fill="#c9ced6"/><circle cx="404" cy="61" r="12" fill="#c9ced6"/>'
    b += '<circle cx="300" cy="96" r="9" fill="#fff" stroke="#e74c3c" stroke-width="4"/><circle cx="460" cy="96" r="9" fill="#fff" stroke="#e74c3c" stroke-width="4"/>'
    b += _mb(318, 120, 124)
    b += '<rect x="300" y="255" width="44" height="16" rx="3" fill="#2b2f36"/><rect x="358" y="255" width="44" height="16" rx="3" fill="#2b2f36"/><rect x="416" y="255" width="44" height="16" rx="3" fill="#2b2f36"/>'
    partes = [
        ('Ultrasonidos', 'TRIG P1 · ECHO P2 (extensión maqueen)', (380, 61), 'L', 44),
        ('Luces LED', 'izquierda P8 · derecha P12', (300, 96), 'L', 110),
        ('Motores M1 y M2', 'izquierdo y derecho', (245, 240), 'L', 240),
        ('Sensores de línea (debajo)', 'P13 y P14 · dan 0 sobre negro', (345, 330), 'L', 330),
        ('micro:bit', 'se inserta en la ranura', (380, 170), 'R', 170),
        ('Puertos Gravity', 'P0, P1 y P2', (380, 263), 'R', 263),
    ]
    return _anat(b, W, H, partes, 'Anatomía de Maqueen Lite (vista desde arriba, frente arriba)',
                 WIKI_DF % 'https://wiki.dfrobot.com/rob0148-en/' + ' y extensión oficial pxt-maqueen')

def maqueen_plus():
    W, H = 760, 420
    b = '<rect x="250" y="70" width="260" height="290" rx="40" fill="#2b2f36"/><rect x="262" y="82" width="236" height="266" rx="32" fill="#3d434c"/>'
    b += _rueda(220, 210) + _rueda(514, 210)
    b += '<rect x="330" y="50" width="100" height="34" rx="6" fill="#20252c"/><circle cx="356" cy="67" r="12" fill="#c9ced6"/><circle cx="404" cy="67" r="12" fill="#c9ced6"/>'
    b += _mb(318, 120, 124)
    for i in range(5):
        b += '<rect x="%d" y="320" width="22" height="10" rx="3" fill="#ffcc00"/>' % (318 + i * 26)
    b += '<circle cx="470" cy="300" r="8" fill="#e0a83a" stroke="#fff" stroke-width="2"/>'
    partes = [
        ('Ultrasonidos', 'TRIG P13 · ECHO P14', (380, 67), 'L', 50),
        ('Motores', 'izquierdo y derecho', (233, 240), 'L', 240),
        ('5 sensores de línea (debajo)', 'L2 · L1 · M · R1 · R2 · dan 1 sobre negro', (330, 325), 'L', 330),
        ('micro:bit', 'se inserta en la ranura', (380, 170), 'R', 170),
        ('Botón de calibración', 'para los sensores de línea', (470, 300), 'R', 300),
    ]
    return _anat(b, W, H, partes, 'Anatomía de Maqueen Plus V2 (vista desde arriba, frente arriba)',
                 WIKI_DF % 'https://wiki.dfrobot.com/mbt0021-en/' + ' y extensión oficial pxt-DFRobot_MaqueenPlus_v20')

def wonder_moto():
    W, H = 760, 360
    b = '<rect x="290" y="110" width="180" height="130" rx="10" fill="#f2f2f2" stroke="#9aa1aa" stroke-width="2"/>'
    b += '<rect x="300" y="120" width="160" height="110" rx="8" fill="#2e78d6"/>' + _mb(330, 128, 100)
    b += '<circle cx="230" cy="250" r="56" fill="#2b2f36"/><circle cx="230" cy="250" r="22" fill="#9aa1aa"/>'
    b += '<circle cx="530" cy="250" r="56" fill="#2b2f36"/><circle cx="530" cy="250" r="22" fill="#9aa1aa"/>'
    b += '<rect x="246" y="190" width="44" height="34" rx="5" fill="#8a8f97"/><rect x="470" y="190" width="44" height="34" rx="5" fill="#8a8f97"/>'
    b += '<path d="M268 190 C 280 160, 300 150, 320 150" stroke="#e2a400" stroke-width="4" fill="none"/><path d="M492 190 C 480 160, 460 150, 440 150" stroke="#e2a400" stroke-width="4" fill="none"/>'
    partes = [
        ('Motor 1', 'conectado a M1', (268, 207), 'L', 120),
        ('Motor 2', 'conectado a M2', (492, 207), 'R', 120),
        ('Placa WuKong', 'con la micro:bit insertada', (380, 225), 'R', 300),
        ('Piezas compatibles con LEGO', 'para montar el modelo', (230, 300), 'L', 300),
    ]
    return _anat(b, W, H, partes, 'Wonder Building Kit · caso «The Motorcycle» (esquema)',
                 WIKI_EF % 'https://wiki.elecfreaks.com/en/microbit/building-blocks/wonder-building-kit/')

def smart_agri():
    W, H = 760, 420
    b = '<rect x="230" y="90" width="300" height="250" rx="10" fill="#e4f3ef" stroke="#0f8a72" stroke-width="2"/><path d="M230 90 L380 30 L530 90" fill="#cfeee4" stroke="#0f8a72" stroke-width="2"/>'
    b += '<path d="M270 300 h90 l-12 40 h-66z" fill="#8a5a33"/><path d="M315 300 c-10 -30 -4 -60 20 -70 c6 24 2 50 -20 70z M315 300 c6 -26 26 -40 46 -36 c-6 22 -24 34 -46 36z" fill="#2e9d4f"/>'
    b += '<rect x="322" y="292" width="6" height="40" fill="#9aa1aa"/><rect x="336" y="292" width="6" height="40" fill="#9aa1aa"/>'
    b += '<rect x="420" y="230" width="80" height="100" rx="6" fill="#bfe3ff" stroke="#2e78d6" stroke-width="2"/><rect x="420" y="280" width="80" height="50" fill="#6fb6f0"/><rect x="452" y="240" width="16" height="80" fill="#e2a400"/>'
    b += '<rect x="390" y="150" width="50" height="30" rx="4" fill="#2e78d6"/><path d="M440 165 h40" stroke="#f2f2f2" stroke-width="8" stroke-linecap="round"/>'
    b += '<rect x="560" y="140" width="130" height="110" rx="8" fill="#20252c"/>' + _mb(575, 150, 100)
    partes = [
        ('Sensor de humedad del suelo', 'puerto P1 de la IoT:bit', (332, 300), 'L', 300),
        ('Sensor de nivel de agua', 'puerto P2', (460, 270), 'L', 380),
        ('Servo (válvula)', 'puerto P9', (415, 165), 'L', 150),
        ('IoT:bit con la micro:bit', 'placa de expansión del kit', (625, 250), 'R', 380),
    ]
    return _anat(b, W, H, partes, 'Smart Agriculture Kit · caso 1 «Auto Irrigation in Farmlands» (esquema)',
                 WIKI_EF % 'https://wiki.elecfreaks.com/en/microbit/wisdom-life/microbit-smart-agriculture-kit/')
