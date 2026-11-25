# -*- coding: utf-8 -*-
"""MicroBlocks: lee programas escritos en el formato de texto de MicroBlocks (el mismo de los .ubp),
los dibuja como bloques en español y genera el archivo .ubp con las bibliotecas que necesita.

Los nombres de los bloques salen de la traducción oficial (microblocks/es.po) y las especificaciones,
de las primitivas del compilador y de las bibliotecas oficiales (carpeta microblocks/bibliotecas)."""
import os, re, html, glob

HERE = os.path.dirname(os.path.abspath(__file__))
MB = os.path.join(HERE, 'microblocks')
e = html.escape

COLOR = {'Output': '#4852BF', 'Input': '#9F42A5', 'Pins': '#548799', 'Comm': '#1E997A', 'Control': '#D18C25',
         'Operators': '#479D1D', 'Variables': '#D3732A', 'Data': '#C44E6B', 'My Blocks': '#1A8CDD'}

# ------------------------------------------------------------------ traducción
def _load_po():
    t = open(os.path.join(MB, 'es.po'), encoding='utf-8').read()
    out = {}
    for m in re.finditer(r'msgid ((?:"(?:[^"\\]|\\.)*"\s*)+)msgstr ((?:"(?:[^"\\]|\\.)*"\s*)+)', t):
        k = ''.join(re.findall(r'"((?:[^"\\]|\\.)*)"', m.group(1)))
        v = ''.join(re.findall(r'"((?:[^"\\]|\\.)*)"', m.group(2)))
        if k and v:
            out[k.replace('\\"', '"')] = v.replace('\\"', '"')
    return out
PO = _load_po()

def tr(s):
    return PO.get(s) or PO.get(s.strip()) or s

# ------------------------------------------------------------------ especificaciones
SPECS = {}      # op -> dict(kind, spec, types, cat, lib)
LIBS = {}       # nombre -> dict(text, depends, cat)

def _tokens_line(line):
    return re.findall(r"'(?:[^']|'')*'|\S+", line)

def _unq(t):
    return t[1:-1].replace("''", "'") if t.startswith("'") else t

def _load_specs():
    cat = None
    for line in open(os.path.join(MB, 'primitivas.gp.txt'), encoding='utf-8'):
        m = re.match(r"\s*'cat;([A-Za-z ]+?)(?:-Advanced)?'", line)
        if m: cat = m.group(1); continue
        m = re.match(r"\s*'Prims-([A-Za-z]+)", line)
        if m: cat = {'Display': 'Output', 'Sensing': 'Input'}.get(m.group(1), 'Control'); continue
        m = re.match(r"\s*\(array (.*)\)\s*$", line)
        if m:
            tk = [_unq(x) for x in _tokens_line(m.group(1))]
            if len(tk) >= 3:
                SPECS.setdefault(tk[1], dict(kind=tk[0], spec=tk[2], types=(tk[3].split() if len(tk) > 3 else []), cat=cat, lib=None))
    for f in sorted(glob.glob(os.path.join(MB, 'bibliotecas', '*.ubl'))):
        text = open(f, encoding='utf-8').read()
        first = _tokens_line(text.splitlines()[0])
        name = _unq(first[1]); lcat = first[2] if len(first) > 2 else 'Output'
        deps = []
        for line in text.splitlines():
            if line.startswith('depends'):
                deps = [_unq(x).lstrip('_') for x in _tokens_line(line)[1:]]
            m = re.match(r"\s*spec '(.)' (.*)$", line)
            if m:
                tk = [_unq(x) for x in _tokens_line(m.group(2))]
                SPECS[tk[0]] = dict(kind=m.group(1).replace(' ', ' '), spec=tk[1], types=(tk[2].split() if len(tk) > 2 else []), cat=lcat, lib=name)
        LIBS[name] = dict(text=text.rstrip() + '\n', depends=deps, cat=lcat)
_load_specs()
INFIX = {'+', '-', '*', '/', '%', '<', '>', '<=', '>=', '==', '!=', '&', '|', '^', '<<', '>>'}

# ------------------------------------------------------------------ análisis del texto
class N:
    """Nodo: op (str), args (lista de N | ('num'|'str'|'var'|'bool', valor) | lista de N para bloques C)."""
    def __init__(self, op, args): self.op, self.args = op, args

def _tokenize(src):
    toks, i = [], 0
    while i < len(src):
        c = src[i]
        if c == '\n': toks.append('\n'); i += 1
        elif c.isspace(): i += 1
        elif c in '(){}': toks.append(c); i += 1
        elif c == "'":
            j = i + 1; buf = ''
            while True:
                if src[j] == "'" and j + 1 < len(src) and src[j + 1] == "'": buf += "'"; j += 2
                elif src[j] == "'": break
                else: buf += src[j]; j += 1
            toks.append(('s', buf)); i = j + 1
        else:
            j = i
            while j < len(src) and not src[j].isspace() and src[j] not in '(){}': j += 1
            toks.append(src[i:j]); i = j
    return toks

