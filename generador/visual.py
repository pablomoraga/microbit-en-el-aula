# -*- coding: utf-8 -*-
"""Componentes visuales: pasos con imagen, recortes de capturas reales e ilustraciones sencillas."""
import html
from placa import frente, _nested, CORAZON, SONRISA
e = html.escape

def recorte(img, x, y, w, h, W=800, H=475, alt=''):
    """Recorte de una captura (coordenadas en píxeles de la captura original W × H)."""
    bs = 100.0 * W / w
    px = 0 if W == w else 100.0 * x / (W - w)
    py = 0 if H == h else 100.0 * y / (H - h)
    return ('<div class="recorte" role="img" aria-label="%s" style="aspect-ratio:%d/%d;background-image:url({{ROOT}}img/editores/%s);'
            'background-size:%.2f%% auto;background-position:%.2f%% %.2f%%"></div>') % (e(alt), w, h, img, bs, px, py)

def pasos(items):
    """items: lista de (html_de_la_imagen, título, texto)."""
    out = '<ol class="pasos-v">'
    for i, (img, t, d) in enumerate(items, 1):
        out += '<li><div class="pv-img">%s</div><div class="pv-txt"><span class="pv-n">%d</span><span class="pv-t">%s</span><p>%s</p></div></li>' % (img, i, t, d)
    return out + '</ol>'

# ------------------------------------------------------------------ ilustraciones
def _svg(w, h, body, label):
    return '<svg class="ilus" viewBox="0 0 %d %d" role="img" aria-label="%s" font-family="system-ui,sans-serif">%s</svg>' % (w, h, e(label), body)

def usb():
    b = '<rect x="18" y="20" width="150" height="96" rx="8" fill="#15202b"/><rect x="26" y="28" width="134" height="80" rx="4" fill="#bfe3ff"/>'
    b += '<path d="M8 120 h170 l-10 12 h-150z" fill="#9aa4b1"/>'
    b += '<path d="M168 112 C 210 112, 210 70, 240 70" stroke="#2b2f36" stroke-width="5" fill="none" stroke-linecap="round"/>'
    b += '<rect x="236" y="62" width="14" height="16" rx="2" fill="#b9c0ca"/>'
    b += _nested(frente(callouts=False, lit=set(), uid='u1'), 248, 30, 96, 80)
    b += '<circle cx="296" cy="36" r="5" fill="#ffcc00"/><text x="210" y="140" font-size="12" fill="#5b6675">cable USB de datos</text>'
    return _svg(350, 148, b, 'Ordenador conectado a la micro:bit con un cable USB')

def arrastrar():
    b = ('<path d="M30 20 h50 l18 18 v76 h-68z" fill="#fff" stroke="#15202b" stroke-width="2"/><path d="M80 20 v18 h18" fill="#eef1f5" stroke="#15202b" stroke-width="2"/>'
         '<text x="64" y="80" text-anchor="middle" font-size="13" font-weight="800" fill="#ff5a36">.hex</text>'
         '<path d="M115 70 H215" stroke="#0f8a72" stroke-width="4" stroke-dasharray="8 6"/><path d="M205 58 l16 12 -16 12" fill="none" stroke="#0f8a72" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
         '<rect x="232" y="40" width="96" height="64" rx="8" fill="#eef1f5" stroke="#15202b" stroke-width="2"/><rect x="232" y="88" width="96" height="16" rx="0" fill="#d5dbe3"/>'
         '<circle cx="316" cy="96" r="3.5" fill="#2fb44a"/><text x="280" y="72" text-anchor="middle" font-size="13" font-weight="800" fill="#15202b">MICROBIT</text>'
         '<text x="280" y="126" text-anchor="middle" font-size="12" fill="#5b6675">unidad USB</text>')
    return _svg(350, 140, b, 'Archivo .hex arrastrado a la unidad MICROBIT')

def funciona():
    b = _nested(frente(callouts=False, lit=CORAZON, uid='f1'), 95, 8, 160, 133)
    b += '<path d="M60 70 a40 40 0 0 1 0 -40 M268 70 a40 40 0 0 0 0 -40" stroke="#ff5a36" stroke-width="3" fill="none" stroke-linecap="round" opacity=".7"/>'
    return _svg(350, 148, b, 'La micro:bit ejecuta el programa')

def firmware():
    b = ('<rect x="20" y="30" width="110" height="80" rx="10" fill="#fff" stroke="#15202b" stroke-width="2"/>'
         '<text x="75" y="62" text-anchor="middle" font-size="12" font-weight="800" fill="#15202b">firmware de</text>'
         '<text x="75" y="80" text-anchor="middle" font-size="12" font-weight="800" fill="#d18c25">MicroBlocks</text>'
         '<path d="M140 70 H200" stroke="#d18c25" stroke-width="4" stroke-dasharray="8 6"/><path d="M190 58 l16 12 -16 12" fill="none" stroke="#d18c25" stroke-width="4"/>')
    b += _nested(frente(callouts=False, lit=SONRISA, uid='fw'), 212, 18, 126, 105)
    return _svg(350, 140, b, 'Instalar el firmware de MicroBlocks en la placa (solo la primera vez)')
