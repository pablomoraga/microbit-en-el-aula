# -*- coding: utf-8 -*-
"""Construye la web completa en _salida/web (o en la carpeta indicada en la variable SALIDA)."""
import os, re, shutil, json, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common, makecode, placa, placa_pro, tarjetas
from common import PAGES, e, P
from iconos import icon, svg_file, logo_lapiz
import c_empezar, c_conoce, c_comenzamos, c_errores, c_matematicas, c_experto, c_talleres, c_ia, c_celebrar, c_imprime, c_saber

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get('SALIDA', os.path.join(HERE, '..', '_salida'))
SITE = os.path.join(OUT, 'web')
TITLE = 'micro:bit en el aula'
import hashlib
VER = hashlib.sha1((open(os.path.join(HERE, 'estilo.css'), 'rb').read() + open(os.path.join(HERE, 'app.js'), 'rb').read())).hexdigest()[:8]

SECTIONS = [
    ('empezar', '01', 'Para empezar', 'placa', 'Qué es programar, por qué micro:bit, bloques frente a texto y pensamiento computacional.'),
    ('conoce', '02', 'Conoce micro:bit', 'chip', 'La placa V2 parte a parte, los editores MakeCode, MicroBlocks y Python, y sus extensiones.'),
    ('comenzamos', '03', 'Comenzamos', 'led', '30 prácticas progresivas con objetivo, paso a paso, ayuda, simulador y solución en los tres editores.'),
    ('errores', '04', 'Encuentra el error', 'lupa', '10 programas con un fallo escondido para aprender a depurar como detectives.'),
    ('matematicas', '05', 'Matemáticas', 'calculadora', 'Tablas, fracciones, coordenadas, velocidad, binario, probabilidad y estadística con la placa.'),
    ('experto', '06', 'Modo experto', 'cohete', 'Juegos, retos, cables de cocodrilo y sensores externos para ir más lejos.'),
    ('talleres', '07', 'Talleres', 'engranaje', 'Proyectos tipo (invernadero, estación meteorológica…) y talleres con kits y robots.'),
    ('ia', '08', 'Inteligencia artificial', 'cerebro', 'Entrena un modelo con tus movimientos usando micro:bit CreateAI y úsalo en MakeCode.'),
    ('celebrar', '09', 'Para celebrar', 'calendario', 'Pequeñas actividades para Halloween, el Día de la Niña en la Ciencia, Navidad y verano.'),
    ('imprime', '10', 'Imprime en 3D', 'caja', 'Mis diseños 3D, ideas de carcasas y soportes y dónde buscar más.'),
    ('saber', '11', 'Para saber más', 'libro', 'Problemas frecuentes, glosario, evaluación, tarjetas imprimibles y enlaces.'),
]
SEC = {s[0]: s for s in SECTIONS}
INTRO = {
    'empezar': P('Antes de conectar la placa conviene saber qué es programar y por qué usamos micro:bit. Este apartado sirve para el alumnado y para el profesorado.'),
    'conoce': P('Un recorrido por la placa micro:bit V2 y por los tres editores que usamos en el material. Cada práctica tiene su solución en los tres, así que puedes elegir el que mejor encaje con tu grupo.'),
    'comenzamos': P('Treinta prácticas ordenadas de menos a más, agrupadas en seis bloques. Cada una se hace en 15-30 minutos y tiene objetivo, paso a paso, pistas y una solución en <b>MakeCode</b>, <b>MicroBlocks</b> y <b>Python</b>.',
                    'Las primeras están pensadas para Primaria; las últimas sirven para ESO. Solo necesitas la micro:bit y un cable USB (y en la radio, dos placas).') +
                  '<p class="acciones"><a class="btn-sec" href="../recursos/tarjetas-comenzamos.pdf" download>' + icon('descarga', 16) +
                  ' Tarjetas imprimibles de las 30 prácticas (PDF)</a></p><p class="hint">Dos tarjetas A5 por hoja: delante, objetivo y pasos; detrás, pistas, bloques y «¿Y si…?». '
                  'Imprime a doble cara (borde largo) y corta por la línea discontinua.</p>',
    'experto': P('Proyectos más abiertos, organizados en cuatro bloques. Los dos últimos necesitan material: cables de cocodrilo y algunos sensores sencillos. Lo encontrarás indicado en cada proyecto.'),
    'talleres': P('Talleres cerrados de una o dos sesiones. En <b>Proyectos tipo</b> se construye un sistema completo con la placa y pocos componentes. En <b>Kits y robots</b> se usan productos concretos de ELECFREAKS y DFRobot con sus extensiones oficiales de MakeCode.'),
    'celebrar': P('Actividades cortas (de 15 a 45 minutos) para celebrar fechas especiales del curso con la micro:bit. Este apartado irá creciendo con nuevas fechas.'),
    'saber': P('Recursos para resolver dudas, evaluar y seguir aprendiendo.'),
    'errores': P('Cada programa tiene un fallo escondido. Pruébalo en el simulador, descubre qué falla y arréglalo. Encontrar y corregir errores (<b>depurar</b>) es una de las habilidades más importantes de la programación. '
                 'Se pueden hacer al terminar Comenzamos o intercaladas con sus prácticas.'),
    'matematicas': P('Actividades para trabajar las matemáticas con la micro:bit, organizadas por los sentidos del currículo. Cada una tiene simulador y solución en los tres editores.'),
    'ia': P('La inteligencia artificial también se aprende haciendo. Con <b>micro:bit CreateAI</b> el alumnado recoge datos de movimiento, entrena un modelo y lo usa en un programa.'),
    'imprime': P('Diseños imprimibles para proteger la placa y completar los proyectos.'),
}
GROUP_INFO = {}   # título de grupo -> (intro html)

