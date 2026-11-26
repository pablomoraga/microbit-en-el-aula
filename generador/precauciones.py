# -*- coding: utf-8 -*-
"""Precauciones de uso: tarjetas con una ilustración propia y su explicación.
Los datos de pilas, alimentación y conector de borde proceden de tech.microbit.org (power supply y edge connector)
y del artículo «How do I power my micro:bit?» de support.microbit.org."""
import html
from placa import frente, _nested, _clip, _led, CORAZON
e = html.escape

V, R, INK, G = '#0f8a72', '#d64031', '#15202b', '#d9a93b'

def _svg(body, label):
    return '<svg class="ilus" viewBox="0 0 240 150" role="img" aria-label="%s" font-family="system-ui,sans-serif">%s</svg>' % (e(label), body)

def _placa(x, y, w, uid, lit=CORAZON):
    return _nested(frente(callouts=False, lit=lit, uid=uid), x, y, w, w * 450 / 540.0)

def _pila(x, y, nivel=1.0, ang=0):
    """Pila AAA tumbada (polo + a la derecha)."""
    s = '<g transform="translate(%s %s) rotate(%s)">' % (x, y, ang)
    s += '<rect x="0" y="0" width="86" height="26" rx="5" fill="#2b2f36"/><rect x="0" y="0" width="22" height="26" rx="5" fill="#c79a3a"/>'
    s += '<rect x="86" y="8" width="6" height="10" rx="2" fill="#9aa1aa"/>'
    s += '<rect x="30" y="7" width="48" height="12" rx="3" fill="#4a4f57"/><rect x="30" y="7" width="%d" height="12" rx="3" fill="%s"/>' % (48 * nivel, V if nivel > .5 else R)
    s += '<text x="80" y="-4" font-size="12" font-weight="800" fill="%s">+</text></g>' % INK
    return s

def _marca(ok, x=214, y=24):
    if ok:
        return '<circle cx="%d" cy="%d" r="16" fill="%s"/><path d="M%d %d l6 6 12 -13" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' % (x, y, V, x - 9, y, )
    return '<circle cx="%d" cy="%d" r="16" fill="%s"/><path d="M%d %d l12 12 M%d %d l-12 12" stroke="#fff" stroke-width="4" stroke-linecap="round"/>' % (x, y, R, x - 6, y - 6, x + 6, y - 6)

def _tachar(x, y, r=34):
    return '<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="6"/><path d="M%d %d L%d %d" stroke="%s" stroke-width="6"/>' % (
        x, y, r, R, x - r * .7, y - r * .7, x + r * .7, y + r * .7, R)

# ------------------------------------------------------------------ ilustraciones
def i_pilas():
    b = '<rect x="40" y="38" width="130" height="78" rx="8" fill="#20252c"/>' + _pila(52, 48) + _pila(52, 82)
    b += '<path d="M170 76 C 190 76, 190 110, 205 110" stroke="%s" stroke-width="4" fill="none"/><path d="M170 82 C 186 82, 186 116, 205 116" stroke="%s" stroke-width="4" fill="none"/>' % (R, INK)
    b += '<text x="105" y="134" text-anchor="middle" font-size="12" fill="#5b6675">2 × AAA alcalinas</text>'
    return _svg(b + _marca(True), 'Portapilas con dos pilas AAA alcalinas')

def i_mezclar():
    b = _pila(30, 46, 1.0) + _pila(30, 90, .2)
    b += '<text x="130" y="64" font-size="12" fill="%s" font-weight="700">nueva</text><text x="130" y="108" font-size="12" fill="%s" font-weight="700">gastada</text>' % (V, R)
    return _svg(b + _marca(False), 'Una pila nueva y una gastada juntas')

def i_enchufe():
    b = '<rect x="38" y="40" width="62" height="74" rx="10" fill="#eef1f5" stroke="%s" stroke-width="2"/><circle cx="58" cy="77" r="6" fill="%s"/><circle cx="80" cy="77" r="6" fill="%s"/>' % (INK, INK, INK)
    b += '<rect x="128" y="44" width="44" height="70" rx="8" fill="#2b2f36"/><rect x="136" y="54" width="28" height="14" rx="3" fill="#7ee0a4"/><text x="150" y="96" text-anchor="middle" font-size="11" fill="#fff">5V</text>'
    b += _tachar(69, 77) + _tachar(150, 79)
    return _svg(b + _marca(False), 'Enchufe de pared y batería externa tachados')

