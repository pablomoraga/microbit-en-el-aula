# -*- coding: utf-8 -*-
"""Registro de páginas y utilidades para escribir el contenido."""
import html, os, re, urllib.parse
import makecode, mbk
from bloques import expand, SELECTOR
from iconos import icon

PAGES = []      # dict(section, group, slug, title, body, kind, meta)
UBP = {}        # nombre -> texto del proyecto MicroBlocks
PY = {}         # nombre -> programa de Python
e = html.escape
SITE_URL = 'https://pablomoraga.github.io/microbit-en-el-aula/'

def page(section, slug, title, body, group=None, kind='texto', meta=None, icono=None):
    PAGES.append(dict(section=section, slug=slug, title=title, body=body, group=group, kind=kind, meta=meta or {}, icono=icono))

def ul(items): return '<ul>' + ''.join('<li>%s</li>' % i for i in items) + '</ul>'
def ol(items): return '<ol class="pasos">' + ''.join('<li>%s</li>' % i for i in items) + '</ol>'
def P(*ps): return ''.join('<p>%s</p>' % p for p in ps)
def h2(t): return '<h2>%s</h2>' % t
def h3(t): return '<h3>%s</h3>' % t

BOX = {'idea': ('bombilla', 'Idea'), 'ojo': ('aviso', 'Atención'), 'docente': ('docente', 'Para el profesorado'),
       'reto': ('cohete', '¿Y si…?'), 'sabias': ('lupa', '¿Sabías que…?'), 'material': ('caja', 'Necesitas')}
def box(kind, title, inner):
    ic = BOX[kind][0]
    return '<div class="caja caja-%s"><p class="caja-t">%s<span>%s</span></p>%s</div>' % (kind, icon(ic, 20), e(title), inner)

def tabla(head, rows, cls='tabla'):
    out = '<div class="tabla-wrap"><table class="%s"><thead><tr>%s</tr></thead><tbody>' % (cls, ''.join('<th>%s</th>' % h for h in head))
    for r in rows:
        out += '<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in r)
    return out + '</tbody></table></div>'

def kbd(t): return '<b class="blk">%s</b>' % t        # nombre de bloque dentro del texto

NIVEL = {1: '★☆☆', 2: '★★☆', 3: '★★★'}
ETAPA = {'P1': 'Primaria 6-9', 'P2': 'Primaria 10-12', 'ESO': 'ESO'}

# ------------------------------------------------------------------ Python
PY_KW = r'\b(from|import|while|True|False|None|if|elif|else|for|in|def|return|and|or|not|break|continue|global|pass|range|lambda)\b'
def py_html(src):
    out = []
    for line in src.split('\n'):
        tokens = re.split(r'(#.*$|"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\')', line)
        buf = ''
        for t in tokens:
            if not t: continue
            if t.startswith('#'): buf += '<span class="c">%s</span>' % e(t)
            elif t[0] in '"\'': buf += '<span class="s">%s</span>' % e(t)
            else:
                x = e(t)
                x = re.sub(PY_KW, r'<span class="k">\1</span>', x)
                x = re.sub(r'(?<![\w.])(\d+)(?![\w])', r'<span class="n">\1</span>', x)
                buf += x
        out.append(buf)
    return '\n'.join(out)

# ------------------------------------------------------------------ paneles de código
def panel_makecode(code, pkgs=(), nota=''):
    ext = ''
    if pkgs:
        names = ', '.join('<b>%s</b> (busca <code>%s</code>)' % (makecode.EXT_BUSCAR[p][0], e(makecode.EXT_BUSCAR[p][1])) for p in pkgs)
        ext = '<p class="ext">%s Antes de empezar añade la extensión %s: <b>Extensiones</b> (al final de la lista de categorías) y escribe el nombre en el buscador.</p>' % (icon('pieza', 18), names)
    sim = ''
    if not pkgs:
        sim = ('<details class="sim"><summary>%s Probar en el simulador</summary><div class="sim-marco" data-code="%s"></div>'
               '<p class="hint">Es el simulador oficial de MakeCode: pulsa sus botones, toca el logotipo o mueve los controles de los sensores.</p></details>') % (
            icon('placa', 18), e(code.strip(), quote=True))
    return ('%s%s' + sim.replace('%', '%%') + '%s<details class="codigo-js"><summary>Ver y copiar el código JavaScript</summary>'
            '<pre class="code"><code>%s</code></pre><button class="copiar" type="button">Copiar</button>'
            '<p class="hint">En MakeCode abre la pestaña <b>JavaScript</b>, borra lo que haya, pega el código y vuelve a <b>Bloques</b>.</p></details>'
            '<p class="acciones"><a class="btn-sec" href="https://makecode.microbit.org/#editor" target="_blank" rel="noopener">%s Abrir MakeCode</a></p>') % (
        ext, makecode.blocks(code, pkgs), nota, e(code.strip()), icon('externo', 16))

