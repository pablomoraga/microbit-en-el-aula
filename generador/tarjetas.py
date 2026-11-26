# -*- coding: utf-8 -*-
"""Tarjetas imprimibles A5 (dos por A4): anverso con objetivo y pasos; reverso con pistas, bloques y «¿Y si…?».
build.py escribe el HTML; herramientas/tarjetas_pdf.py lo convierte en PDF con Chrome o Edge."""
import os, html, re
import common, makecode
from bloques import expand
from iconos import logo_lapiz
e = html.escape

CSS = '''@page{size:A4;margin:0}*{box-sizing:border-box}
body{margin:0;font:11.5pt/1.42 "Segoe UI",system-ui,sans-serif;color:#15202b;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.hoja{width:210mm;height:297mm;display:flex;flex-direction:column;page-break-after:always;overflow:hidden}
.t{width:210mm;height:148.5mm;padding:9mm 12mm 10mm;position:relative;overflow:hidden;border-bottom:1px dashed #b8c0ca;
 background:#fbfcfd}
.banda{display:flex;align-items:center;gap:4mm;background:#15202b;color:#fff;margin:-9mm -12mm 5mm;padding:4mm 12mm;border-bottom:1.2mm solid #ff5a36}
.banda img{width:12mm;height:12mm;border-radius:2.5mm}
.num{font:800 15pt Consolas,monospace;color:#ffd27a;letter-spacing:.05em}.grupo{font:9pt Consolas,monospace;color:#c9d2dc}
.chips{margin-left:auto;display:flex;flex-wrap:wrap;gap:1.5mm;justify-content:flex-end;max-width:90mm}
.chips span{font:8.5pt Consolas,monospace;border:1px solid #ffd27a;color:#ffd27a;border-radius:4mm;padding:.6mm 2.4mm}
h1{font-size:21pt;margin:0 0 3mm;letter-spacing:-.02em}
h2{font:800 9.5pt Consolas,monospace;text-transform:uppercase;letter-spacing:.08em;color:#e8461f;margin:3.2mm 0 1.4mm}
.obj{background:#fff;border:.5mm solid #15202b;border-radius:3mm;padding:2.4mm 4mm;box-shadow:1mm 1mm 0 #15202b}
ol,ul{margin:0;padding-left:6mm}li{margin:.7mm 0}
.dos{display:grid;grid-template-columns:1fr 1fr;gap:6mm}
.bloques{background:#fff;border:.4mm solid #d5dbe3;border-radius:3mm;padding:2mm;display:flex;align-items:center;justify-content:center;height:66mm}
.bloques img{max-width:100%;max-height:62mm;object-fit:contain}
.pie{position:absolute;left:12mm;right:12mm;bottom:4mm;font:7.5pt Consolas,monospace;color:#7a8592;border-top:1px solid #d5dbe3;padding-top:1.2mm;display:flex;justify-content:space-between}
.mat{font-size:9.5pt;color:#5b6675;margin:2mm 0 0}
.e-mb,.e-py{display:none}.bq{display:inline-block;background:var(--c);color:#fff;font-weight:700;font-size:.86em;padding:.2mm 2mm .5mm;border-radius:1.4mm;white-space:nowrap}'''

def _front(f, logo):
    pasos = ''.join('<li>%s</li>' % expand(p) for p in f['pasos'])
    mat = ('<p class="mat"><b>Necesitas:</b> %s</p>' % ', '.join(f['materiales'])) if f['materiales'] else ''
    return ('<div class="t"><div class="banda"><img src="%s" alt=""><div><div class="num">PRÁCTICA %s</div><div class="grupo">%s</div></div>'
            '<div class="chips"><span>%s</span><span>%s</span></div></div>'
            '<h1>%s</h1><div class="obj"><b>Objetivo:</b> %s</div>%s<h2>Paso a paso</h2><ol>%s</ol>'
            '<div class="pie"><span>micro:bit en el aula · Pablo Moraga</span><span>Solución en MakeCode, MicroBlocks y Python en la web</span></div></div>') % (
        logo, e(f['num']), e(f['group'] or ''), common.NIVEL[f['nivel']], e(f['tiempo']), e(f['title']), f['objetivo'], mat, pasos)

def _back(f, imgdir):
    pistas = ''.join('<li>%s</li>' % expand(p) for p in f['pistas'])
    amp = ''.join('<li>%s</li>' % p for p in f['ampliar'])
    img = ''
    if f['mc'] and os.path.exists(os.path.join(makecode.IMG, f['mc'] + '.webp')):
        img = '<img src="%s/%s.webp" alt="">' % (imgdir, f['mc'])
    return ('<div class="t"><h2 style="margin-top:0">Práctica %s · %s</h2><div class="dos"><div><h2>Pistas</h2><ul>%s</ul><h2>¿Y si…?</h2><ul>%s</ul></div>'
            '<div><h2>Una solución en MakeCode</h2><div class="bloques">%s</div></div></div>'
            '<div class="pie"><span>%s</span><span>pablomoraga.github.io/microbit-en-el-aula</span></div></div>') % (
        e(f['num']), e(f['title']), pistas, amp, img, e(f['title']))

def build_html(out_path, section='comenzamos'):
    fichas = [f for f in common.FICHAS if f['section'] == section]
    logo = 'data:image/svg+xml;utf8,' + logo_lapiz().replace('#', '%23').replace('"', "'")
    imgdir = 'file:///' + makecode.IMG.replace('\\', '/')
    hojas = []
    for i in range(0, len(fichas), 2):
        par = fichas[i:i + 2]
        hojas.append('<div class="hoja">%s</div>' % ''.join(_front(f, logo) for f in par))
        hojas.append('<div class="hoja">%s</div>' % ''.join(_back(f, imgdir) for f in par))
    # Antes de imprimir, cada imagen de bloques se convierte en JPEG a la resolución que ocupa en papel (≈ 220 ppp): el PDF pesa mucho menos.
    js = ('<script>window.addEventListener("load",function(){document.querySelectorAll(".bloques img").forEach(function(i){'
          'var r=i.getBoundingClientRect(),k=2.3,c=document.createElement("canvas");c.width=Math.round(r.width*k);c.height=Math.round(r.height*k);'
          'var g=c.getContext("2d");g.fillStyle="#fff";g.fillRect(0,0,c.width,c.height);g.drawImage(i,0,0,c.width,c.height);'
          'i.style.width=r.width+"px";i.style.height=r.height+"px";i.src=c.toDataURL("image/jpeg",.86);});});</script>')
    doc = '<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><title>Tarjetas</title><style>%s</style></head><body>%s%s</body></html>' % (CSS, ''.join(hojas), js)
    doc = re.sub(r'<b class="blk">(.*?)</b>', r'<b>\1</b>', doc)
    open(out_path, 'w', encoding='utf-8').write(doc)
    return len(fichas)
