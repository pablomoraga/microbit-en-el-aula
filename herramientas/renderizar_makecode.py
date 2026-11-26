# -*- coding: utf-8 -*-
"""Convierte en imágenes WebP los bloques de MakeCode que usa la web.

Uso (desde la carpeta del proyecto):
    1. python generador/build.py           -> crea _salida/makecode-pendientes.json
    2. python herramientas/renderizar_makecode.py
    3. Abre http://localhost:8791/ en Chrome o Edge y espera a que termine.
    4. Vuelve a construir la web: python generador/build.py

Las imágenes las dibuja el propio MakeCode (makecode.microbit.org) en español y se guardan en
generador/estaticos/img/makecode/. Solo se renderizan los programas nuevos o cambiados."""
import base64, json, os, sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PEND = os.path.join(ROOT, '_salida', 'makecode-pendientes.json')
DEST = os.path.join(ROOT, 'generador', 'estaticos', 'img', 'makecode')
TEXTS = os.path.join(ROOT, '_salida', 'makecode-textos.json')

PAGE = r'''<!doctype html><html lang="es"><meta charset="utf-8"><title>Renderizar MakeCode</title>
<body style="font:14px system-ui;margin:20px"><h1>Renderizando bloques de MakeCode</h1><p id="st">Cargando MakeCode…</p><pre id="log"></pre><div id="out"></div>
<script>
const jobs = %s;
const st = document.getElementById('st'), log = t => document.getElementById('log').textContent += t + '\n';
let done = 0, sent = 0, ready = false;
const f = document.createElement('iframe'); f.style.display = 'none';
f.src = 'https://makecode.microbit.org/--docs?render=1&forcelang=es'; document.body.appendChild(f);
function next() {
  if (sent >= jobs.length) return;
  const j = jobs[sent++];
  const opts = {}; if (j.pkg) opts.package = j.pkg;
  f.contentWindow.postMessage({type: 'renderblocks', id: j.id, code: j.code, options: opts}, '*');
}
window.addEventListener('message', async ev => {
  const m = ev.data; if (!m || !m.type) return;
  if (m.type === 'renderready' && !ready) { ready = true; st.textContent = 'Preparando extensiones…';
    // calentamiento: carga cada extensión con un programa mínimo antes de los trabajos reales
    const pk = [...new Set(jobs.map(j => j.pkg).filter(Boolean))];
    pk.forEach((p, i) => f.contentWindow.postMessage({type: 'renderblocks', id: 'warm' + i, code: 'basic.showNumber(0)', options: {package: p}}, '*'));
    setTimeout(() => { st.textContent = 'Renderizando ' + jobs.length + ' programas…'; for (let i = 0; i < 3; i++) next(); }, pk.length ? 8000 : 0); }
  if (m.type === 'renderblocks' && String(m.id).startsWith('warm')) return;
  if (m.type === 'renderblocks') {
    const texts = []; const tmp = document.createElement('div'); tmp.innerHTML = m.svg || '';
    tmp.querySelectorAll('text').forEach(t => texts.push(t.textContent));
    let uri = '';
    if (m.uri) {
      const img = new Image(); img.src = m.uri; await img.decode();
      const c = document.createElement('canvas'); c.width = Math.round(m.width * 2); c.height = Math.round(m.height * 2);
      const g = c.getContext('2d'); g.fillStyle = '#fff'; g.fillRect(0, 0, c.width, c.height);
      g.imageSmoothingQuality = 'high'; g.drawImage(img, 0, 0, c.width, c.height);
      uri = c.toDataURL('image/webp', 0.9);
    }
    const r = await fetch('/guardar', {method: 'POST', body: JSON.stringify({id: m.id, uri, texts, error: m.error || '', w: m.width, h: m.height})});
    done++; log(m.id + ' ' + (m.uri ? 'ok' : 'ERROR ' + (m.error || '')) + ' ' + (await r.text()));
    st.textContent = done + ' / ' + jobs.length + (done === jobs.length ? ' · terminado ✓' : '');
    next();
  }
});
if (!jobs.length) st.textContent = 'No hay nada pendiente ✓';
</script></body></html>'''

class H(SimpleHTTPRequestHandler):
    def do_GET(self):
        jobs = json.load(open(PEND, encoding='utf-8')) if os.path.exists(PEND) else []
        if '--todo' not in sys.argv:
            jobs = [j for j in jobs if not os.path.exists(os.path.join(DEST, j['id'] + '.webp'))]
        body = (PAGE % json.dumps(jobs)).encode('utf-8')
        self.send_response(200); self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(body))); self.end_headers(); self.wfile.write(body)

    def do_POST(self):
        data = json.loads(self.rfile.read(int(self.headers['Content-Length'])).decode('utf-8'))
        msg = 'sin imagen'
        if data['uri'].startswith('data:image/webp;base64,'):
            os.makedirs(DEST, exist_ok=True)
            open(os.path.join(DEST, data['id'] + '.webp'), 'wb').write(base64.b64decode(data['uri'].split(',', 1)[1]))
            msg = 'guardado'
        allt = json.load(open(TEXTS, encoding='utf-8')) if os.path.exists(TEXTS) else {}
        allt[data['id']] = dict(texts=data['texts'], error=data['error'], w=data['w'], h=data['h'])
        json.dump(allt, open(TEXTS, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        body = msg.encode('utf-8')
        self.send_response(200); self.send_header('Content-Length', str(len(body))); self.end_headers(); self.wfile.write(body)

    def log_message(self, *a): pass

if __name__ == '__main__':
    print('Abre http://localhost:8791/ en el navegador (Ctrl+C para terminar)')
    HTTPServer(('127.0.0.1', 8791), H).serve_forever()
