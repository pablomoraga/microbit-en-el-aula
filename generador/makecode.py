# -*- coding: utf-8 -*-
"""MakeCode: cada programa se escribe en JavaScript (el mismo que muestra la pestaña JavaScript de MakeCode).
Las imágenes de los bloques las dibuja el propio MakeCode con herramientas/renderizar_makecode.py
y se guardan en estaticos/img/makecode/<id>.webp (a doble resolución)."""
import hashlib, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, 'estaticos', 'img', 'makecode')
REG = {}          # id -> dict(code, pkg)
e = html.escape

# extensiones (nombre=github:repositorio) que se cargan para dibujar los bloques
PKG = {
    'cutebot': 'cutebot=github:elecfreaks/pxt-cutebot',
    'maqueen': 'maqueen=github:DFRobot/pxt-maqueen',
    'maqueenplus': 'maqueenPlusV2=github:DFRobot/pxt-DFRobot_MaqueenPlus_v20',
    'wukong': 'wukong=github:elecfreaks/pxt-wukong',
    'environment': 'environment=github:tinkertanker/pxt-iot-environment-kit',
    'sonarbit': 'sonarbit=github:elecfreaks/pxt-sonarbit',
    'neopixel': 'neopixel=github:microsoft/pxt-neopixel',
    'servo': 'servo=github:microsoft/pxt-servo',
}
# lo que el alumnado escribe en el buscador de extensiones
EXT_BUSCAR = {
    'cutebot': ('Cutebot', 'cutebot'), 'maqueen': ('Maqueen', 'maqueen'),
    'maqueenplus': ('MaqueenPlusV2', 'https://github.com/DFRobot/pxt-DFRobot_MaqueenPlus_v20'),
    'wukong': ('WuKong', 'wukong'), 'environment': ('Octopus (iot-environment-kit)', 'iot-environment-kit'),
    'sonarbit': ('sonar:bit', 'https://github.com/elecfreaks/pxt-sonarbit'), 'neopixel': ('NeoPixel', 'neopixel'),
    'servo': ('Servo', 'servo'),
}

def key(code, pkgs=()):
    pk = ','.join(PKG[p] for p in pkgs)
    return 'mc-' + hashlib.sha1((pk + '\n' + code.strip()).encode('utf-8')).hexdigest()[:12], pk

def blocks(code, pkgs=(), alt='Programa en bloques de MakeCode'):
    """Imagen de los bloques (o un aviso si aún no se ha renderizado)."""
    k, pk = key(code, pkgs)
    REG[k] = dict(code=code.strip(), pkg=pk)
    if os.path.exists(os.path.join(IMG, k + '.webp')):
        w, h = webp_size(os.path.join(IMG, k + '.webp'))
        return ('<figure class="mc-img"><img src="{{ROOT}}img/makecode/%s.webp" width="%d" height="%d" '
                'alt="%s" loading="lazy"></figure>' % (k, w // 2, h // 2, e(alt)))
    return '<p class="aviso">⏳ Imagen de los bloques pendiente (<code>%s</code>).</p>' % k

def webp_size(path):
    """Ancho y alto de un archivo WebP (formatos VP8, VP8L y VP8X)."""
    b = open(path, 'rb').read(40)
    kind = b[12:16]
    if kind == b'VP8X':
        return 1 + int.from_bytes(b[24:27], 'little'), 1 + int.from_bytes(b[27:30], 'little')
    if kind == b'VP8L':
        v = int.from_bytes(b[21:25], 'little')
        return 1 + (v & 0x3FFF), 1 + ((v >> 14) & 0x3FFF)
    return int.from_bytes(b[26:28], 'little') & 0x3FFF, int.from_bytes(b[28:30], 'little') & 0x3FFF

def missing():
    return [dict(id=k, code=v['code'], pkg=v['pkg']) for k, v in REG.items() if not os.path.exists(os.path.join(IMG, k + '.webp'))]

def all_jobs():
    return [dict(id=k, code=v['code'], pkg=v['pkg']) for k, v in REG.items()]