def i_usb_y_pilas():
    b = _placa(70, 30, 100, 'pr1')
    b += '<path d="M120 30 C 120 10, 60 10, 30 18" stroke="%s" stroke-width="5" fill="none" stroke-linecap="round"/><rect x="113" y="26" width="14" height="10" rx="2" fill="#b9c0ca"/>' % INK
    b += '<path d="M150 32 C 160 8, 200 10, 214 50" stroke="%s" stroke-width="3" fill="none"/><path d="M146 32 C 156 4, 206 4, 222 50" stroke="%s" stroke-width="3" fill="none"/>' % (R, INK)
    b += '<rect x="196" y="50" width="40" height="64" rx="6" fill="#20252c"/><rect x="202" y="58" width="28" height="22" rx="3" fill="#c79a3a"/><rect x="202" y="84" width="28" height="22" rx="3" fill="#c79a3a"/>'
    b += '<text x="30" y="40" font-size="11" fill="#5b6675">USB</text>'
    return _svg(b, 'micro:bit con cable USB y portapilas conectados a la vez')

def i_cocodrilo():
    b = '<rect x="10" y="40" width="220" height="70" rx="6" fill="#1f2a37"/>'
    for i in range(44):
        b += '<rect x="%.1f" y="82" width="2.2" height="28" fill="%s"/>' % (16 + i * 4.9, G)
    for cx, lab in ((44, '0'), (120, '1'), (196, '2')):
        b += '<rect x="%d" y="70" width="34" height="40" rx="5" fill="%s"/><circle cx="%d" cy="84" r="8" fill="#fff"/><text x="%d" y="104" text-anchor="middle" font-size="10" font-weight="700" fill="#1f2a37">%s</text>' % (cx - 17, G, cx, cx, lab)
    b += _clip(44, 92, 180, '#c0392b').replace('translate(44 92)', 'translate(44 84)')
    b += _clip(132, 84, 205, '#2b2f36')
    b += '<circle cx="139" cy="98" r="15" fill="none" stroke="%s" stroke-width="3"/>' % R
    b += '<text x="44" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="%s">recta</text><text x="160" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="%s">torcida</text>' % (V, R)
    return _svg(b, 'Pinza de cocodrilo recta en el anillo 0 y otra torcida tocando los pines de al lado')

def i_corto():
    b = '<rect x="10" y="50" width="220" height="60" rx="6" fill="#1f2a37"/>'
    for cx, lab in ((70, '3V'), (170, 'GND')):
        b += '<rect x="%d" y="66" width="44" height="44" rx="5" fill="%s"/><circle cx="%d" cy="82" r="9" fill="#fff"/><text x="%d" y="104" text-anchor="middle" font-size="10" font-weight="700" fill="#1f2a37">%s</text>' % (cx - 22, G, cx, cx, lab)
    b += '<path d="M70 82 C 90 10, 150 10, 170 82" stroke="%s" stroke-width="6" fill="none" stroke-linecap="round"/>' % R
    b += '<path d="M112 22 l-8 14 h10 l-8 14" stroke="#ffcc00" stroke-width="4" fill="none" stroke-linejoin="round"/>'
    return _svg(b + _marca(False), 'Cable que une 3V y GND directamente: cortocircuito')

def i_resistencia():
    b = '<path d="M20 100 H70" stroke="#c0392b" stroke-width="5" stroke-linecap="round"/>'
    b += '<path d="M70 100 H160" stroke="#a9adb3" stroke-width="3"/><rect x="92" y="90" width="46" height="20" rx="9" fill="#d9bd88"/>'
    for x, c in ((100, '#c0392b'), (108, '#c0392b'), (116, '#5b3a29'), (128, '#c8a24a')):
        b += '<rect x="%d" y="90" width="4" height="20" fill="%s"/>' % (x, c)
    b += _led(185, 52, '#e74c3c', True)
    b += '<path d="M182 104 V100 H160" stroke="#a9adb3" stroke-width="3" fill="none"/>'
    b += '<text x="115" y="134" text-anchor="middle" font-size="12" fill="#5b6675">pin → 220 Ω → LED → GND</text>'
    return _svg(b + _marca(True), 'LED con una resistencia en serie')

def i_motor():
    b = _placa(16, 46, 92, 'pr2')
    b += '<circle cx="180" cy="92" r="34" fill="#8a8f97"/><circle cx="180" cy="92" r="10" fill="#2b2f36"/><rect x="170" y="48" width="20" height="14" fill="#6b7078"/>'
    b += '<path d="M108 100 C 130 100, 130 70, 150 72" stroke="%s" stroke-width="4" fill="none"/>' % R
    b += _tachar(130, 86, 22)
    return _svg(b + _marca(False), 'Motor conectado directamente a un pin de la micro:bit')