class _P:
    def __init__(self, toks): self.t, self.i = toks, 0
    def peek(self): return self.t[self.i] if self.i < len(self.t) else None
    def nxt(self): v = self.t[self.i]; self.i += 1; return v
    def items(self, stop):
        out = []
        while self.peek() is not None and self.peek() not in stop:
            t = self.nxt()
            if t == '(':
                out.append(('expr', self.items({')'}))); self.nxt()
            elif t == '{':
                out.append(('block', self.stmts())); self.nxt()
            else:
                out.append(t)
        return out
    def stmts(self):
        out = []
        while True:
            while self.peek() == '\n': self.nxt()
            if self.peek() in (None, '}'): return out
            out.append(_stmt(self.items({'\n', '}'})))

def _atom(it):
    if isinstance(it, tuple):
        if it[0] == 's': return ('str', it[1])
        if it[0] == 'expr': return _expr(it[1])
        if it[0] == 'block': return it[1]
    if re.fullmatch(r'-?\d+(\.\d+)?', it): return ('num', it)
    if it in ('true', 'false'): return ('bool', it)
    return ('var', it)

def _name(it): return it[1] if isinstance(it, tuple) else it

def _expr(items):
    if len(items) == 3 and isinstance(items[1], str) and items[1] in INFIX:
        return N(items[1], [_atom(items[0]), _atom(items[2])])
    if len(items) == 1 and isinstance(items[0], str) and items[0] not in SPECS:
        return _atom(items[0])
    return N(_name(items[0]), [_atom(x) for x in items[1:]])

def _stmt(items):
    if len(items) >= 3 and items[1] in ('=', '+='):
        return N(items[1], [('var', items[0]), _atom(items[2])])
    return N(_name(items[0]), [_atom(x) for x in items[1:]])

def parse(src):
    """Devuelve una lista de guiones; cada guion es una lista de nodos."""
    p = _P(_tokenize(src))
    scripts = []
    for st in p.stmts():
        scripts.append(st)
    return scripts

def parse_program(src):
    """El programa se escribe como varios guiones separados por una línea con ---."""
    return [parse(part.strip() + '\n') for part in re.split(r'\n---+\n', src.strip())]

# ------------------------------------------------------------------ dibujo
def _label_parts(spec):
    parts = spec.split(' : ')
    out = [tr(parts[0])]
    for p in parts[1:]:
        out.append(tr(p))
    return out

def _grid(val):
    try: n = int(val)
    except Exception: n = 0
    cells = ''.join('<i class="%s"></i>' % ('on' if (n >> i) & 1 else '') for i in range(25))
    return '<span class="mb-grid">%s</span>' % cells

def _arg(a, typ):
    if isinstance(a, N):
        return render_node(a, inline=True)
    if isinstance(a, list):
        return ''
    k, v = a
    if k == 'menuvar':
        return '<span class="mb-menu">%s ▾</span>' % e(v)
    if k == 'var':
        return '<span class="mb-rep" style="background:%s">%s</span>' % (COLOR['Variables'], e(v))
    if typ == 'microbitDisplay':
        return _grid(v)
    if typ and typ.startswith('menu') or (typ and '.' in typ and typ.split('.')[0] in ('str', 'auto') and k == 'str' and ';' in v):
        return '<span class="mb-menu">%s ▾</span>' % e(tr(v) if ';' in v else tr(v))
    if k == 'bool' or typ == 'bool':
        on = v in ('true', True)
        return '<span class="mb-bool %s">%s</span>' % ('on' if on else 'off', '' )
    if k == 'num':
        return '<span class="mb-num">%s</span>' % e(v)
    return '<span class="mb-str">%s</span>' % e(tr(v) if ';' in v else v)

def _fill(spec, types, args, color):
    """Rellena los huecos «_» del texto traducido con los argumentos."""
    parts = spec.split(' : ')
    ai = 0
    lines = [[]]
    cblocks = []
    for pi, part in enumerate(parts):
        if part == '...': break
        nslots = part.count('_')
        if pi > 0 and ai >= len(args): break
        text = tr(part)
        if text.count('_') != nslots: text = part
        pieces = re.split(r'(_|#BR#)', text)
        for pc in pieces:
            if pc == '_':
                typ = types[ai] if ai < len(types) else ''
                a = args[ai] if ai < len(args) else None
                ai += 1
                if isinstance(a, list) or typ == 'cmd':
                    cblocks.append(a if isinstance(a, list) else [])
                    lines.append('C')
                    lines.append([])
                elif a is not None:
                    lines[-1].append(_arg(a, typ))
            elif pc == '#BR#':
                lines.append([])
            elif pc.strip():
                lines[-1].append('<span class="mb-t">%s</span>' % e(pc.strip()))
    return lines, cblocks

def _wrap_lines(lines, cblocks, color, kind):
    out = ''
    ci = 0
    for ln in lines:
        if ln == 'C':
            out += '<div class="mb-in">%s</div>' % render_stack(cblocks[ci]); ci += 1
        elif ln:
            out += '<div class="mb-line">%s</div>' % ''.join(ln)
    return out

