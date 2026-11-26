# -*- coding: utf-8 -*-
"""Escenas en perspectiva de los proyectos de Talleres (dibujos propios con iso.Escena)."""
from iso import Escena, mix
from placa import CORAZON, SONRISA

SI = {(1, 4), (2, 3), (3, 0), (3, 2), (4, 1)}               # marca de verificación
NO = {(0, 0), (0, 4), (1, 1), (1, 3), (2, 2), (3, 1), (3, 3), (4, 0), (4, 4)}
GOTA = {(0, 2), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3)}
CARTON = '#c9a36b'

def _planta(s, u, v, z):
    x, y = s.P(u, v, z)
    hojas = ''
    for dx, dy, r, rot in ((-30, -40, 30, -30), (28, -48, 32, 30), (0, -78, 34, 0), (-42, -14, 24, -50), (40, -18, 24, 50)):
        hojas += '<ellipse cx="%.1f" cy="%.1f" rx="%d" ry="%d" fill="#2e9d4f" transform="rotate(%d %.1f %.1f)"/>' % (x + dx, y + dy, r * .55, r, rot, x + dx, y + dy)
    s.add('<path d="M%.1f %.1f V%.1f" stroke="#2b7a3e" stroke-width="5"/>' % (x, y, y - 70) + hojas)

def invernadero():
    s = Escena(760, 520, s=0.46)
    s.caja(-80, -60, 1260, 860, 18, '#e9dcc0', sombra=False, tapa='#efe4cc')
    z0 = 18
    u, v, w, d, h = 0, 0, 520, 380, 300
    s.sombra(u, v, w, d)
    # paredes del fondo
    s.add(s.poly([(u, v, z0), (u + w, v, z0), (u + w, v, z0 + h), (u, v, z0 + h)], '#cfeee4', ' opacity=".55" stroke="#0f8a72" stroke-width="2"'))
    s.add(s.poly([(u, v, z0), (u, v + d, z0), (u, v + d, z0 + h), (u, v, z0 + h)], '#cfeee4', ' opacity=".45" stroke="#0f8a72" stroke-width="2"'))
    # maceta con tierra, clavos y planta
    s.cilindro(250, 200, 95, 120, '#b5653a', z=z0, tapa='#6b4226')
    for cu, cv in ((230, 186), (272, 212)):
        s.add(s.poly([(cu, cv, z0 + 120), (cu + 6, cv, z0 + 120), (cu + 6, cv, z0 + 200), (cu, cv, z0 + 200)], '#9aa1aa'))
    _planta(s, 250, 200, z0 + 120)
    # servo y ventana del techo, abierta
    s.caja(380, 20, 90, 60, 50, '#2e78d6', z=z0 + h - 50, sombra=False)
    s.add(s.poly([(u, v, z0 + h), (u + w, v, z0 + h), (u + w, v + d * .8, z0 + h + 160), (u, v + d * .8, z0 + h + 160)], '#bfe6da', ' opacity=".6" stroke="#0f8a72" stroke-width="2"'))
    # paredes delanteras transparentes
    s.add(s.poly([(u, v + d, z0), (u + w, v + d, z0), (u + w, v + d, z0 + h), (u, v + d, z0 + h)], '#dff5ee', ' opacity=".35" stroke="#0f8a72" stroke-width="2.5"'))
    s.add(s.poly([(u + w, v, z0), (u + w, v + d, z0), (u + w, v + d, z0 + h), (u + w, v, z0 + h)], '#dff5ee', ' opacity=".3" stroke="#0f8a72" stroke-width="2.5"'))
    # micro:bit a la derecha: los cables salen del conector hacia delante y van al invernadero
    mu, mv, mw = 680, 300, 320
    s.microbit(mu, mv, mw, z=z0, lit=GOTA, uid='inv')
    for anillo, col, fin in (('P1', '#2e78d6', (480, 400)), ('3V', '#c0392b', (500, 410)), ('P0', '#ef7d1a', (520, 300))):
        a = s.anillo(mu, mv, mw, anillo)
        s.cable((a[0], a[1] + 50), fin, col, z=z0 + 5, grosor=10, curva=200)
        s.pinza(a[0], a[1], col, z=z0 + 10, largo=60)
    s.punto(mu + 160, mv + 120, z0 + 14, 'micro:bit', 'Mide la temperatura y lee la humedad. Muestra una gota cuando hay que regar.')
    s.punto(250, 200, z0 + 200, 'Clavos de humedad', 'Clavados en la tierra: uno a 3V y el otro a P1.')
    s.punto(425, 50, z0 + h, 'Servo de la ventana', 'Conectado a P0: abre el techo si hace más de 28 °C.')
    s.punto(120, 280, z0 + h + 120, 'Ventana', 'Se cierra al bajar de 24 °C.')
    return s.figura('Invernadero inteligente (esquema en perspectiva)')