def panel_microblocks(src, name, desc=''):
    UBP[name] = mbk.ubp(src, desc)
    libs = mbk.used_libraries(src)
    lib_txt = ''
    if libs:
        lib_txt = '<p class="ext">%s Usa las bibliotecas %s. Al abrir el proyecto se cargan solas.</p>' % (
            icon('pieza', 18), ', '.join('<b>%s</b>' % e(mbk.tr(l)) for l in libs))
    open_url = 'https://microblocks.fun/run/microblocks.html?lang=es&project=' + urllib.parse.quote(SITE_URL + 'programas/microblocks/' + name + '.ubp', safe='')
    html_blocks = mbk.render(src)
    MBPNG[name] = dict(html=html_blocks, text=mbk.script_text(src))
    png = os.path.join(MBPNG_DIR, name + '.png')
    if os.path.exists(png):
        w, h = _png_size(png)
        vista = ('<figure class="mb-png"><img src="{{ROOT}}img/microblocks/%s.png" width="%d" height="%d" alt="Programa de MicroBlocks: %s" draggable="true" loading="lazy">'
                 '<figcaption>%s <b>Arrastra esta imagen</b> al área de programación de MicroBlocks y aparecerán los bloques (también puedes guardarla y soltarla después).</figcaption></figure>') % (
            name, w // 2, h // 2, e(desc), icon('bloques2', 16))
    else:
        vista = html_blocks
    return ('%s%s<p class="acciones"><a class="btn-sec" href="%s" target="_blank" rel="noopener">%s Abrir en MicroBlocks</a> '
            '<a class="btn-sec" href="{{ROOT}}programas/microblocks/%s.ubp" download>%s Descargar .ubp</a></p>'
            '<p class="hint">Abre MicroBlocks en Chrome o Edge. Si pregunta si quieres actualizar una biblioteca a una versión nueva, pulsa <b>Sí</b>.</p>') % (
        vista, lib_txt, e(open_url), icon('externo', 16), name, icon('descarga', 16))

MBPNG = {}
MBPNG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'estaticos', 'img', 'microblocks')

def _png_size(path):
    b = open(path, 'rb').read(24)
    return int.from_bytes(b[16:20], 'big'), int.from_bytes(b[20:24], 'big')

def panel_python(src, name):
    PY[name] = src.strip() + '\n'
    return ('<pre class="code py"><code>%s</code></pre><button class="copiar" type="button">Copiar</button>'
            '<p class="acciones"><a class="btn-sec" href="https://python.microbit.org/" target="_blank" rel="noopener">%s Abrir el editor de Python</a> '
            '<a class="btn-sec" href="{{ROOT}}programas/python/%s.py" download>%s Descargar .py</a></p>'
            '<p class="hint">En el editor de Python pulsa <b>Abrir…</b> y elige el archivo .py, o pega el código.</p>') % (
        py_html(src.strip()), icon('externo', 16), name, icon('descarga', 16))

def soluciones(name, mc=None, mb=None, py=None, pkgs=(), desc='', mc_nota=''):
    """Pestañas con el programa en los tres editores. El alumnado elige y la web recuerda su elección."""
    tabs, panels = [], []
    for key, label, ic, content in (('makecode', 'MakeCode', 'bloques', mc), ('microblocks', 'MicroBlocks', 'bloques2', mb), ('python', 'Python', 'codigo', py)):
        if content is None: continue
        tabs.append('<button type="button" role="tab" data-t="%s">%s%s</button>' % (key, icon(ic, 16), label))
        if key == 'makecode': body = panel_makecode(content, pkgs, mc_nota)
        elif key == 'microblocks': body = panel_microblocks(content, name, desc)
        else: body = panel_python(content, name)
        panels.append('<div class="tab-panel" role="tabpanel" data-t="%s">%s</div>' % (key, body))
    return '<div class="tabs"><div class="tab-bar" role="tablist">%s</div>%s</div>' % (''.join(tabs), ''.join(panels))