def render_node(n, inline=False):
    if not isinstance(n, N):
        return _arg(n, '')
    op = n.op
    if op in ('=', '+='):
        spec = 'set _ to _' if op == '=' else 'change _ by _'
        color = COLOR['Variables']
        lines, cb = _fill(spec, ['menu.var', 'auto'], [('menuvar', n.args[0][1])] + n.args[1:], color)
        return '<div class="mb-blk" style="background:%s">%s</div>' % (color, _wrap_lines(lines, cb, color, ' '))
    if op == 'if':
        color = COLOR['Control']
        out = ''
        args = n.args
        i = 0
        first = True
        while i < len(args):
            if isinstance(args[i], tuple) and args[i] == ('var', 'else'):
                out += '<div class="mb-line"><span class="mb-t">%s</span></div><div class="mb-in">%s</div>' % ('si no', render_stack(args[i + 1]))
                i += 2; continue
            word = 'si' if first else 'si no, si'
            out += '<div class="mb-line"><span class="mb-t">%s</span>%s</div><div class="mb-in">%s</div>' % (
                e(word), _arg(args[i], 'bool'), render_stack(args[i + 1] if i + 1 < len(args) else []))
            first = False; i += 2
        return '<div class="mb-blk mb-c" style="background:%s">%s<div class="mb-end"></div></div>' % (color, out)
    sp = SPECS.get(op)
    if sp is None:
        if op in INFIX:
            sym = {'*': '×', '-': '−', '==': '=', '!=': '≠', '%': tr('mod')}.get(op, op)
            sp = dict(kind='r', spec='_ %s _' % sym, types=['num', 'num'], cat='Operators')
        else:
            raise KeyError('MicroBlocks: bloque desconocido «%s»' % op)
    color = COLOR.get(sp['cat'], COLOR['My Blocks'])
    if op in INFIX or op in ('and', 'or', 'not'): color = COLOR['Operators']
    lines, cb = _fill(sp['spec'], sp['types'], n.args, color)
    body = _wrap_lines(lines, cb, color, sp['kind'])
    if sp['kind'] == 'r':
        boolish = op in INFIX and op in ('<', '>', '<=', '>=', '==', '!=') or op in ('and', 'or', 'not', 'buttonA', 'buttonB') or sp['spec'].endswith('?')
        return '<span class="mb-rep%s" style="background:%s">%s</span>' % (' mb-hex' if boolish else '', color, body.replace('<div class="mb-line">', '').replace('</div>', ''))
    cls = 'mb-blk'
    if sp['kind'] == 'h': cls += ' mb-hat'
    if cb: cls += ' mb-c'
    return '<div class="%s" style="background:%s">%s%s</div>' % (cls, color, body, '<div class="mb-end"></div>' if cb else '')

def render_stack(nodes):
    return ''.join(render_node(n) for n in nodes)

def render(src):
    """HTML de un programa (varios guiones lado a lado)."""
    scripts = parse_program(src)
    return '<div class="mb-prog">%s</div>' % ''.join('<div class="mb-script">%s</div>' % render_stack(sc) for sc in scripts)

# ------------------------------------------------------------------ .ubp
def _walk(x):
    if isinstance(x, N):
        yield x
        for a in x.args: yield from _walk(a)
    elif isinstance(x, list):
        for a in x: yield from _walk(a)

def ubp(src, description=''):
    scripts = parse_program(src)
    ops, gvars = set(), []
    for sc in scripts:
        for n in _walk(sc):
            ops.add(n.op)
            if n.op in ('=', '+=') and n.args[0][1] not in gvars:
                gvars.append(n.args[0][1])
            if n.op not in SPECS and n.op not in INFIX and n.op not in ('=', '+=', 'if'):
                raise KeyError('MicroBlocks: bloque desconocido «%s»' % n.op)
    libs = []
    def need(name):
        if name in LIBS and name not in libs:
            libs.append(name)
            for d in LIBS[name]['depends']: need(d)
    for op in sorted(ops):
        sp = SPECS.get(op)
        if sp and sp['lib']: need(sp['lib'])
    out = ["module main", "author 'Pablo Moraga'", "version 1 0 ", "description '%s'" % description.replace("'", "''")]
    if gvars: out.append('variables ' + ' '.join(gvars) + ' ')
    out.append('')
    y = 50
    for sc in scripts:
        body = '\n'.join(p.strip() for p in re.split(r'\n---+\n', src.strip()))
    parts = re.split(r'\n---+\n', src.strip())
    for i, part in enumerate(parts):
        out.append('script %d %d {' % (50 + (i % 2) * 420, 50 + (i // 2) * 320))
        out.append(part.strip())
        out.append('}')
        out.append('')
    out.append('')
    for name in libs:
        out.append(LIBS[name]['text'])
        out.append('')
    return '\n'.join(out)

def used_libraries(src):
    scripts = parse_program(src)
    names = []
    for sc in scripts:
        for n in _walk(sc):
            sp = SPECS.get(n.op)
            if sp and sp['lib'] and sp['lib'] not in names: names.append(sp['lib'])
    return names