def register_group(title, intro_html):
    GROUP_INFO[title] = intro_html
for mod in (c_comenzamos, c_experto, c_talleres, c_celebrar, c_conoce):
    for t, h in getattr(mod, 'GRUPOS', {}).items():
        register_group(t, h)

def slugify(t):
    t = t.lower()
    for a, b in zip('áéíóúñü', 'aeiounu'): t = t.replace(a, b)
    return re.sub(r'[^a-z0-9]+', '-', t).strip('-')

# ------------------------------------------------------------------ árbol
tree = []
for sid, *_ in SECTIONS:
    items, groups = [], {}
    for p in [p for p in PAGES if p['section'] == sid]:
        if p['group']:
            if p['group'] not in groups:
                g = dict(kind='group', title=p['group'], slug=slugify(p['group']), pages=[], section=sid)
                groups[p['group']] = g; items.append(g)
            groups[p['group']]['pages'].append(p)
        else:
            items.append(p)
    tree.append((sid, items))
TREE = dict(tree)

flat = []
for sid, items in tree:
    flat.append(dict(kind='section', section=sid, slug='index', title=SEC[sid][2]))
    for it in items:
        if it.get('kind') == 'group':
            flat.append(dict(kind='groupidx', section=sid, slug=it['slug'], title=it['title'], group=it))
            flat.extend(it['pages'])
        else:
            flat.append(it)

def label(p):
    if p.get('kind') == 'practica': return '%s · %s' % (p['meta']['num'], p['title'])
    return p['title']

def tag_of(p):
    m = p.get('meta', {})
    if p.get('kind') == 'practica': return 'Práctica %s · %s' % (m['num'], common.NIVEL[m['nivel']])
    if p.get('kind') == 'proyecto': return 'Proyecto · %s' % m.get('tiempo', '')
    if p.get('kind') == 'celebrar': return 'Actividades'
    return 'Lectura'