def estacion():
    s = Escena(760, 480, s=0.42, x0=250, y0=120)
    s.caja(-60, -40, 1180, 720, 16, '#e9dcc0', sombra=False, tapa='#efe4cc')
    z0 = 16
    # garita de la estación (caja ventilada) con la placa encima
    s.caja(40, 120, 300, 260, 220, '#f2f2f2', z=z0, borde='#9aa1aa')
    for i in range(5):
        s.add(s.poly([(60 + i * 0, 380, z0 + 40 + i * 34), (320, 380, z0 + 40 + i * 34), (320, 380, z0 + 50 + i * 34), (60, 380, z0 + 50 + i * 34)], '#c9ced6'))
    s.microbit(60, 140, 260, z=z0 + 220, lit={(0, 2), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (4, 2)}, uid='est1')
    s.ondas(190, 250, z0 + 300, color='#e3008c')
    # panel en el aula
    s.microbit(720, 260, 300, z=z0, lit=SONRISA, uid='est2')
    s.ondas(870, 360, z0 + 60, color='#e3008c')
    s.punto(190, 260, z0 + 240, 'Estación', 'Mide temperatura, luz y ruido y lo envía por radio cada 5 segundos.')
    s.punto(270, 380, z0 + 120, 'Garita ventilada', 'Protege la placa del sol directo y deja pasar el aire.')
    s.punto(870, 380, z0 + 20, 'Panel en el aula', 'Recibe los datos (grupo de radio 10) y los muestra con A, B y el logotipo.')
    return s.figura('Estación meteorológica con dos micro:bits')

def semaforo():
    s = Escena(760, 500, s=0.42, x0=300, y0=120)
    # maqueta de cartón con la calle
    s.caja(-40, 0, 1000, 700, 30, CARTON, tapa='#d7b57d')
    z0 = 30
    s.add('<g transform="%s"><rect x="-40" y="300" width="1000" height="180" fill="#4a4f57"/>%s</g>' % (
        s.M(z0 + 1), ''.join('<rect x="%d" y="384" width="60" height="12" fill="#fff"/>' % x for x in range(0, 960, 120))))
    s.add('<g transform="%s">%s</g>' % (s.M(z0 + 2), ''.join('<rect x="%d" y="300" width="22" height="180" fill="#f2f2f2"/>' % x for x in range(620, 800, 40))))
    # semáforo: poste y cabeza con tres LED
    s.caja(520, 200, 30, 30, 360, '#2b2f36', z=z0)
    s.caja(490, 190, 90, 60, 200, '#20252c', z=z0 + 360, sombra=False)
    for i, (c, on) in enumerate((('#ff3b30', True), ('#e2a400', False), ('#2e9d4f', False))):
        col = c if on else mix(c, .45)
        s.add('<g transform="%s"><circle cx="45" cy="%d" r="22" fill="%s"/>%s</g>' % (
            s.frontal(490, 250, z0 + 560), 38 + i * 62, col, ('<circle cx="45" cy="%d" r="34" fill="%s" opacity=".25"/>' % (38 + i * 62, c)) if on else ''))
    # micro:bit en la maqueta
    for anillo, col, du in (('P0', '#c0392b', 0), ('P1', '#e2a400', 10), ('P2', '#2e9d4f', 20)):
        a = s.anillo(80, 520, 280, anillo)
        s.cable((a[0], a[1]), (520 + du, 232), col, z=z0 + 4, grosor=8, curva=-160)
    for anillo, col in (('GND', '#262a30'),):
        a = s.anillo(80, 520, 280, anillo)
        s.cable((a[0], a[1]), (550, 232), col, z=z0 + 4, grosor=8, curva=-100)
    s.microbit(80, 520, 280, z=z0, lit={(r, c) for r in range(5) for c in range(5) if (r, c) in {(0, 2), (1, 1), (1, 2), (1, 3), (2, 2), (3, 1), (3, 3), (4, 1), (4, 3)}}, uid='sem')
    for anillo, col in (('P0', '#c0392b'), ('P1', '#e2a400'), ('P2', '#2e9d4f'), ('GND', '#262a30')):
        a = s.anillo(80, 520, 280, anillo)
        s.pinza(a[0], a[1], col, z=z0 + 10, largo=55)
    s.punto(535, 200, z0 + 600, 'Semáforo de coches', 'Tres LED con resistencias: rojo en P0, amarillo en P1 y verde en P2; las patas cortas a GND.')
    s.punto(220, 620, z0 + 14, 'micro:bit', 'El botón A es el pulsador de peatones; la pantalla muestra al peatón cruzando.')
    s.punto(700, 390, z0 + 6, 'Paso de peatones', 'Pintado en la maqueta de cartón.')
    return s.figura('Cruce con semáforo inteligente (maqueta de cartón)')

