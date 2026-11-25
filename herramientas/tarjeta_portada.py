# -*- coding: utf-8 -*-
"""Genera el HTML de la imagen de tarjeta (1200 × 600) para la página principal.
Uso: python herramientas/tarjeta_portada.py salida.html  y luego una captura con Chrome headless."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'generador'))
import placa_pro

CSS = '''html,body{margin:0;width:1200px;height:600px;overflow:hidden}
body{background:#eef1f5;background-image:linear-gradient(rgba(21,32,43,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(21,32,43,.05) 1px,transparent 1px);
 background-size:28px 28px;font-family:"Segoe UI",system-ui,sans-serif;display:grid;grid-template-columns:520px 1fr;align-items:center}
.t{padding-left:70px}.k{font:700 17px Consolas,monospace;letter-spacing:.14em;color:#0f8a72;text-transform:uppercase}
h1{font-weight:800;font-size:84px;line-height:.95;margin:.15em 0 .1em;color:#15202b;letter-spacing:-.03em}
.l{font-family:"Ink Free","Segoe Print",cursive;font-weight:700;font-size:80px;color:transparent;
 background:repeating-linear-gradient(-58deg,#ff5a36 0 2.6px,#ff8b6b 2.6px 4.2px,#e8461f 4.2px 6px);-webkit-background-clip:text;background-clip:text;
 -webkit-text-stroke:1.6px #b8351a;display:inline-block;transform:rotate(-2deg);filter:url(#lapiz)}
.c{display:inline-block;margin-top:26px;background:#15202b;color:#ffd27a;font:700 20px Consolas,monospace;padding:10px 16px;border-radius:10px}
.i svg{width:690px;height:auto;display:block;margin-left:-20px}'''

html = ('<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body>'
        '<svg width="0" height="0" style="position:absolute"><filter id="lapiz"><feTurbulence type="fractalNoise" baseFrequency=".55" numOctaves="2" seed="7" result="n"/>'
        '<feDisplacementMap in="SourceGraphic" in2="n" scale="2.4"/></filter></svg>'
        '<div class="t"><div class="k">Primaria · ESO</div><h1>micro:bit</h1><span class="l">en el aula</span><br>'
        '<span class="c">MakeCode · MicroBlocks · Python</span></div><div class="i">%s</div></body></html>') % (CSS, placa_pro.hero())
open(sys.argv[1], 'w', encoding='utf-8').write(html)