def card(p, href, tag=None, desc=''):
    ic = p.get('icono') or 'chip'
    return ('<a class="card" href="%s"><span class="card-ico">%s</span><span class="card-tag">%s</span><span class="card-t">%s</span>%s</a>'
            % (href, icon(ic, 26), e(tag or tag_of(p)), e(p['title']), ('<span class="card-d">%s</span>' % e(desc)) if desc else ''))

def section_body(sid):
    out = INTRO[sid] + '<div class="cards">'
    for it in TREE[sid]:
        if it.get('kind') == 'group':
            n = len(it['pages'])
            word = {'comenzamos': 'prácticas', 'experto': 'proyectos', 'talleres': 'talleres', 'celebrar': 'fechas'}.get(sid, 'páginas')
            ic = it['pages'][0].get('icono') or 'chip'
            out += ('<a class="card" href="%s.html"><span class="card-ico">%s</span><span class="card-tag">%d %s</span><span class="card-t">%s</span></a>'
                    % (it['slug'], icon(ic, 26), n, word, e(it['title'])))
        else:
            out += card(it, '%s.html' % it['slug'])
    return out + '</div>'

def group_body(g):
    body = GROUP_INFO.get(g['title'], '')
    return body + '<div class="cards">%s</div>' % ''.join(card(p, '%s.html' % p['slug']) for p in g['pages'])

# ------------------------------------------------------------------ plantilla
def nav_html(cur):
    out = '<nav class="side" aria-label="Contenidos"><a class="side-home" href="../index.html">%s Inicio</a>' % icon('inicio', 16)
    for sid, num, title, ic, _ in SECTIONS:
        op = cur and cur['section'] == sid
        out += '<details%s><summary><span class="num">%s</span> %s</summary><ul>' % (' open' if op else '', num, e(title))
        out += '<li><a href="../%s/index.html"%s>Presentación</a></li>' % (sid, ' class="on"' if op and cur['slug'] == 'index' else '')
        for it in TREE[sid]:
            if it.get('kind') == 'group':
                gopen = cur is not None and (cur.get('group') == it['title'] or cur.get('slug') == it['slug'])
                out += '<li><details%s><summary>%s</summary><ul><li><a href="../%s/%s.html"%s>Introducción</a></li>' % (
                    ' open' if gopen else '', e(it['title']), sid, it['slug'], ' class="on"' if cur is not None and cur.get('slug') == it['slug'] and cur.get('kind') == 'groupidx' else '')
                for p in it['pages']:
                    out += '<li><a href="../%s/%s.html"%s>%s</a></li>' % (sid, p['slug'], ' class="on"' if cur is p else '', e(label(p)))
                out += '</ul></details></li>'
            else:
                out += '<li><a href="../%s/%s.html"%s>%s</a></li>' % (sid, it['slug'], ' class="on"' if cur is it else '', e(label(it)))
        out += '</ul></details>'
    return out + '</nav>'

HEADER = ('<header class="top"><a class="brand" href="{root}index.html"><img src="{root}img/icono.svg?v=' + VER + '" alt="" width="38" height="38">'
          '<span class="brand-t">micro:bit <em class="lapiz">en el aula</em></span></a><button class="menu-btn" type="button" aria-label="Abrir el menú">☰</button>'
          '<nav class="topnav">{links}</nav></header>')
FOOTER = ('<footer class="foot"><p>© Pablo Moraga · Contenidos con licencia <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.es" target="_blank" rel="noopener">CC BY-NC-ND 4.0</a> · '
          '<a href="https://github.com/pablomoraga" target="_blank" rel="noopener">github.com/pablomoraga</a></p>'
          '<p class="small">Puedes compartir este material y sus programas tal cual, sin modificarlos, sin fines comerciales y citando siempre a su autor.</p>'
          '<p class="small">micro:bit es una marca de la Micro:bit Educational Foundation. MakeCode es un proyecto de Microsoft. MicroBlocks es un proyecto de código abierto '
          '(sus bibliotecas se distribuyen con licencia MPL 2.0). Este material es independiente y no está vinculado a ninguna de estas organizaciones ni a los fabricantes de los kits.</p></footer>')

