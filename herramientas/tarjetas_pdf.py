# -*- coding: utf-8 -*-
"""Convierte _salida/tarjetas-comenzamos.html en generador/estaticos/recursos/tarjetas-comenzamos.pdf con Chrome o Edge.
Uso: python generador/build.py && python herramientas/tarjetas_pdf.py && python generador/build.py"""
import os, subprocess, shutil
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = os.path.join(ROOT, '_salida', 'tarjetas-comenzamos.html')
dst = os.path.join(ROOT, 'generador', 'estaticos', 'recursos', 'tarjetas-comenzamos.pdf')
os.makedirs(os.path.dirname(dst), exist_ok=True)
cands = [r'C:\Program Files\Google\Chrome\Application\chrome.exe', r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
         shutil.which('google-chrome') or '', shutil.which('chromium') or '']
exe = next(c for c in cands if c and os.path.exists(c))
subprocess.run([exe, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', '--allow-file-access-from-files', '--virtual-time-budget=15000',
                '--print-to-pdf=' + dst, 'file:///' + src.replace('\\', '/')], check=True, capture_output=True, timeout=180)
print('PDF:', dst, os.path.getsize(dst) // 1024, 'KB')
