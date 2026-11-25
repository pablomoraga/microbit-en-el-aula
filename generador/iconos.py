# -*- coding: utf-8 -*-
"""Iconos propios de estilo electrónico (SVG de línea, 24 × 24, usan currentColor)."""

I = {
    # ---- electrónica
    'led': '<path d="M8 14V8a4 4 0 0 1 8 0v6"/><path d="M6 14h12"/><path d="M10 14v7M14 14v5"/><path d="M18 4l2-2M20 7h2M4 4L2 2M4 7H2"/>',
    'pulsador': '<rect x="4" y="9" width="16" height="10" rx="2"/><circle cx="12" cy="14" r="3"/><path d="M6 9V6M18 9V6M6 19v3M18 19v3"/>',
    'resistencia': '<path d="M2 12h4l1.5-4 3 8 3-8 3 8 1.5-4h4"/>',
    'chip': '<rect x="6" y="6" width="12" height="12" rx="2"/><rect x="9.5" y="9.5" width="5" height="5" rx="1"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>',
    'placa': '<rect x="2" y="4" width="20" height="14" rx="2.5"/><circle cx="7" cy="11" r="1.6"/><circle cx="17" cy="11" r="1.6"/><path d="M10 9h4M10 11h4M10 13h4"/><path d="M4 18v2M8 18v2M12 18v2M16 18v2M20 18v2"/>',
    'altavoz': '<path d="M4 9v6h4l5 4V5L8 9z"/><path d="M16.5 8.5a5 5 0 0 1 0 7M19 6a8.5 8.5 0 0 1 0 12"/>',
    'microfono': '<rect x="9" y="2.5" width="6" height="11" rx="3"/><path d="M5.5 11a6.5 6.5 0 0 0 13 0M12 17.5V21M8.5 21h7"/>',
    'antena': '<path d="M12 11v10M9 21h6"/><circle cx="12" cy="9" r="2"/><path d="M8 5.5a5 5 0 0 0 0 7M16 5.5a5 5 0 0 1 0 7M5.2 3a8.6 8.6 0 0 0 0 12M18.8 3a8.6 8.6 0 0 1 0 12"/>',
    'brujula': '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
    'termometro': '<path d="M14 14.8V5a2 2 0 0 0-4 0v9.8a4 4 0 1 0 4 0z"/><path d="M12 9v7"/>',
    'sol': '<circle cx="12" cy="12" r="4"/><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 17.3l1.8 1.8M4.9 19.1l1.8-1.8M17.3 6.7l1.8-1.8"/>',
    'bateria': '<rect x="2" y="7" width="17" height="10" rx="2"/><path d="M22 10.5v3M6 10v4M9.5 10v4"/>',
    'cocodrilo': '<path d="M2 15l6-6 11 2.5c1.6.4 2.5 1.6 2.5 3H11"/><path d="M2 15h9"/><path d="M10 11.5l1 3.5M13 12l1 3M16 12.6l.8 2.4"/><path d="M2 15v3"/>',
    'cable': '<path d="M4 20c0-6 5-6 8-8s4-6 4-8"/><rect x="13" y="1.5" width="6" height="4" rx="1"/><rect x="1.5" y="18.5" width="5" height="4" rx="1"/>',
    'sensor': '<circle cx="12" cy="12" r="2.5"/><path d="M7.8 7.8a6 6 0 0 0 0 8.4M16.2 7.8a6 6 0 0 1 0 8.4M5 5a10 10 0 0 0 0 14M19 5a10 10 0 0 1 0 14"/>',
    'motor': '<circle cx="11" cy="12" r="7"/><circle cx="11" cy="12" r="2"/><path d="M18 12h4M11 5v2M11 17v2M6 12h2"/>',
    'engranaje': '<circle cx="12" cy="12" r="3"/><path d="M12 2.5l1.6 2.7 3-.9.7 3 2.9 1.2-1.2 2.9 1.2 2.9-2.9 1.2-.7 3-3-.9L12 21.5l-1.6-2.7-3 .9-.7-3-2.9-1.2L5 12.6 3.8 9.7l2.9-1.2.7-3 3 .9z"/>',
    'servo': '<rect x="3" y="8" width="13" height="10" rx="2"/><circle cx="12" cy="13" r="2"/><path d="M12 11V3l7 2"/>',
    'usb': '<path d="M12 21V5M12 5l-2.5 3M12 5l2.5 3"/><path d="M12 16l-4-3V10M12 13l4-3V8"/><circle cx="8" cy="9" r="1.2"/><rect x="14.8" y="5.8" width="2.4" height="2.4"/><circle cx="12" cy="21" r="1"/>',
    'rayo': '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
    'onda': '<path d="M2 12c2-5 4-5 6 0s4 5 6 0 4-5 6 0"/>',
    'robot': '<rect x="5" y="8" width="14" height="10" rx="3"/><circle cx="9.5" cy="13" r="1.4"/><circle cx="14.5" cy="13" r="1.4"/><path d="M12 8V4.5"/><circle cx="12" cy="3.5" r="1"/><path d="M2.5 12v3M21.5 12v3M8 18v2.5M16 18v2.5"/>',
    'coche': '<rect x="3" y="7" width="18" height="9" rx="3"/><circle cx="7.5" cy="18" r="2.2"/><circle cx="16.5" cy="18" r="2.2"/><path d="M7 7V5h10v2"/><circle cx="7" cy="11.5" r="1"/><circle cx="17" cy="11.5" r="1"/>',
    'mando': '<path d="M7 7h10a5 5 0 0 1 4.8 6.4l-1 3.3a2.5 2.5 0 0 1-4.2 1L14.5 16h-5l-2.1 1.7a2.5 2.5 0 0 1-4.2-1l-1-3.3A5 5 0 0 1 7 7z"/><path d="M7.5 10v4M5.5 12h4"/><circle cx="16" cy="11" r=".8"/><circle cx="17.5" cy="13.2" r=".8"/>',
    'planta': '<path d="M12 21v-9"/><path d="M12 12C12 7 8 5 4 5c0 4 3 7 8 7zM12 14c0-4 3-6.5 7.5-6.5 0 4-3 6.5-7.5 6.5z"/><path d="M7 21h10"/>',
    'nube': '<path d="M7 18h10a4 4 0 0 0 .6-8A6 6 0 0 0 6 9.5 4.3 4.3 0 0 0 7 18z"/>',
    'gota': '<path d="M12 3s6 6.6 6 11a6 6 0 0 1-12 0c0-4.4 6-11 6-11z"/>',
    'casa': '<path d="M3 11l9-7 9 7"/><path d="M5 9.5V20h14V9.5"/><rect x="10" y="14" width="4" height="6"/>',
    'semaforo': '<rect x="7" y="2" width="10" height="20" rx="3"/><circle cx="12" cy="7" r="1.8"/><circle cx="12" cy="12" r="1.8"/><circle cx="12" cy="17" r="1.8"/>',
    'musica': '<path d="M9 18V5l11-2v13"/><circle cx="6.5" cy="18" r="2.5"/><circle cx="17.5" cy="16" r="2.5"/>',
    'dado': '<rect x="3.5" y="3.5" width="17" height="17" rx="3.5"/><circle cx="8.5" cy="8.5" r="1.1"/><circle cx="15.5" cy="15.5" r="1.1"/><circle cx="12" cy="12" r="1.1"/><circle cx="15.5" cy="8.5" r="1.1"/><circle cx="8.5" cy="15.5" r="1.1"/>',
    'corazon': '<path d="M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0 1 12 7.5 4.3 4.3 0 0 1 19.5 10c0 5.4-7.5 10-7.5 10z"/>',
    'matriz': '<rect x="3" y="3" width="18" height="18" rx="3"/><circle cx="8" cy="8" r="1"/><circle cx="12" cy="8" r="1"/><circle cx="16" cy="8" r="1"/><circle cx="8" cy="12" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="16" cy="12" r="1"/><circle cx="8" cy="16" r="1"/><circle cx="12" cy="16" r="1"/><circle cx="16" cy="16" r="1"/>',
    'acelerometro': '<path d="M12 3v18M3 12h18"/><path d="M12 3l-2 2.5M12 3l2 2.5M21 12l-2.5-2M21 12l-2.5 2"/><path d="M5 19l5-5"/><path d="M5 19h3M5 19v-3"/>',
    'tactil': '<path d="M9 11V5.5a1.5 1.5 0 0 1 3 0V10"/><path d="M12 10V8.5a1.5 1.5 0 0 1 3 0V11"/><path d="M15 11v-.5a1.5 1.5 0 0 1 3 0V15a6 6 0 0 1-6 6h-1a6 6 0 0 1-4.6-2.2L4 15.5a1.5 1.5 0 0 1 2.4-1.8L9 16"/>',
    # ---- didáctica / interfaz
    'bombilla': '<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2V16h5v-.1c0-.8.4-1.5 1-2A6 6 0 0 0 12 3z"/>',
    'aviso': '<path d="M12 3.5l9.5 16.5h-19z"/><path d="M12 10v4.5M12 17.2v.3"/>',
    'docente': '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2.7 9 2.7 12 0v-5M22 9v5"/>',
    'cohete': '<path d="M14 4c3-1.5 5.5-1 6.5-.5.5 1 1 3.5-.5 6.5l-6.5 6.5-6-6z"/><path d="M7.5 10.5L4 10l3-4h5M13.5 16.5L14 20l4-3v-5"/><circle cx="15.5" cy="8.5" r="1.4"/><path d="M6 15c-2 .5-2.5 2.5-2.5 5.5 3 0 5-.5 5.5-2.5"/>',
    'lupa': '<circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5L21 21"/>',
    'caja': '<path d="M3 7.5l9-4.5 9 4.5v9L12 21l-9-4.5z"/><path d="M3 7.5l9 4.5 9-4.5M12 12v9"/>',
    'pieza': '<path d="M9 4.5a2 2 0 0 1 4 0V6h4v4h-1.5a2 2 0 0 0 0 4H17v4h-4v-1.5a2 2 0 0 0-4 0V18H5v-4h1.5a2 2 0 0 0 0-4H5V6h4z"/>',
    'externo': '<path d="M14 4h6v6M20 4l-9 9"/><path d="M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/>',
    'descarga': '<path d="M12 3v12M7 10l5 5 5-5M4 20h16"/>',
    'reloj': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    'diana': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>',
    'salvavidas': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/><path d="M5.6 5.6l3.6 3.6M14.8 14.8l3.6 3.6M18.4 5.6l-3.6 3.6M9.2 14.8l-3.6 3.6"/>',
    'check': '<circle cx="12" cy="12" r="9"/><path d="M8 12.5l2.7 2.7L16 9.8"/>',
    'bloques': '<path d="M3 5h7l1 1.5h3L15 5h6v5H3z"/><path d="M3 12h9l1 1.5h3l1-1.5h4v5H3z"/>',
    'bloques2': '<rect x="3" y="4" width="18" height="6" rx="3"/><rect x="3" y="13" width="12" height="6" rx="3"/>',
    'codigo': '<path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/>',
    'libro': '<path d="M4 4.5A1.5 1.5 0 0 1 5.5 3H20v15H5.5A1.5 1.5 0 0 0 4 19.5z"/><path d="M4 19.5A1.5 1.5 0 0 0 5.5 21H20v-3"/>',
    'enlace': '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
    'lista': '<path d="M9 6h12M9 12h12M9 18h12"/><circle cx="4.5" cy="6" r="1.2"/><circle cx="4.5" cy="12" r="1.2"/><circle cx="4.5" cy="18" r="1.2"/>',
    'trofeo': '<path d="M8 4h8v5a4 4 0 0 1-8 0z"/><path d="M8 6H4.5c0 3 1.5 4.5 3.7 4.7M16 6h3.5c0 3-1.5 4.5-3.7 4.7M12 13v4M8 21h8M9.5 17h5v4h-5z"/>',
    'calendario': '<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/><circle cx="12" cy="15" r="1.4"/>',
    'estrella': '<path d="M12 3l2.7 5.6 6.1.8-4.5 4.2 1.1 6.1L12 16.8l-5.4 2.9 1.1-6.1L3.2 9.4l6.1-.8z"/>',
    'calabaza': '<path d="M12 7c-5 0-8 3-8 7s3 6 8 6 8-2 8-6-3-7-8-7z"/><path d="M12 7c-2 0-3 4-3 6.5S10 20 12 20s3-4 3-6.5S14 7 12 7z"/><path d="M12 7V4.5c0-1 .8-1.5 2-1.5"/>',
    'arbol': '<path d="M12 2.5l5 6.5h-2.5l4 5.5h-3l3.5 4.5h-14L8.5 14.5h-3l4-5.5H7z"/><path d="M12 19v3"/>',
    'matraz': '<path d="M9.5 3h5M10.5 3v6L4.8 18.6A1.6 1.6 0 0 0 6.2 21h11.6a1.6 1.6 0 0 0 1.4-2.4L13.5 9V3"/><path d="M7 15h10"/>',
    'playa': '<path d="M3 20c3-1.5 6-1.5 9 0s6 1.5 9 0"/><path d="M12 17L8 6"/><path d="M8 6c2.5-3 7.5-2.5 9.5 1L8 6c-3-.5-5.5 1.5-5.5 4z"/>',
    'inicio': '<path d="M4 11l8-7 8 7v9h-5v-6H9v6H4z"/>',
    'flecha': '<path d="M5 12h14M13 6l6 6-6 6"/>',
    'puzle': '<rect x="3" y="3" width="8" height="8" rx="2"/><rect x="13" y="3" width="8" height="8" rx="2"/><rect x="3" y="13" width="8" height="8" rx="2"/><rect x="13" y="13" width="8" height="8" rx="4"/>',
    'cerebro': '<path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-2 5 3 3 0 0 0 2 5 3 3 0 0 0 3 3h1V4z"/><path d="M15 4a3 3 0 0 1 3 3 3 3 0 0 1 2 5 3 3 0 0 1-2 5 3 3 0 0 1-3 3h-1V4z"/><path d="M10 9H8M14 9h2M10 14H7.5M14 14h2.5"/>',
}