LAPIZ = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true"><filter id="lapiz" x="-5%%" y="-10%%" width="110%%" height="120%%">'
         '<feTurbulence type="fractalNoise" baseFrequency=".55" numOctaves="2" seed="7" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="2.2"/></filter></svg>')

def doc(title, body, root, cur=None, pn=''):
    links = ''.join('<a href="%s%s/index.html">%s</a>' % (root, sid, e(t)) for sid, _, t, _, _ in SECTIONS)
    side = nav_html(cur) if cur is not None else ''
    return ('<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>%s · %s</title><meta name="description" content="Manual propio para aprender a programar la micro:bit V2 con MakeCode, MicroBlocks y Python en Primaria y ESO.">'
            '<link rel="icon" href="%simg/icono.svg?v=' + VER + '"><link rel="stylesheet" href="%scss/estilo.css?v=' + VER + '"></head><body>' + LAPIZ + '%s'
            '<div class="layout %s">%s<main id="contenido">%s%s</main></div>%s<script src="%sjs/app.js?v=' + VER + '"></script></body></html>') % (
        e(title), TITLE, root, root, HEADER.format(root=root, links=links), 'with-side' if side else 'home', side, body, pn, FOOTER, root)

def crumbs(p):
    out = '<p class="crumbs"><a href="../index.html">Inicio</a> › <a href="index.html">%s</a>' % e(SEC[p['section']][2])
    if isinstance(p.get('group'), str):
        out += ' › <a href="%s.html">%s</a>' % (slugify(p['group']), e(p['group']))
    return out + '</p>'

def prevnext(i):
    out = '<div class="pn">'
    if i > 0:
        q = flat[i - 1]; out += '<a class="pn-prev" href="../%s/%s.html">← %s</a>' % (q['section'], q['slug'], e(label(q) if q.get('kind') != 'section' else q['title']))
    else: out += '<span></span>'
    if i < len(flat) - 1:
        q = flat[i + 1]; out += '<a class="pn-next" href="../%s/%s.html">%s →</a>' % (q['section'], q['slug'], e(label(q) if q.get('kind') != 'section' else q['title']))
    return out + '</div>'

