# -*- coding: utf-8 -*-
"""Recortables imprimibles (A4, en milímetros) con una ventana para la micro:bit V2 (51,6 × 42 mm).
Se imprimen al 100 % en cartulina, se recortan por la línea continua y la placa se pega por detrás."""
import os

MB_W, MB_H = 51.6, 42.0          # tamaño de la micro:bit (documentación técnica)

def _doc(titulo, figura, color, extra=''):
    cx, cy = 105, 140
    vx, vy = cx - MB_W / 2, cy - MB_H / 2
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297" font-family="Arial,sans-serif">'
            '<rect width="210" height="297" fill="#fff"/>'
            '<text x="105" y="16" text-anchor="middle" font-size="7" font-weight="bold" fill="#15202b">%s · micro:bit en el aula</text>'
            '<text x="105" y="24" text-anchor="middle" font-size="3.6" fill="#5b6675">Imprime al 100 %% en cartulina. Recorta por la línea continua y la ventana. Pega la micro:bit por detrás con cinta.</text>'
            '%s%s'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" fill="#fff" stroke="#15202b" stroke-width=".5" stroke-dasharray="2 1.5"/>'
            '<text x="105" y="%.1f" text-anchor="middle" font-size="3.4" fill="#5b6675">ventana para la micro:bit (51,6 × 42 mm)</text>'
            '<text x="105" y="288" text-anchor="middle" font-size="3" fill="#9aa1aa">© Pablo Moraga · CC BY-NC 4.0</text></svg>') % (
        titulo, figura, extra, vx, vy, MB_W, MB_H, cy + MB_H / 2 + 6)

def calabaza():
    f = ('<path d="M105 62 C 40 62, 22 110, 26 150 C 30 205, 70 232, 105 232 C 140 232, 180 205, 184 150 C 188 110, 170 62, 105 62 Z" fill="#f28c28" stroke="#15202b" stroke-width=".8"/>'
         '<path d="M70 70 C 55 110, 55 190, 72 226 M140 70 C 155 110, 155 190, 138 226" fill="none" stroke="#c96a14" stroke-width=".8"/>'
         '<path d="M98 64 C 96 50, 100 42, 112 38 L114 44 C 106 48, 106 54, 108 64 Z" fill="#5a8a2e" stroke="#15202b" stroke-width=".8"/>')
    return _doc('Calabaza de Halloween', f, '#f28c28')

def arbol():
    f = ('<path d="M105 40 L170 120 H148 L186 190 H158 L194 246 H16 L52 190 H24 L62 120 H40 Z" fill="#2e9d4f" stroke="#15202b" stroke-width=".8"/>'
         '<rect x="94" y="246" width="22" height="22" fill="#8a5a33" stroke="#15202b" stroke-width=".8"/>'
         '<path d="M105 30 l3 7 7 .5 -5.5 4.5 2 7 -6.5 -4 -6.5 4 2 -7 -5.5 -4.5 7 -.5z" fill="#ffd27a" stroke="#15202b" stroke-width=".6"/>')
    return _doc('Árbol de Navidad', f, '#2e9d4f')

def matraz():
    f = ('<path d="M88 40 H122 V52 H116 V95 L176 220 Q182 236 166 236 H44 Q28 236 34 220 L94 95 V52 H88 Z" fill="#e4f3ef" stroke="#15202b" stroke-width=".8"/>'
         '<path d="M58 180 H152 L168 222 Q172 230 162 230 H48 Q38 230 42 222 Z" fill="#8a5cf6" opacity=".55"/>'
         '<circle cx="80" cy="200" r="4" fill="#fff" opacity=".8"/><circle cx="128" cy="206" r="3" fill="#fff" opacity=".8"/>')
    return _doc('Matraz de científica', f, '#8a5cf6')

def sol():
    rays = ''.join('<path d="M105 140 L%.1f %.1f" stroke="#e8a400" stroke-width="7" stroke-linecap="round"/>' % (
        105 + 92 * __import__('math').cos(a * 0.5236), 140 + 92 * __import__('math').sin(a * 0.5236)) for a in range(12))
    f = rays + '<circle cx="105" cy="140" r="62" fill="#ffd27a" stroke="#15202b" stroke-width=".8"/>'
    return _doc('Sol de verano', f, '#ffd27a')

def escribir(carpeta):
    os.makedirs(carpeta, exist_ok=True)
    for nombre, fn in (('calabaza', calabaza), ('arbol-de-navidad', arbol), ('matraz', matraz), ('sol', sol)):
        open(os.path.join(carpeta, nombre + '.svg'), 'w', encoding='utf-8').write(fn())