def icon(name, size=22, cls='ico'):
    return ('<svg class="%s" width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (cls, size, size, I[name]))

def svg_file(name, color='#1d2b3a', bg=None, size=24):
    """Icono como archivo SVG independiente (favicon y similares)."""
    rect = '<rect width="24" height="24" rx="6" fill="%s"/>' % bg if bg else ''
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 24 24">%s<g fill="none" stroke="%s" stroke-width="1.8" '
            'stroke-linecap="round" stroke-linejoin="round">%s</g></svg>' % (size, size, rect, color, I[name]))

def logo_lapiz(size=64):
    """Logotipo: una micro:bit dibujada a lápiz sobre fondo naranja."""
    g = '#2a1a14'
    def doble(d, w=1.6, o=.9):
        # cada trazo se repasa dos veces, ligeramente desplazado, como a lápiz
        return ('<path d="%s" stroke="%s" stroke-width="%s" opacity="%s"/>'
                '<path d="%s" stroke="%s" stroke-width="%.1f" opacity=".45" transform="translate(.7 -.5) rotate(.6 32 32)"/>' % (d, g, w, o, d, g, w * .7))
    body = doble('M12 18 Q11 17 13 16 H51 Q53 16 53 18 V44 H11 V19', 2)
    body += doble('M13 44 V50 M19 44 V50 M25 44 V50 M31 44 V50 M37 44 V50 M43 44 V50 M49 44 V50', 1.3, .8)
    body += doble('M17 31 a3.3 3.3 0 1 0 6.6 0 a3.3 3.3 0 1 0 -6.6 0 M40.4 31 a3.3 3.3 0 1 0 6.6 0 a3.3 3.3 0 1 0 -6.6 0', 1.6)
    body += doble('M27 21 h10 a3 3 0 0 1 0 6 h-10 a3 3 0 0 1 0 -6z', 1.3, .85)
    dots = ''.join('<circle cx="%d" cy="%d" r="1.15" fill="%s"/>' % (28 + c * 2.8, 30 + r * 2.8, g) for r in range(5) for c in range(5)
                   if (r, c) in {(0, 1), (0, 3), (1, 0), (1, 2), (1, 4), (2, 0), (2, 4), (3, 1), (3, 3), (4, 2)})
    hatch = ''.join('<path d="M%d 44 l6 -6" stroke="%s" stroke-width=".7" opacity=".35"/>' % (x, g) for x in range(14, 50, 3))
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 64 64">'
            '<defs><filter id="l" x="-5%%" y="-5%%" width="110%%" height="110%%"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="3" result="n"/>'
            '<feDisplacementMap in="SourceGraphic" in2="n" scale="1.4"/></filter></defs>'
            '<rect width="64" height="64" rx="15" fill="#ff5a36"/><rect x="3" y="3" width="58" height="58" rx="12" fill="none" stroke="#fff" stroke-opacity=".35" stroke-dasharray="3 2"/>'
            '<g fill="none" stroke-linecap="round" stroke-linejoin="round" filter="url(#l)">%s%s%s</g></svg>' % (size, size, body, hatch, dots))