# ------------------------------------------------------------------ prácticas
FICHAS = []
def practica(section, num, slug, title, nivel, etapa, tiempo, conceptos, objetivo, pasos, pistas, mc, mb, py, ampliar,
             group=None, materiales=None, nota=None, explica=None, pkgs=(), icono='chip', mc_nota='', conexion=None):
    head = ('<div class="ficha"><span class="chip chip-num">%s</span><span class="chip">Dificultad %s</span><span class="chip">%s</span>'
            '<span class="chip">%s %s</span>%s</div>' % (e(num), NIVEL[nivel], e(ETAPA[etapa]), icon('reloj', 14), e(tiempo),
                                                       ''.join('<span class="chip chip-c">%s</span>' % e(c) for c in conceptos)))
    body = head + '<div class="objetivo">%s<div><b>Objetivo</b><p>%s</p></div></div>' % (icon('diana', 28), objetivo)
    if materiales:
        body += box('material', 'Necesitas', ul(materiales))
    if conexion:
        body += '<h2>Conexiones</h2>' + conexion
    body += '<h2>Paso a paso</h2>' + SELECTOR + ol([expand(x) for x in pasos])
    if nota:
        body += nota
    body += '<details class="ayuda"><summary>%s Ayuda: pistas</summary>%s</details>' % (icon('salvavidas', 18), ul([expand(x) for x in pistas]))
    body += ('<details class="ayuda sol"><summary>%s Una solución posible</summary><p class="hint">Elige el editor con el que trabajas: '
             'la web lo recordará en las demás prácticas.</p>%s%s</details>' % (
                 icon('check', 18), soluciones(slug, mc, mb, py, pkgs, title, mc_nota), ('<p>%s</p>' % explica) if explica else ''))
    if ampliar:
        body += box('reto', '¿Y si…?', ul(ampliar))
    FICHAS.append(dict(slug=slug, num=num, title=title, section=section, group=group, objetivo=objetivo, pasos=pasos, pistas=pistas,
                       ampliar=ampliar or [], nivel=nivel, etapa=etapa, tiempo=tiempo, conceptos=conceptos, materiales=materiales or [],
                       mc=makecode.key(mc, pkgs)[0] if mc else None))
    page(section, slug, title, body, group=group, kind='practica', meta=dict(num=num, nivel=nivel, tiempo=tiempo, etapa=etapa), icono=icono)

def proyecto(section, slug, title, group, intro, materiales, conexiones, fases, mc=None, mb=None, py=None, pkgs=(),
             ampliar=None, docente=None, icono='chip', tiempo='60 min', etapa='P2', mc_nota='', extra=''):
    """Proyecto de taller o de modo experto, con fases."""
    head = '<div class="ficha"><span class="chip">%s %s</span><span class="chip">%s</span></div>' % (icon('reloj', 14), e(tiempo), e(ETAPA[etapa]))
    body = head + P(intro)
    if materiales: body += box('material', 'Necesitas', ul(materiales))
    if conexiones: body += '<h2>Conexiones</h2>' + conexiones
    if fases: body += '<h2>Paso a paso</h2>' + SELECTOR + ol([expand(x) for x in fases])
    body += extra
    if mc or mb or py:
        body += '<h2>Programa</h2>' + soluciones(slug, mc, mb, py, pkgs, title, mc_nota)
    if ampliar: body += box('reto', '¿Y si…?', ul(ampliar))
    if docente: body += box('docente', 'Para el profesorado', docente)
    page(section, slug, title, body, group=group, kind='proyecto', meta=dict(tiempo=tiempo, etapa=etapa), icono=icono)

def anatomia(img, alt, puntos, pie=''):
    """Captura real de un editor con sus partes numeradas (x e y en % de la imagen) y una leyenda debajo."""
    marks = ''.join(('<span class="anat-pt" tabindex="0" style="left:%s%%;top:%s%%" aria-label="%s">%d'
                     '<span class="anat-tip%s"><b>%s</b>%s</span></span>') % (x, y, e(t), i + 1, ' izq' if x > 60 else '', t, d) for i, (x, y, t, d) in enumerate(puntos))
    ley = ''.join('<li><span class="n">%d</span><b>%s</b>%s</li>' % (i + 1, t, d) for i, (x, y, t, d) in enumerate(puntos))
    return ('<figure class="captura"><div class="anat-wrap"><img src="{{ROOT}}img/editores/%s" alt="%s" loading="lazy">%s</div>'
            '%s</figure><ol class="leyenda">%s</ol>') % (img, e(alt), marks, ('<figcaption>%s</figcaption>' % pie) if pie else '', ley)