def casa():
    s = Escena(760, 520, s=0.44, x0=300, y0=150)
    s.caja(-60, -40, 1000, 760, 16, '#e9dcc0', sombra=False, tapa='#efe4cc')
    z0 = 16
    u, v, w, d, h = 80, 60, 520, 380, 300
    s.caja(u, v, w, d, h, CARTON, z=z0, tapa='#d7b57d')
    # tejado a dos aguas
    top = z0 + h
    s.add(s.poly([(u - 20, v + d / 2, top + 170), (u + w + 20, v + d / 2, top + 170), (u + w + 20, v + d + 30, top - 10), (u - 20, v + d + 30, top - 10)], '#b5482e'))
    s.add(s.poly([(u + w + 20, v - 30, top - 10), (u + w + 20, v + d / 2, top + 170), (u + w + 20, v + d + 30, top - 10)], '#8f3722'))
    # puerta entreabierta con láminas de aluminio
    s.add('<g transform="%s"><rect x="300" y="0" width="140" height="230" fill="#7a4a26"/><rect x="292" y="40" width="10" height="150" fill="#d4d9df" stroke="#8b939c"/>'
          '<rect x="430" y="40" width="10" height="150" fill="#d4d9df" stroke="#8b939c"/><circle cx="420" cy="120" r="7" fill="#e0a83a"/></g>' % s.frontal(u, v + d, z0 + 230))
    for wx in (40, 200):
        s.add('<g transform="%s"><rect x="%d" y="0" width="90" height="80" fill="#bfe3ff" stroke="#fff" stroke-width="6"/></g>' % (s.frontal(u, v + d, z0 + 260), wx))
    pa, pg = s.anillo(640, 520, 260, 'P1'), s.anillo(640, 520, 260, 'GND')
    s.cable((pa[0], pa[1]), (u + 300, v + d + 10), '#2e78d6', z=z0 + 4, grosor=8, curva=-120)
    s.cable((pg[0], pg[1]), (u + 440, v + d + 10), '#262a30', z=z0 + 4, grosor=8, curva=-60)
    s.microbit(640, 520, 260, z=z0, lit={(0, 0), (0, 4), (1, 1), (1, 3), (2, 2), (3, 1), (3, 3), (4, 0), (4, 4)}, uid='casa')
    s.pinza(pa[0], pa[1], '#2e78d6', z=z0 + 10, largo=60)
    s.pinza(pg[0], pg[1], '#262a30', z=z0 + 10, largo=60)
    s.punto(u + 370, v + d, z0 + 160, 'Interruptor de la puerta', 'Dos láminas de aluminio (P1 y GND) que se tocan con la puerta cerrada.')
    s.punto(770, 600, z0 + 14, 'micro:bit', 'Si se abre la puerta, suena la alarma. La clave A, A, B la desactiva.')
    s.punto(u + 300, v + d / 2, top + 170, 'Casa de cartón', 'Una caja de zapatos sirve: recorta la puerta y las ventanas.')
    return s.figura('Casa segura (maqueta de cartón)')

def votacion():
    s = Escena(760, 460, s=0.40, x0=260, y0=120)
    s.caja(-80, -60, 1300, 800, 16, '#e9dcc0', sombra=False, tapa='#efe4cc')
    z0 = 16
    pos = [(0, 60, SI), (330, -10, NO), (700, 40, SI), (60, 420, SI), (760, 440, NO)]
    for i, (u, v, lit) in enumerate(pos):
        s.microbit(u, v, 240, z=z0, lit=lit, uid='vo%d' % i)
        s.ondas(u + 120, v + 110, z0 + 40, n=2, color='#e3008c', r0=20)
    s.microbit(380, 300, 320, z=z0, lit={(r, c) for r in range(5) for c in range(5) if c in (1, 3) and r in (0, 1, 2, 3, 4)} | {(0, 2), (4, 2)}, uid='urna')
    s.punto(120, 160, z0 + 14, 'Votantes', 'Cada placa vota: A = sí y B = no.')
    s.punto(540, 440, z0 + 14, 'Urna', 'Cuenta los votos recibidos por radio (grupo 20) y los muestra al tocar el logotipo.')
    return s.figura('Votación por radio en clase')

def orquesta():
    s = Escena(760, 460, s=0.40, x0=260, y0=120)
    s.caja(-80, -60, 1300, 800, 16, '#e9dcc0', sombra=False, tapa='#efe4cc')
    z0 = 16
    s.microbit(380, 300, 320, z=z0, lit={(0, 2), (1, 2), (2, 2), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1)}, uid='dir')
    s.ondas(540, 450, z0 + 60, n=3, color='#e63022')
    for i, (u, v) in enumerate(((0, 40), (360, -40), (760, 30), (40, 470), (800, 480))):
        s.microbit(u, v, 230, z=z0, lit=SONRISA, uid='mu%d' % i)
        x, y = s.P(u + 200, v + 20, z0 + 120)
        s.add('<g transform="translate(%.1f %.1f)"><ellipse cx="0" cy="18" rx="9" ry="7" fill="#e63022"/><path d="M8 18 V-14 l14 6" stroke="#e63022" stroke-width="4" fill="none"/></g>' % (x, y))
    s.punto(540, 470, z0 + 14, 'Directora', 'Marca el compás por radio (grupo 30). Con A empieza y para.')
    s.punto(120, 140, z0 + 14, 'Músicos', 'Cada placa elige su nota con B y suena en los tiempos 1 y 3.')
    return s.figura('Orquesta micro:bit')
