# -*- coding: utf-8 -*-
"""Índice por conceptos: reúne las prácticas según las etiquetas de su ficha."""
import re
from common import page, FICHAS, PAGES, P, e

ALIAS = {'condicional': 'condicionales', 'reescalar': 'escalar valores', 'pines táctiles': 'táctil'}

def norm(c):
    c = c.strip().lower()
    return ALIAS.get(c, c)

def cslug(c):
    for a, b in zip('áéíóúñü', 'aeiounu'): c = c.replace(a, b)
    return 'c-' + re.sub(r'[^a-z0-9]+', '-', c).strip('-')

SEC_TXT = {'comenzamos': 'Comenzamos', 'experto': 'Modo experto', 'matematicas': 'Matemáticas', 'errores': 'Encuentra el error',
           'celebrar': 'Para celebrar', 'talleres': 'Talleres', 'ia': 'IA'}

CONOCIDOS = set()

def registrar():
    idx = {}
    for f in FICHAS:
        for c in f['conceptos']:
            idx.setdefault(norm(c), []).append(f)
    CONOCIDOS.update(cslug(c) for c in idx)
    orden = sorted(idx, key=lambda c: (-len(idx[c]), c))
    nube = ''.join('<a class="cpt" href="#%s" data-c="%s">%s<span>%d</span></a>' % (cslug(c), cslug(c), e(c), len(idx[c])) for c in orden)
    bloques = ''
    for c in sorted(idx):
        items = ''.join('<li><a href="../%s/%s.html"><b>%s</b> %s</a> <span class="hint">%s</span></li>' % (
            f['section'], f['slug'], e(f['num']), e(f['title']), SEC_TXT.get(f['section'], '')) for f in idx[c])
        bloques += '<section class="cpt-b" id="%s"><h3>%s <span class="hint">· %d</span></h3><ul>%s</ul></section>' % (cslug(c), e(c), len(idx[c]), items)
    body = (P('Pulsa un concepto para ver todas las prácticas que lo trabajan, o escribe para buscarlo. Los números indican cuántas prácticas hay.') +
            '<div class="cpt-f"><input type="search" id="cpt-q" placeholder="Busca un concepto: variables, radio, fracciones…" aria-label="Buscar concepto">'
            '<button type="button" class="btn-sec" id="cpt-todos">Ver todos</button></div>'
            '<div class="cpt-nube">%s</div><div class="cpt-lista">%s</div>') % (nube, bloques)
    page('saber', 'conceptos', 'Índice por conceptos', body, icono='lupa')
    nueva = PAGES.pop()
    i = next((k for k, q in enumerate(PAGES) if q['section'] == 'saber' and q['slug'] == 'glosario'), len(PAGES) - 1)
    PAGES.insert(i + 1, nueva)

def enlazar(html, root='../'):
    """Convierte las etiquetas de concepto de las fichas en enlaces al índice."""
    def f(m):
        sl = cslug(norm(m.group(1)))
        if sl not in CONOCIDOS: return m.group(0)
        return '<a class="chip chip-c" href="%ssaber/conceptos.html#%s">%s</a>' % (root, sl, m.group(1))
    return re.sub(r'<span class="chip chip-c">([^<]+)</span>', f, html)