def i_placa_ext():
    b = '<rect x="20" y="58" width="200" height="62" rx="8" fill="#2e78d6"/>'
    for i in range(8):
        b += '<rect x="%d" y="100" width="14" height="14" rx="2" fill="#f2c230"/>' % (34 + i * 22)
    b += _placa(66, 8, 108, 'pr3')
    b += '<rect x="196" y="66" width="20" height="26" rx="3" fill="#20252c"/><text x="206" y="138" text-anchor="middle" font-size="11" fill="#5b6675">pilas</text>'
    b += '<text x="110" y="138" text-anchor="middle" font-size="11" fill="#5b6675">placa de expansión</text>'
    return _svg(b + _marca(True, 24, 24), 'micro:bit insertada en una placa de expansión con alimentación propia')

def i_bordes():
    b = _placa(60, 26, 120, 'pr4')
    b += '<path d="M46 60 q-6 18 4 34 l16 -4 -4 -28z" fill="#f1c7a8" stroke="#c99a7b"/><path d="M194 60 q6 18 -4 34 l-16 -4 4 -28z" fill="#f1c7a8" stroke="#c99a7b"/>'
    return _svg(b + _marca(True), 'Manos sujetando la placa por los bordes')

def i_metal():
    b = '<rect x="10" y="98" width="220" height="30" rx="4" fill="#b9c0ca"/><path d="M10 104 H230 M10 114 H230" stroke="#fff" stroke-opacity=".6"/>'
    b += '<path d="M60 110 l20 -6 M150 116 l26 -4" stroke="#6b7078" stroke-width="3" stroke-linecap="round"/>'
    b += _placa(62, 22, 110, 'pr5')
    return _svg(b + _marca(False), 'Placa encendida apoyada sobre una superficie metálica con clips sueltos')

def i_agua():
    b = _placa(30, 40, 104, 'pr6')
    b += '<path d="M186 40 c-18 26 -24 40 -24 52 a24 24 0 0 0 48 0 c0 -12 -6 -26 -24 -52z" fill="#5aa9e6"/><path d="M176 90 a10 10 0 0 0 10 10" stroke="#fff" stroke-width="3" fill="none"/>'
    return _svg(b + _marca(False, 214, 130), 'Gota de agua junto a la placa')

def i_usb_cable():
    b = '<rect x="120" y="54" width="100" height="50" rx="6" fill="#1f2a37"/><rect x="104" y="70" width="18" height="18" rx="2" fill="#b9c0ca"/>'
    b += '<rect x="56" y="64" width="50" height="30" rx="6" fill="#2b2f36"/><path d="M56 79 H14" stroke="#2b2f36" stroke-width="8" stroke-linecap="round"/>'
    b += '<path d="M70 54 v-16 M90 54 v-16" stroke="%s" stroke-width="3"/><path d="M64 44 l6 -8 6 8 M84 44 l6 -8 6 8" stroke="%s" stroke-width="3" fill="none"/>' % (V, V)
    b += '<text x="80" y="124" text-anchor="middle" font-size="11" fill="#5b6675">tira del conector, recto</text>'
    return _svg(b + _marca(True), 'Desconectar el cable USB tirando del conector y en línea recta')

def i_guardar():
    b = '<path d="M40 60 h160 l-10 66 h-140z" fill="#d9bd88" stroke="#a78755" stroke-width="2"/><path d="M40 60 l14 -20 h132 l14 20" fill="#ead6ad" stroke="#a78755" stroke-width="2"/>'
    b += '<rect x="64" y="72" width="46" height="40" rx="4" fill="#c4ccd6" opacity=".9"/><rect x="122" y="72" width="46" height="40" rx="4" fill="#c4ccd6" opacity=".9"/>'
    b += '<text x="87" y="98" text-anchor="middle" font-size="14" font-weight="800" fill="%s">07</text><text x="145" y="98" text-anchor="middle" font-size="14" font-weight="800" fill="%s">08</text>' % (INK, INK)
    return _svg(b + _marca(True), 'Caja con las placas numeradas en bolsas')

def i_robot():
    b = '<rect x="40" y="56" width="150" height="54" rx="12" fill="#2e78d6"/><circle cx="66" cy="114" r="18" fill="#2b2f36"/><circle cx="164" cy="114" r="18" fill="#2b2f36"/>'
    b += '<rect x="96" y="40" width="44" height="18" rx="3" fill="#20252c"/>'
    b += '<rect x="150" y="66" width="30" height="16" rx="8" fill="#eef1f5" stroke="%s"/><circle cx="158" cy="74" r="6" fill="%s"/>' % (INK, INK)
    b += '<text x="165" y="100" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">OFF</text>'
    return _svg(b + _marca(True), 'Robot con el interruptor en OFF')