# ------------------------------------------------------------------ construir
def build():
    shutil.rmtree(SITE, ignore_errors=True)
    for d in ('css', 'js', 'img', 'programas/microblocks', 'programas/python'):
        os.makedirs(os.path.join(SITE, d), exist_ok=True)
    shutil.copy(os.path.join(HERE, 'estilo.css'), os.path.join(SITE, 'css', 'estilo.css'))
    shutil.copy(os.path.join(HERE, 'app.js'), os.path.join(SITE, 'js', 'app.js'))
    open(os.path.join(SITE, 'img', 'icono.svg'), 'w', encoding='utf-8').write(logo_lapiz())
    # páginas
    pages_html = []
    for i, p in enumerate(flat):
        if p['kind'] == 'section': body = '<p class="crumbs"><a href="../index.html">Inicio</a></p><h1>%s</h1>%s' % (e(p['title']), section_body(p['section']))
        elif p['kind'] == 'groupidx': body = crumbs(p) + '<h1>%s</h1>%s' % (e(p['title']), group_body(p['group']))
        else: body = crumbs(p) + '<h1>%s</h1>%s' % (e(p['title']), p['body'])
        pages_html.append((p, body, i))
    for p, body, i in pages_html:
        d = os.path.join(SITE, p['section']); os.makedirs(d, exist_ok=True)
        html_ = doc(p['title'], body.replace('{{ROOT}}', '../'), '../', p, prevnext(i))
        open(os.path.join(d, p['slug'] + '.html'), 'w', encoding='utf-8').write(html_)
    # portada
    cards = ''.join('<a class="card big" href="%s/index.html"><span class="card-ico">%s</span><span class="card-tag">%s</span><span class="card-t">%s</span><span class="card-d">%s</span></a>'
                    % (sid, icon(ic, 30), num, e(t), e(d)) for sid, num, t, ic, d in SECTIONS)
    npr = sum(1 for p in PAGES if p['kind'] == 'practica')
    nproj = sum(1 for p in PAGES if p['kind'] == 'proyecto')
    home = ('<section class="hero"><div class="hero-txt"><p class="kicker">Programación y robótica · Primaria y ESO</p><h1>micro:bit <em class=\"lapiz\">en el aula</em></h1>'
            '<p class="tagline">Bloques primero, texto después</p>'
            '<p class="lead">Un manual propio para aprender a programar la placa micro:bit V2 con <b>MakeCode</b>, <b>MicroBlocks</b> y <b>Python</b>: '
            'del primer LED encendido a juegos, sensores, robots y proyectos con kits.</p>'
            '<p><a class="btn" href="empezar/index.html">Empezar</a> <a class="btn btn2" href="comenzamos/index.html">Ir a las prácticas</a></p>'
            '<div class="stats"><span><b>%d</b> prácticas</span><span><b>%d</b> proyectos y talleres</span><span><b>3</b> editores</span></div></div>'
            '<div class="hero-img">%s</div></section>'
            '<section class="home-sec"><h2><span class="num">00</span> Contenidos</h2><div class="cards">%s</div></section>'
            '<section class="home-sec"><h2><span class="num">→</span> Cómo usar este material</h2><div class="tres">'
            '<div>%s<h3>Elige editor</h3><p>Cada solución aparece en MakeCode, MicroBlocks y Python. Elige una pestaña y la web la recordará.</p></div>'
            '<div>%s<h3>Avanza a tu ritmo</h3><p>Las prácticas van de menos a más. Marca las que termines: se guarda en tu navegador.</p></div>'
            '<div>%s<h3>Descarga y prueba</h3><p>Todos los programas se pueden copiar, descargar o abrir directamente en el editor.</p></div></div></section>') % (
        npr, nproj, placa_pro.hero(), cards, icon('bloques', 30), icon('trofeo', 30), icon('descarga', 30))
    open(os.path.join(SITE, 'index.html'), 'w', encoding='utf-8').write(doc('Inicio', home, '', None).replace('{{ROOT}}', ''))
    # programas
    for name, txt in common.UBP.items():
        open(os.path.join(SITE, 'programas', 'microblocks', name + '.ubp'), 'w', encoding='utf-8', newline='\n').write(txt)
    for name, txt in common.PY.items():
        open(os.path.join(SITE, 'programas', 'python', name + '.py'), 'w', encoding='utf-8', newline='\n').write(txt)
    est = os.path.join(HERE, 'estaticos')
    if os.path.isdir(est):
        shutil.copytree(est, SITE, dirs_exist_ok=True)
    open(os.path.join(SITE, '.nojekyll'), 'w').close()
    # MakeCode: lista de imágenes para el renderizador
    tarjetas.build_html(os.path.join(OUT, 'tarjetas-comenzamos.html'))
    json.dump(makecode.all_jobs(), open(os.path.join(OUT, 'makecode-pendientes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    falta = makecode.missing()
    # imágenes que ya no se usan
    usadas = set(makecode.REG)
    sobran = [f for f in os.listdir(makecode.IMG) if f.endswith('.webp') and f[:-5] not in usadas]
    return falta, sobran

if __name__ == '__main__':
    falta, sobran = build()
    print('páginas:', len(flat), '· prácticas:', sum(1 for p in PAGES if p['kind'] == 'practica'),
          '· programas MicroBlocks:', len(common.UBP), '· Python:', len(common.PY), '· MakeCode:', len(makecode.REG))
    if falta: print('AVISO: faltan %d imágenes de MakeCode. Ejecuta herramientas/renderizar_makecode.py' % len(falta))
    if sobran: print('Imágenes de MakeCode sin usar (se pueden borrar):', len(sobran))
