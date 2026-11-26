# -*- coding: utf-8 -*-
"""Crea imágenes PNG de los programas de MicroBlocks que llevan el programa dentro.
MicroBlocks lee el trozo de texto «script» de un PNG cuando se suelta en el editor y pega sus guiones
(cargando las bibliotecas de la línea «depends»), igual que hace con las imágenes que exporta él mismo.

Uso: python generador/build.py ; python herramientas/renderizar_microblocks.py ; abrir http://localhost:8792/ ;
     cuando termine, volver a construir la web. Opción --todo para regenerarlas todas."""
import base64, json, os, re, struct, sys, zlib
from http.server import HTTPServer, SimpleHTTPRequestHandler

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PEND = os.path.join(ROOT, '_salida', 'microblocks-pendientes.json')
DEST = os.path.join(ROOT, 'generador', 'estaticos', 'img', 'microblocks')
CSS_FILE = os.path.join(ROOT, 'generador', 'estilo.css')

def css_bloques():
    css = open(CSS_FILE, encoding='utf-8').read()
    reglas = re.findall(r'(\.mb-[^{]*\{[^}]*\})', css)
    return ':root{--paper:#fbfcfd}' + ''.join(reglas)

PAGE = r'''<!doctype html><html lang="es"><meta charset="utf-8"><title>Imágenes de MicroBlocks</title>
<style>body{font:14px system-ui;margin:20px}.zona{display:inline-block;padding:6px;background:transparent}%s</style>
<body><h1>Imágenes de MicroBlocks</h1><p id="st"></p><pre id="log"></pre><div id="out"></div>
<script>
const jobs = %s, CSS = %s;
const st = document.getElementById('st'), log = t => document.getElementById('log').textContent += t + '\n';
(async function () {
  let n = 0;
  for (const j of jobs) {
    const box = document.createElement('div'); box.className = 'zona'; box.innerHTML = j.html; document.getElementById('out').appendChild(box);
    await new Promise(r => requestAnimationFrame(r));
    const r = box.getBoundingClientRect(), w = Math.ceil(r.width), h = Math.ceil(r.height), k = 2;
    const xml = new XMLSerializer().serializeToString(box);
    const svg = '<svg xmlns="http://www.w3.org/2000/svg" width="' + w + '" height="' + h + '"><foreignObject width="100%%" height="100%%">' +
      '<div xmlns="http://www.w3.org/1999/xhtml"><style>' + CSS + '</style>' + xml + '</div></foreignObject></svg>';
    const img = new Image(); img.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg); await img.decode();
    const c = document.createElement('canvas'); c.width = w * k; c.height = h * k;
    const g = c.getContext('2d'); g.scale(k, k); g.drawImage(img, 0, 0);
    const resp = await fetch('/guardar', {method: 'POST', body: JSON.stringify({id: j.id, uri: c.toDataURL('image/png'), text: j.text})});
    n++; log(j.id + ' ' + (await resp.text())); st.textContent = n + ' / ' + jobs.length + (n === jobs.length ? ' · terminado ✓' : '');
    box.remove();
  }
  if (!jobs.length) st.textContent = 'No hay nada pendiente ✓';
})();
</script></body></html>'''

def add_text_chunk(png, key, text):
    data = key.encode('latin-1') + b'\x00' + text.encode('utf-8')
    chunk = struct.pack('>I', len(data)) + b'tEXt' + data + struct.pack('>I', zlib.crc32(b'tEXt' + data) & 0xffffffff)
    i = png.rindex(b'IEND') - 4          # antes del trozo IEND
    return png[:i] + chunk + png[i:]

def texto_guardado(path):
    """Texto «script» guardado en un PNG (None si no existe): sirve para saber si la imagen está al día."""
    if not os.path.exists(path):
        return None
    b = open(path, 'rb').read(); i = 8
    while i < len(b):
        n = struct.unpack('>I', b[i:i + 4])[0]; t = b[i + 4:i + 8]; d = b[i + 8:i + 8 + n]
        if t == b'tEXt' and d.startswith(b'script\x00'):
            return d[7:].decode('utf-8')
        i += 12 + n
    return None

class H(SimpleHTTPRequestHandler):
    def do_GET(self):
        jobs = json.load(open(PEND, encoding='utf-8')) if os.path.exists(PEND) else []
        if '--todo' not in sys.argv:
            jobs = [j for j in jobs if texto_guardado(os.path.join(DEST, j['id'] + '.png')) != j['text']]
        css = css_bloques()
        body = (PAGE % (css, json.dumps(jobs, ensure_ascii=False), json.dumps(css))).encode('utf-8')
        self.send_response(200); self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(body))); self.end_headers(); self.wfile.write(body)

    def do_POST(self):
        d = json.loads(self.rfile.read(int(self.headers['Content-Length'])).decode('utf-8'))
        png = base64.b64decode(d['uri'].split(',', 1)[1])
        os.makedirs(DEST, exist_ok=True)
        open(os.path.join(DEST, d['id'] + '.png'), 'wb').write(add_text_chunk(png, 'script', d['text']))
        body = b'guardado'
        self.send_response(200); self.send_header('Content-Length', str(len(body))); self.end_headers(); self.wfile.write(body)

    def log_message(self, *a): pass

if __name__ == '__main__':
    print('Abre http://localhost:8792/ (Ctrl+C para terminar)')
    HTTPServer(('127.0.0.1', 8792), H).serve_forever()