# ------------------------------------------------------------------ tarjetas
def tarjetas(items):
    out = '<div class="prec">'
    for svg, ok, t, d in items:
        cls = {True: 'si', False: 'no', None: 'info'}[ok]
        lab = {True: 'Hazlo así', False: 'Evítalo', None: 'Bueno saberlo'}[ok]
        out += '<div class="prec-c prec-%s"><div class="prec-img">%s</div><div class="prec-txt"><span class="prec-l">%s</span><b>%s</b><p>%s</p></div></div>' % (cls, svg, lab, t, d)
    return out + '</div>'

ALIMENTACION = [
    (i_pilas(), True, 'Dos pilas AAA alcalinas', 'El portapilas de la micro:bit lleva 2 pilas AAA de zinc o alcalinas. Colócalas respetando el + y el −.'),
    (i_mezclar(), False, 'Mezclar pilas', 'No juntes pilas nuevas con gastadas ni de tipos distintos. Retira las gastadas y no intentes cargar pilas que no son recargables.'),
    (i_enchufe(), False, 'Enchufe o batería externa', 'No conectes la placa directamente a la red ni a un cargador portátil. Las pilas recargables, solo si has comprobado su voltaje: la placa admite como máximo 3,6 V.'),
    (i_usb_y_pilas(), None, 'USB y pilas a la vez', 'Se pueden tener conectados el cable USB y el portapilas al mismo tiempo: la placa está preparada para ello.'),
]
CONEXIONES = [
    (i_cocodrilo(), None, 'Pinzas de cocodrilo rectas', 'Engancha la pinza recta en el anillo. En 0, 1 y 2, si roza los pines finos de al lado puede alterar la pantalla o la lectura de luz.'),
    (i_corto(), False, 'Unir 3V con GND', 'Un cable directo entre 3V y GND, o entre los polos del portapilas, es un cortocircuito: no lo hagas nunca.'),
    (i_resistencia(), True, 'LED con resistencia', 'Un LED externo siempre con una resistencia en serie (por ejemplo, 220 Ω). Los pines dan muy poca corriente.'),
    (i_motor(), False, 'Motores en un pin', 'Motores, servos, altavoces o tiras largas de LED no van directos a un pin: pueden estropear la placa con el tiempo.'),
    (i_placa_ext(), True, 'Placa de expansión', 'Para motores y servos usa una placa de expansión con sus propias pilas (Cutebot, Maqueen, WuKong, IoT:bit…).'),
]
MANIPULAR = [
    (i_bordes(), True, 'Sujétala por los bordes', 'Evita tocar los componentes y los contactos dorados con los dedos: la electricidad estática y la grasa de la piel no les sientan bien.'),
    (i_metal(), False, 'Sobre metal o con clips sueltos', 'No apoyes la placa encendida sobre una mesa metálica, papel de aluminio, clips o cables pelados: pueden provocar un cortocircuito por detrás.'),
    (i_agua(), False, 'Cerca del agua', 'Mantén la placa lejos de vasos, botellas y del riego. En los proyectos con plantas, el sensor va en la tierra; la placa, fuera y seca.'),
    (i_usb_cable(), True, 'El cable, por el conector', 'Conecta y desconecta el micro USB tirando del conector, en línea recta y sin hacer palanca. Lo mismo con el conector del portapilas: no lo fuerces.'),
    (i_guardar(), True, 'Guárdalas numeradas', 'Cada placa en su bolsa o compartimento, con un número. Así cada grupo trabaja siempre con la misma y se detectan antes las averías.'),
    (i_robot(), True, 'Robots apagados', 'Al terminar, pon el interruptor del robot en OFF y, si no se va a usar en semanas, quita las pilas.'),
]

FUENTES = ('<a href="https://tech.microbit.org/hardware/powersupply/" target="_blank" rel="noopener">alimentación</a> y '
           '<a href="https://tech.microbit.org/hardware/edge-connector/" target="_blank" rel="noopener">conector de borde</a> de tech.microbit.org, y '
           '<a href="https://support.microbit.org/solution/articles/19000013982-how-do-i-power-my-micro-bit-/en" target="_blank" rel="noopener">«How do I power my micro:bit?»</a> del soporte oficial')
