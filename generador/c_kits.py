# -*- coding: utf-8 -*-
"""Kits de robótica: una ficha por kit (placa en modo anatomía, sensores y montaje) y sus actividades.
Datos comprobados en la documentación oficial (wiki de ELECFREAKS y de DFRobot) y en el código de sus extensiones de MakeCode.
Imágenes: dibujos propios, la foto de WuKong del repositorio pxt-wukong (MIT) y fotos de DFRobot enlazadas desde su wiki.
Las imágenes del wiki de ELECFREAKS no se copian (no tienen licencia abierta y su servidor no permite enlazarlas):
el montaje se ve en un visor que abre la página oficial."""
from common import page, proyecto, P, h2, ul, box, tabla, e, kbd

S = 'talleres'
GC, GL, GP, GW, GA = 'Cutebot', 'Maqueen Lite', 'Maqueen Plus V2', 'Wonder Building Kit', 'Smart Agriculture Kit'
GRUPOS = {
    GC: P('Coche robot de ELECFREAKS. Empieza por <b>Conoce Cutebot</b> y sigue con las actividades.'),
    GL: P('Robot de DFRobot para empezar con la robótica. Empieza por <b>Conoce Maqueen Lite</b>.'),
    GP: P('La versión ampliada de Maqueen, con cinco sensores de línea. Empieza por <b>Conoce Maqueen Plus V2</b>.'),
    GW: P('Piezas compatibles con LEGO, motores y la placa WuKong. Empieza por <b>Conoce el Wonder Building Kit</b>.'),
    GA: P('Sensores para el huerto y la granja con la placa IoT:bit. Empieza por <b>Conoce el Smart Agriculture Kit</b>.'),
}

EF = 'https://wiki.elecfreaks.com/en/microbit/'
def a(url, txt): return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (url, txt)

# ------------------------------------------------------------------ piezas comunes
def anat(src, alt, puntos, pie, svg=None):
    """Modo anatomía: imagen (o SVG propio) con puntos numerados y leyenda (x, y en %)."""
    marks = ''.join(('<span class="anat-pt" tabindex="0" style="left:%s%%;top:%s%%" aria-label="%s">%d'
                     '<span class="anat-tip%s"><b>%s</b>%s</span></span>') % (x, y, e(t), i + 1, ' izq' if x > 60 else '', t, d)
                    for i, (x, y, t, d) in enumerate(puntos))
    ley = ''.join('<li><span class="n">%d</span><b>%s</b>%s</li>' % (i + 1, t, d) for i, (x, y, t, d) in enumerate(puntos))
    fig = svg if svg else '<img src="{{ROOT}}%s" alt="%s" loading="lazy">' % (src, e(alt))
    return ('<figure class="captura"><div class="anat-wrap">%s%s</div><figcaption>%s</figcaption></figure>'
            '<ol class="leyenda">%s</ol>') % (fig, marks, pie, ley)

def carrusel(cid, slides, fuente):
    """slides: (url, texto) o (url, texto, (i, n)) para recortar el fotograma i de una tira de n."""
    sl = ''
    for k, s in enumerate(slides):
        url, txt = s[0], s[1]
        if len(s) > 2:
            i, n = s[2]
            img = ('<div class="crop" role="img" aria-label="%s" style="aspect-ratio:480/300;background-image:url(%s);'
                   'background-size:%d%% 100%%;background-position:%.4f%% 0"></div>') % (e(txt), url, n * 100, i * 100.0 / (n - 1))
        else:
            img = '<img src="%s" alt="%s" loading="lazy">' % (url, e(txt))
        sl += '<figure class="sl">%s<figcaption><b>%d</b>%s</figcaption></figure>' % (img, k + 1, txt)
    nums = ''.join('<a href="#">%d</a>' % (k + 1) for k in range(len(slides)))
    return ('<p>Usa las flechas, desliza las imágenes o pulsa un número.</p>'
            '<div class="carr" id="%s"><button class="carr-b prev" aria-label="Paso anterior">‹</button><div class="carr-t">%s</div>'
            '<button class="carr-b next" aria-label="Paso siguiente">›</button></div><div class="carr-n" data-c="%s">%s</div>'
            '<p class="fuente">Imágenes: %s. Se muestran enlazadas desde su web, con su autoría.</p>') % (cid, sl, cid, nums, fuente)

def visor(url, titulo, pasos):
    """Abre la página oficial de montaje dentro de la web (las imágenes las sirve el fabricante)."""
    return ('<div class="visor"><div class="visor-cab">Montaje oficial · %s · %s<a href="%s" target="_blank" rel="noopener">Abrir en el wiki ↗</a></div>'
            '<iframe src="%s" title="Montaje oficial: %s" loading="lazy"></iframe></div>'
            '<p class="fuente">Instrucciones e imágenes de ELECFREAKS, mostradas desde su wiki. Desplázate dentro del recuadro para ver todos los pasos.</p>') % (
                e(titulo), pasos, url, url, e(titulo))

def componentes(filas):
    return tabla(['Componente', 'Para qué sirve', 'Pin o puerto'], filas)

# =================================================================== CUTEBOT
page(S, 'cutebot', 'Conoce Cutebot',
    P('Cutebot es un coche de tracción trasera con dos motores. Trae sensores y luces de serie, así que se programa sin cables.') +
    h2('La placa del robot') +
    P('En Cutebot la placa de expansión <b>va integrada en el chasis</b>. La micro:bit se inserta en su ranura y la placa reparte la energía de las pilas '
      'y conecta motores, luces y sensores con los pines de la micro:bit. Encima va la placa del portapilas, con conectores para ampliar. Pasa el ratón por los números.') +
    anat('img/kits/cutebot-foto.png', 'Foto de Cutebot con la micro:bit', [
        (25, 50, 'Ultrasonidos HC-SR04', 'Delante. TRIG en P8 y ECHO en P12.'),
        (40, 34, 'micro:bit', 'Se inserta en la ranura del robot.'),
        (72, 34, 'Portapilas (3 × AA)', 'Con conectores I2C, servos S1-S2, P1 y P2.'),
        (85, 57, 'Ruedas traseras', 'Cada una con su micromotor de 300 rpm.'),
        (10, 57, 'Faros RGB', 'Uno a cada lado del frente.'),
        (24, 75, 'Debajo del chasis', 'Sensores de línea (P13 y P14), dos LED de colores (P15) y la rueda loca.'),
    ], 'Cutebot. Foto: %s (captura).' % a(EF + 'microbit-smart-car/microbit-smart-cutebot/cutebot_car', 'wiki de ELECFREAKS')) +
    P('Detrás están el receptor de infrarrojos (P16) y el interruptor de encendido.') +
    h2('Sensores y componentes') +
    componentes([
        ['2 motores (N20, 300 rpm)', 'Mueven las ruedas traseras; la rueda loca de delante permite girar', 'Placa del robot'],
        ['Ultrasonidos HC-SR04', 'Mide distancias de 2 a 400 cm', 'TRIG P8 · ECHO P12'],
        ['2 sensores de línea', 'Distinguen una línea negra del suelo claro', 'P13 (izquierdo) · P14 (derecho)'],
        ['2 faros RGB', 'Luces de colores delante', 'Placa del robot'],
        ['2 LED de colores (debajo)', 'Luces de gálibo', 'P15'],
        ['Receptor de infrarrojos', 'Recibe órdenes de un mando', 'P16'],
        ['Conectores del portapilas', 'I2C, servos S1 y S2, P1 y P2', '—'],
    ]) +
    h2('Montaje') +
    P('Cutebot viene montado. Solo hay que poner <b>3 pilas AA</b> en el portapilas, colocar el sensor de ultrasonidos delante e insertar la micro:bit con la pantalla hacia delante.') +
    box('idea', 'Extensión', P('En MakeCode, busca <b>cutebot</b> en Extensiones.')) +
    P('Fuente: %s y extensión oficial %s.' % (a(EF + 'microbit-smart-car/microbit-smart-cutebot/cutebot_car', 'wiki de ELECFREAKS'), a('https://github.com/elecfreaks/pxt-cutebot', 'pxt-cutebot'))),
    group=GC, icono='coche')

proyecto(S, 'cutebot-primeros-movimientos', 'Cutebot: primeros movimientos', GC,
    'Aprendemos a mover el coche: arrancar poco a poco para que no levante la rueda delantera, ir marcha atrás y dibujar un ocho en el suelo.',
    ['Cutebot con pilas y su micro:bit', 'Un espacio libre en el suelo'], None,
    ['Añade la extensión <b>cutebot</b>.',
     'Con A, sube la velocidad de 0 a 100 en diez pasos y luego para: así arranca suave.',
     'Con B, ve marcha atrás 1 segundo.', 'Con A+B, gira primero hacia un lado y luego hacia el otro para dibujar un ocho.'],
    mc='''input.onButtonPressed(Button.A, function () {
    for (let index = 0; index <= 10; index++) {
        cuteBot.motors(index * 10, index * 10)
        basic.pause(100)
    }
    basic.pause(1000)
    cuteBot.stopcar()
})
input.onButtonPressed(Button.B, function () {
    cuteBot.moveTime(cuteBot.Direction.backward, 50, 1)
})
input.onButtonPressed(Button.AB, function () {
    cuteBot.motors(80, 30)
    basic.pause(2000)
    cuteBot.motors(30, 80)
    basic.pause(2000)
    cuteBot.stopcar()
})''', pkgs=('cutebot',),
    ampliar=['Cambia las pausas hasta que el ocho quede cerrado.', 'Dibuja un cuadrado: avanza, gira, y repite 4 veces.'],
    docente=P('Basado en los casos 1 a 3 del wiki de ELECFREAKS. Las velocidades van de −100 a 100 en el bloque de las dos ruedas.'),
    icono='coche', tiempo='1 sesión', etapa='P2')

proyecto(S, 'cutebot-luces', 'Cutebot: faros automáticos e intermitentes', GC,
    'Los faros se encienden solos cuando hay poca luz. Con los botones, el coche pone el intermitente antes de girar.',
    ['Cutebot con pilas y su micro:bit', 'Una linterna o una caja para tapar la luz'], None,
    ['Crea la variable %s y ponla en falso.' % kbd('intermitente'),
     'Para siempre: si no hay intermitente y el nivel de luz es menor que 30, enciende los faros en blanco; si no, apágalos.',
     'Con A, parpadea 5 veces el faro derecho en naranja; con B, el izquierdo.'],
    mc='''let intermitente = false
input.onButtonPressed(Button.A, function () {
    intermitente = true
    for (let index = 0; index < 5; index++) {
        cuteBot.colorLight(cuteBot.RGBLights.RGB_L, 0xff8000)
        basic.pause(300)
        cuteBot.closeheadlights()
        basic.pause(300)
    }
    intermitente = false
})
input.onButtonPressed(Button.B, function () {
    intermitente = true
    for (let index = 0; index < 5; index++) {
        cuteBot.colorLight(cuteBot.RGBLights.RGB_R, 0xff8000)
        basic.pause(300)
        cuteBot.closeheadlights()
        basic.pause(300)
    }
    intermitente = false
})
basic.forever(function () {
    if (!(intermitente)) {
        if (input.lightLevel() < 30) {
            cuteBot.colorLight(cuteBot.RGBLights.ALL, 0xffffff)
        } else {
            cuteBot.closeheadlights()
        }
    }
})''', pkgs=('cutebot',),
    ampliar=['Ajusta el umbral de 30 según la luz de tu clase.', 'Haz que gire de verdad después del intermitente.'],
    docente=P('Basado en los casos 5 y 6 del wiki de ELECFREAKS. El nivel de luz lo mide la pantalla de la micro:bit (de 0 a 255). '
              'Ojo: en la extensión, el faro <code>RGB_L</code> aparece como «Right_RGB» (derecho) y <code>RGB_R</code> como «Left_RGB» (izquierdo).'),
    icono='bombilla', tiempo='1 sesión', etapa='P2')

proyecto(S, 'taller-cutebot', 'Cutebot: sigue la línea y esquiva obstáculos', GC,
    'Programamos Cutebot para seguir una línea negra y frenar ante los obstáculos.',
    ['Cutebot con pilas y su micro:bit', 'Cinta aislante negra sobre un suelo claro (o el mapa que trae el kit)'], None,
    ['Con A, activa el modo <b>seguir la línea</b>: si los dos sensores ven línea, recto; si solo la ve el izquierdo, gira a la izquierda; si solo el derecho, a la derecha.',
     'Si un obstáculo está a menos de 10 cm, para y enciende los faros en rojo.', 'Con B, detén el robot.'],
    mc='''let activo = false
input.onButtonPressed(Button.A, function () {
    activo = true
})
input.onButtonPressed(Button.B, function () {
    activo = false
    cuteBot.stopcar()
})
basic.forever(function () {
    if (activo) {
        if (cuteBot.ultrasonic(cuteBot.SonarUnit.Centimeters) < 10) {
            cuteBot.stopcar()
            cuteBot.colorLight(cuteBot.RGBLights.ALL, 0xff0000)
        } else {
            cuteBot.colorLight(cuteBot.RGBLights.ALL, 0x00ff00)
            if (cuteBot.tracking(cuteBot.TrackingState.L_R_line)) {
                cuteBot.motors(30, 30)
            } else if (cuteBot.tracking(cuteBot.TrackingState.L_line_R_unline)) {
                cuteBot.motors(0, 30)
            } else if (cuteBot.tracking(cuteBot.TrackingState.L_unline_R_line)) {
                cuteBot.motors(30, 0)
            }
        }
    }
})''', pkgs=('cutebot',),
    ampliar=['¿Cuál es la velocidad más rápida a la que no se sale?', 'Haz una carrera de seguidores de línea por equipos.'],
    docente=P('Basado en los casos 8 y 9 del wiki de ELECFREAKS. Si el robot se sale en las curvas, baja la velocidad.'),
    icono='coche', tiempo='2 sesiones', etapa='P2')

proyecto(S, 'cutebot-mantiene-distancia', 'Cutebot: mantén la distancia', GC,
    'El coche sigue tu mano como si fuera una mascota: se acerca si te alejas y retrocede si te acercas demasiado.',
    ['Cutebot con pilas y su micro:bit', 'Tu mano o un libro'], None,
    ['Guarda en %s la distancia que mide el ultrasonido.' % kbd('distancia'),
     'Si es menor que 10 cm, retrocede; si está entre 20 y 40 cm, avanza; en otro caso, para.'],
    mc='''let distancia = 0
basic.forever(function () {
    distancia = cuteBot.ultrasonic(cuteBot.SonarUnit.Centimeters)
    if (distancia < 10) {
        cuteBot.motors(-30, -30)
    } else if (distancia > 20 && distancia < 40) {
        cuteBot.motors(30, 30)
    } else {
        cuteBot.stopcar()
    }
})''', pkgs=('cutebot',),
    ampliar=['Muestra la distancia en la pantalla con un gráfico de barras.'],
    docente=P('Basado en el caso 10 del wiki de ELECFREAKS. Entre 10 y 20 cm el coche se queda quieto: es la «zona tranquila».'),
    icono='onda', tiempo='1 sesión', etapa='P2')

proyecto(S, 'cutebot-teledirigido', 'Cutebot: teledirigido por radio', GC,
    'Una micro:bit hace de mando: al inclinarla, el Cutebot avanza, retrocede o gira. Une la práctica '
    '<a href="../experto/mando-por-inclinacion.html">R6 · Mando por inclinación</a> con los motores del robot.',
    ['Cutebot con pilas y su micro:bit', 'Otra micro:bit con portapilas (el mando)', 'Un circuito con obstáculos hecho con cajas o vasos'], None,
    ['Carga en la micro:bit del mando el programa de la práctica R6. Envía 1 (delante), 2 (detrás), 3 (izquierda), 4 (derecha) o 0 (plana) por el grupo de radio 7.',
     'En la micro:bit del robot pon el mismo %s y, al recibir un número, mueve los motores según el código: para girar, una rueda va más rápida que la otra.' % kbd('radio fijar grupo 7'),
     'Guarda en %s el momento en que llegó el último mensaje.' % kbd('ultimo'),
     'En %s, si han pasado más de 500 ms sin mensajes, para el coche: así no se escapa si el mando se apaga o se aleja.' % kbd('para siempre'),
     'Prueba en el suelo: si al inclinar a la izquierda gira a la derecha, intercambia los códigos 3 y 4 en el robot.'],
    mc='''let ultimo = 0
radio.setGroup(7)
radio.onReceivedNumber(function (receivedNumber) {
    ultimo = input.runningTime()
    if (receivedNumber == 1) {
        cuteBot.motors(50, 50)
    } else if (receivedNumber == 2) {
        cuteBot.motors(-40, -40)
    } else if (receivedNumber == 3) {
        cuteBot.motors(10, 50)
    } else if (receivedNumber == 4) {
        cuteBot.motors(50, 10)
    } else {
        cuteBot.stopcar()
    }
})
basic.forever(function () {
    if (input.runningTime() - ultimo > 500) {
        cuteBot.stopcar()
    }
    basic.pause(100)
})''', pkgs=('cutebot',),
    ampliar=['Usa el botón A del mando para tocar el claxon (código 5) y el B para encender los faros (código 6).',
             'Carrera de obstáculos por equipos: una persona conduce y otra da indicaciones sin tocar el mando.',
             'Con Maqueen Lite funciona igual: cambia los bloques de motor por los de la extensión maqueen.'],
    docente=P('Cada pareja debe usar un número de grupo distinto (del 0 al 255): si dos mandos comparten grupo, mueven los dos robots. '
              'El código 0 y la parada por tiempo son la «seguridad» del robot: conviene comentarlo con el grupo.'),
    icono='mando', tiempo='1-2 sesiones', etapa='P2')

# =================================================================== MAQUEEN LITE
DF_LITE = 'https://wiki.dfrobot.com/rob0148-en/'
TIRA = 'https://dfimg.dfrobot.com/nobody/wiki/1c52b0e9bde2fdc52f3bd068b52ebc60_0x0.jpg.webp'
page(S, 'maqueen-lite', 'Conoce Maqueen Lite',
    P('Maqueen Lite es un robot pequeño de DFRobot con dos motores, sensores de línea, luces y conector para ultrasonidos.') +
    h2('La placa del robot') +
    P('Como en Cutebot, la placa de expansión <b>es el propio chasis</b>: tiene la ranura de la micro:bit, el control de los motores y los conectores. Pasa el ratón por los números.') +
    anat('img/kits/maqueen-lite-placa.png', 'Placa de Maqueen Lite vista desde arriba', [
        (46, 8, 'Receptor de infrarrojos', 'P16.'),
        (37, 11, 'Luz LED izquierda', 'P8.'),
        (56, 11, 'Luz LED derecha', 'P12.'),
        (31, 25, 'Botón de calibración', 'Para los sensores de línea.'),
        (30, 39, 'Servos S1 y S2', 'Conectores para dos servos.'),
        (46, 31, 'Conector de ultrasonidos e I2C', 'SR04: TRIG en P1 y ECHO en P2. I2C: P19 y P20.'),
        (63, 39, 'Puertos P0, P1 y P2', 'Para sensores Gravity.'),
        (53, 49, 'Zumbador', 'En P0; tiene un interruptor para desconectarlo.'),
        (38, 69, 'Motores', 'Izquierdo y derecho, controlados por I2C.'),
        (46, 92, 'Interruptor de encendido', 'Alimentación de 3,5 a 5 V.'),
    ], 'Maqueen Lite. Imagen: %s (captura del diagrama de pines).' % a(DF_LITE + '#tech_specs', 'wiki de DFRobot')) +
    h2('Sensores y componentes') +
    componentes([
        ['2 motores N20', 'Mueven las ruedas', 'M1 (izquierdo) · M2 (derecho)'],
        ['2 sensores de línea', 'Dan 0 sobre negro y 1 sobre blanco', 'P13 · P14'],
        ['2 luces LED rojas', 'Se encienden o apagan', 'P8 (izquierda) · P12 (derecha)'],
        ['Ultrasonidos SR04', 'Mide distancias', 'TRIG P1 · ECHO P2'],
        ['Zumbador', 'Hace sonar notas y melodías', 'P0'],
        ['Receptor de infrarrojos', 'Recibe órdenes de un mando', 'P16'],
        ['4 luces RGB de ambiente', 'Luces de colores', '—'],
        ['Conectores', 'Servos S1 y S2, Gravity P0-P2 e I2C', '—'],
    ]) +
    h2('Montaje') +
    carrusel('mq-lite', [
        (TIRA, 'Monta las dos ruedas.', (0, 5)),
        (TIRA, 'Pega la cinta adhesiva de doble cara en el portapilas.', (1, 5)),
        (TIRA, 'Conecta el cable del portapilas.', (2, 5)),
        (TIRA, 'Fija el portapilas al coche y pon 3 pilas AAA.', (3, 5)),
        (TIRA, 'Inserta la micro:bit (y el sensor de ultrasonidos en su conector).', (4, 5)),
    ], 'DFRobot, %s' % a(DF_LITE + 'docs/22595', 'guía de inicio de Maqueen Lite')) +
    box('ojo', 'Calibrar los sensores de línea', P('Vienen calibrados. Si no detectan bien la línea: pon el robot con los dos sensores sobre negro y mantén pulsado el botón de calibración 1 segundo; los indicadores azules parpadean.')) +
    box('idea', 'Extensión', P('En MakeCode, busca <b>maqueen</b> o pega <code>https://github.com/DFRobot/pxt-maqueen</code>.')) +
    P('Fuente: %s (especificaciones y pines) y extensión oficial %s.' % (a(DF_LITE, 'wiki de DFRobot'), a('https://github.com/DFRobot/pxt-maqueen', 'pxt-maqueen'))),
    group=GL, icono='robot')

proyecto(S, 'maqueen-baile', 'Maqueen: baile de motores y luces', GL,
    'Primer contacto con los motores y las luces: el robot avanza, gira sobre sí mismo y sus luces se alternan como en una pista de baile.',
    ['Maqueen Lite con pilas y su micro:bit'], None,
    ['Añade la extensión <b>maqueen</b>.', 'Con A, avanza 1 segundo, gira sobre sí mismo (un motor hacia delante y otro hacia atrás) y para.',
     'Para siempre, alterna la luz izquierda y la derecha cada 300 ms.'],
    mc='''input.onButtonPressed(Button.A, function () {
    maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 100)
    basic.pause(1000)
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 100)
    maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 100)
    basic.pause(800)
    maqueen.motorStop(maqueen.Motors.All)
})
basic.forever(function () {
    maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
    maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
    basic.pause(300)
    maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
    maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
    basic.pause(300)
})''', pkgs=('maqueen',),
    ampliar=['Añade música con los bloques de Música mientras baila.', 'Inventa una coreografía con B.'],
    docente=P('Basado en los ejemplos de motores y de luces del wiki de DFRobot (velocidad de 0 a 255).'),
    icono='musica', tiempo='1 sesión', etapa='P2')

proyecto(S, 'maqueen-sensores', 'Maqueen: lee sus sensores', GL,
    'Antes de programar un robot autónomo hay que saber qué «ve». Mostramos en la pantalla la distancia y lo que leen los sensores de línea.',
    ['Maqueen Lite con su micro:bit y el ultrasonido montado', 'Una hoja con una franja negra'], None,
    ['Con A, muestra la distancia del ultrasonido en centímetros.',
     'Con B, muestra el valor del sensor de línea izquierdo y después el del derecho.',
     'Prueba sobre negro y sobre blanco y anota los valores en una tabla.'],
    mc='''input.onButtonPressed(Button.A, function () {
    basic.showNumber(maqueen.Ultrasonic())
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(maqueen.readPatrol(maqueen.Patrol.PatrolLeft))
    basic.showNumber(maqueen.readPatrol(maqueen.Patrol.PatrolRight))
})''', pkgs=('maqueen',),
    ampliar=['¿A qué distancia máxima detecta una pared? ¿Y una pelota?'],
    docente=P('Basado en los ejemplos de lectura del wiki de DFRobot: el sensor de línea da 0 sobre negro y 1 sobre blanco. Si el ultrasonido da 0, revisa el conector.'),
    icono='lupa', tiempo='1 sesión', etapa='P2')

proyecto(S, 'maqueen-sigue-linea', 'Maqueen: sigue la línea', GL,
    'Con los dos sensores de línea el robot recorre un circuito de cinta negra sin salirse.',
    ['Maqueen Lite con pilas y su micro:bit', 'El mapa del kit o un circuito de cinta negra'], None,
    ['Si los dos sensores ven negro (0 y 0), avanza.',
     'Si solo el izquierdo ve negro, para el motor izquierdo y mueve el derecho: gira a la izquierda.',
     'Si solo el derecho ve negro, haz lo contrario.'],
    mc='''basic.forever(function () {
    if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 60)
    } else if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
        maqueen.motorStop(maqueen.Motors.M1)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 60)
    } else if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 60)
        maqueen.motorStop(maqueen.Motors.M2)
    }
})''', pkgs=('maqueen',),
    ampliar=['Si pierde la línea (1 y 1), haz que retroceda un poco.'],
    docente=P('Basado en el ejemplo de seguimiento de línea del wiki de DFRobot. Si gira hacia el lado equivocado, intercambia los motores en los dos casos de giro.'),
    icono='robot', tiempo='1-2 sesiones', etapa='P2')

proyecto(S, 'taller-maqueen', 'Maqueen: robot que esquiva obstáculos', GL,
    'El robot avanza, detecta obstáculos con el ultrasonido, enciende sus luces y gira para esquivarlos.',
    ['Maqueen Lite con su micro:bit y el ultrasonido montado', 'Cajas o libros como obstáculos'], None,
    ['Si la distancia es mayor que 15 cm, avanza con las luces apagadas.', 'Si es menor, enciende las luces, retrocede un poco y gira hacia un lado.'],
    mc='''basic.forever(function () {
    if (maqueen.Ultrasonic() > 15) {
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 80)
    } else {
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CCW, 60)
        basic.pause(400)
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 80)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 80)
        basic.pause(400)
    }
})''', pkgs=('maqueen',),
    ampliar=['Elige el lado del giro al azar.', 'Haz que pite antes de retroceder, como un camión.'],
    docente=P('Basado en el ejemplo de esquivar obstáculos del wiki de DFRobot (allí gira si el obstáculo está a menos de 30 cm).'),
    icono='robot', tiempo='1 sesión', etapa='P2')

# =================================================================== MAQUEEN PLUS V2
DF_PLUS = 'https://wiki.dfrobot.com/mbt0021-en/'
DFI = 'https://dfimg.dfrobot.com/nobody/wiki/'
page(S, 'maqueen-plus-v2', 'Conoce Maqueen Plus V2',
    P('Maqueen Plus V2 es más grande que Maqueen Lite: tiene cinco sensores de línea calibrables, faros, luces RGB y muchos más conectores.') +
    h2('La placa del robot') +
    P('La placa de expansión es la base del robot. Sobre ella van el portapilas, la ranura de la micro:bit y el sensor de ultrasonidos. Pasa el ratón por los números.') +
    anat('img/kits/maqueen-plus-v2-foto.png', 'Foto de Maqueen Plus V2 con sus partes', [
        (41, 21, 'Portapilas', '4 pilas AA (o una batería 18650 en su versión).'),
        (56, 45, 'micro:bit', 'Compatible con V1 y V2.'),
        (59, 58, 'Ultrasonidos', 'TRIG en P13 y ECHO en P14.'),
        (55, 71, 'Faros LED', 'Dos luces delanteras.'),
        (61, 78, 'Receptor de infrarrojos', 'Para un mando a distancia.'),
        (47, 78, '4 luces RGB', 'Debajo, en P15.'),
        (37, 64, '5 sensores de línea', 'Debajo: L2, L1, M, R1 y R2. Dan 1 sobre negro.'),
        (37, 39, 'Zumbador', 'En P0, con interruptor.'),
        (36, 28, 'Puertos de expansión', 'E/S de 5 V y 3,3 V e I2C (también para HuskyLens).'),
    ], 'Maqueen Plus V2 (versión AA). Foto: %s (captura).' % a(DF_PLUS + '#tech_specs', 'wiki de DFRobot')) +
    h2('Sensores y componentes') +
    componentes([
        ['2 motores N20', 'Mueven las ruedas', 'Placa del robot (I2C)'],
        ['5 sensores de línea', 'L2, L1, M, R1 y R2; dan 1 sobre negro', 'Placa del robot (I2C)'],
        ['2 faros LED', 'Luces delanteras', 'Placa del robot (I2C)'],
        ['4 luces RGB', 'Luces de colores de ambiente', 'P15'],
        ['Ultrasonidos SR04', 'Mide distancias', 'TRIG P13 · ECHO P14'],
        ['Zumbador (con interruptor)', 'Sonidos; si se apaga, P0 queda libre', 'P0'],
        ['Receptor de infrarrojos', 'Recibe órdenes de un mando', '—'],
        ['Conectores', 'E/S de 5 V (P0-P2), E/S de 3,3 V e I2C (también para la cámara HuskyLens)', '—'],
    ]) +
    h2('Puesta en marcha') +
    carrusel('mq-plus', [
        (DFI + 'f6893244d53f891da9d2fd4de5cf04a6_0x0.png.webp', 'El robot y sus partes (versión con pilas AA).'),
        (DFI + '9386da971b12552baf80df6d72b7ba8b_0x0.jpg.webp', 'Pon 4 pilas AA (o la batería 18650 en su versión). Cuidado con la polaridad.'),
        (DFI + '37afb24ea182d418547f342f08b130ab_0x0.png.webp', 'Conecta el sensor de ultrasonidos.'),
        (DFI + 'd43ec607ad5af69cd05d745847a4622c_0x0.jpg.webp', 'Inserta la micro:bit.'),
        (DFI + '48c8e47f7bc4a6dae6323b5f74547312_0x0.jpg.webp', 'Conecta la micro:bit al ordenador con el cable USB y descarga el programa.'),
        (DFI + 'b37b805507874152f7749c055c532e2d_0x0.jpg.webp', 'Desconecta el cable y enciende el interruptor.'),
        (DFI + 'fbb0f4a03b0babf2030fcddc3b094699_0x0.png.webp', 'Calibración (solo si hace falta): pon los 5 sensores sobre negro…'),
        (DFI + '8686a0d760f4abf84031d8ab816ee6b9_0x0.png.webp', '…y mantén pulsado el botón de calibración 1 segundo: los faros parpadean.'),
    ], 'DFRobot, %s' % a(DF_PLUS + 'docs/21531', 'guía de inicio de Maqueen Plus V2')) +
    box('idea', 'Extensión', P('En MakeCode, pega <code>https://github.com/DFRobot/pxt-DFRobot_MaqueenPlus_v20</code> en el buscador de extensiones. '
        'Empieza siempre el programa con %s.' % kbd('I2CInit'))) +
    P('Fuente: %s y extensión oficial %s.' % (a(DF_PLUS, 'wiki de DFRobot'), a('https://github.com/DFRobot/pxt-DFRobot_MaqueenPlus_v20', 'pxt-DFRobot_MaqueenPlus_v20'))),
    group=GP, icono='robot')

proyecto(S, 'maqueen-plus-primeros-pasos', 'Maqueen Plus V2: movimientos y luces', GP,
    'Movemos el robot y usamos sus dos tipos de luces: los faros delanteros y las luces RGB de colores.',
    ['Maqueen Plus V2 con pilas y su micro:bit'], None,
    ['Al iniciar, llama a %s.' % kbd('I2CInit'),
     'Con A, enciende los faros y las luces RGB en verde, avanza 1 segundo, gira y para.',
     'Con B, ve marcha atrás con las luces en rojo.'],
    mc='''input.onButtonPressed(Button.A, function () {
    maqueenPlusV2.controlLED(maqueenPlusV2.MyEnumLed.AllLed, maqueenPlusV2.MyEnumSwitch.Open)
    maqueenPlusV2.showColor(DigitalPin.P15, maqueenPlusV2.colors(maqueenPlusV2.NeoPixelColors.Green))
    maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.AllMotor, maqueenPlusV2.MyEnumDir.Forward, 100)
    basic.pause(1000)
    maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.LeftMotor, maqueenPlusV2.MyEnumDir.Forward, 100)
    maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.RightMotor, maqueenPlusV2.MyEnumDir.Backward, 100)
    basic.pause(600)
    maqueenPlusV2.controlMotorStop(maqueenPlusV2.MyEnumMotor.AllMotor)
    maqueenPlusV2.controlLED(maqueenPlusV2.MyEnumLed.AllLed, maqueenPlusV2.MyEnumSwitch.Close)
    maqueenPlusV2.ledBlank(DigitalPin.P15)
})
input.onButtonPressed(Button.B, function () {
    maqueenPlusV2.showColor(DigitalPin.P15, maqueenPlusV2.colors(maqueenPlusV2.NeoPixelColors.Red))
    maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.AllMotor, maqueenPlusV2.MyEnumDir.Backward, 80)
    basic.pause(1000)
    maqueenPlusV2.controlMotorStop(maqueenPlusV2.MyEnumMotor.AllMotor)
    maqueenPlusV2.ledBlank(DigitalPin.P15)
})
maqueenPlusV2.I2CInit()''', pkgs=('maqueenplus',),
    ampliar=['Cambia los colores y los tiempos para crear tu propia señal.'],
    docente=P('Basado en el ejemplo de prueba de la extensión oficial (luces RGB en P15). La velocidad de los motores va de 0 a 255.'),
    icono='bombilla', tiempo='1 sesión', etapa='P2')

proyecto(S, 'maqueen-plus-esquiva', 'Maqueen Plus V2: esquiva obstáculos', GP,
    'El robot avanza y, si encuentra algo a menos de 30 cm, enciende los faros y gira hacia un lado elegido al azar.',
    ['Maqueen Plus V2 con su micro:bit y el ultrasonido conectado', 'Cajas o libros como obstáculos'], None,
    ['Guarda en %s la distancia (TRIG P13, ECHO P14).' % kbd('distancia'),
     'Si es menor que 30 y no es 0, enciende los faros y gira a un lado al azar durante 0,8 s.',
     'Si no, apaga los faros y avanza.'],
    mc='''let distancia = 0
maqueenPlusV2.I2CInit()
basic.forever(function () {
    distancia = maqueenPlusV2.readUltrasonic(DigitalPin.P13, DigitalPin.P14)
    if (distancia < 30 && distancia != 0) {
        maqueenPlusV2.controlLED(maqueenPlusV2.MyEnumLed.AllLed, maqueenPlusV2.MyEnumSwitch.Open)
        if (Math.randomBoolean()) {
            maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.LeftMotor, maqueenPlusV2.MyEnumDir.Forward, 100)
            maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.RightMotor, maqueenPlusV2.MyEnumDir.Forward, 0)
        } else {
            maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.LeftMotor, maqueenPlusV2.MyEnumDir.Forward, 0)
            maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.RightMotor, maqueenPlusV2.MyEnumDir.Forward, 100)
        }
        basic.pause(800)
    } else {
        maqueenPlusV2.controlLED(maqueenPlusV2.MyEnumLed.AllLed, maqueenPlusV2.MyEnumSwitch.Close)
        maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.AllMotor, maqueenPlusV2.MyEnumDir.Forward, 100)
    }
})''', pkgs=('maqueenplus',),
    ampliar=['Haz que suene una nota cada vez que esquiva.'],
    docente=P('Adaptado del programa de ejemplo de la guía de inicio de DFRobot. Se descarta el 0 porque el sensor lo da cuando no recibe eco.'),
    icono='robot', tiempo='1 sesión', etapa='P2')

proyecto(S, 'taller-maqueen-plus', 'Maqueen Plus V2: seguidor de línea', GP,
    'Seguimos una línea con el sensor central y los dos interiores.',
    ['Maqueen Plus V2 con pilas y su micro:bit', 'El mapa del kit o un circuito de cinta negra'], None,
    ['Al iniciar, llama a %s.' % kbd('I2CInit'),
     'Si el sensor central (M) ve la línea (vale 1), avanza recto.',
     'Si la ve el sensor derecho interior (R1) y no el izquierdo (L1), corrige hacia la derecha; si es al revés, hacia la izquierda.'],
    mc='''maqueenPlusV2.I2CInit()
basic.forever(function () {
    if (maqueenPlusV2.readLineSensorState(maqueenPlusV2.MyEnumLineSensor.SensorM) == 1) {
        maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.AllMotor, maqueenPlusV2.MyEnumDir.Forward, 80)
    } else if (maqueenPlusV2.readLineSensorState(maqueenPlusV2.MyEnumLineSensor.SensorR1) == 1) {
        maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.LeftMotor, maqueenPlusV2.MyEnumDir.Forward, 120)
        maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.RightMotor, maqueenPlusV2.MyEnumDir.Forward, 30)
    } else if (maqueenPlusV2.readLineSensorState(maqueenPlusV2.MyEnumLineSensor.SensorL1) == 1) {
        maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.LeftMotor, maqueenPlusV2.MyEnumDir.Forward, 30)
        maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.RightMotor, maqueenPlusV2.MyEnumDir.Forward, 120)
    }
})''', pkgs=('maqueenplus',),
    ampliar=['Usa también los sensores exteriores (L2 y R2) para las curvas cerradas.'],
    docente=P('Adaptado del ejemplo de seguimiento de línea de la extensión oficial, en el que el estado 1 indica que el sensor detecta la línea.'),
    icono='robot', tiempo='1-2 sesiones', etapa='P2')

proyecto(S, 'maqueen-plus-polilla', 'Maqueen Plus V2: robot polilla', GP,
    'Como una polilla, el robot avanza hacia la luz: cuanta más luz recibe la micro:bit, más rápido va.',
    ['Maqueen Plus V2 con su micro:bit', 'Una linterna'], None,
    ['Para siempre: si el nivel de luz es mayor que 100, avanza con una velocidad igual al nivel de luz.', 'Si no, para.'],
    mc='''maqueenPlusV2.I2CInit()
basic.forever(function () {
    if (input.lightLevel() > 100) {
        maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.AllMotor, maqueenPlusV2.MyEnumDir.Forward, input.lightLevel())
    } else {
        maqueenPlusV2.controlMotorStop(maqueenPlusV2.MyEnumMotor.AllMotor)
    }
})''', pkgs=('maqueenplus',),
    ampliar=['Al revés: un robot que huye de la luz (marcha atrás).'],
    docente=P('Inspirado en el ejemplo de control por luz del wiki de DFRobot. La luz la mide la pantalla de la micro:bit (0 a 255), el mismo rango que la velocidad de los motores.'),
    icono='bombilla', tiempo='1 sesión', etapa='P2')

# =================================================================== WONDER BUILDING KIT
WB = EF + 'building-blocks/wonder-building-kit/'
page(S, 'wonder-building-kit', 'Conoce el Wonder Building Kit',
    P('Kit de construcción con piezas compatibles con LEGO para montar decenas de modelos (motos, coches, puertas, brazos robot…). El cerebro es la micro:bit sobre la placa WuKong.') +
    h2('La placa WuKong') +
    P('WuKong es la placa de expansión del kit. Lleva <b>batería propia</b> (400 mAh, se carga en unos 20 minutos por USB) y los circuitos para mover motores y servos, '
      'que la micro:bit sola no puede alimentar. Se encaja en las piezas como un ladrillo más. Pasa el ratón por los números.') +
    anat('img/kits/wukong-placa.png', 'Placa WuKong con sus conectores', [
        (50, 30, 'Ranura de la micro:bit', 'Se inserta con la pantalla hacia fuera.'),
        (20, 52, 'Servos S0 a S7', 'Ocho conectores de servo: señal (azul), V (rojo) y G (negro).'),
        (79, 52, 'Puertos GVS', 'P0, P1, P2, P8, P12, P13, P14 y P15 para sensores: G (tierra), V (3 V) y S (señal).'),
        (49, 57, 'Alimentación de 5 V', 'Para los sensores que necesitan 5 V.'),
        (50, 74, 'Conector I2C', 'G, 3V, P19 (CL) y P20 (DA): pantalla OLED y otros módulos I2C.'),
        (9, 72, 'Motor M1', 'Conector del primer motor.'),
        (91, 72, 'Motor M2', 'Conector del segundo motor.'),
        (77, 12, 'Luces de colores', 'LED0 a LED3, en P16. Se programan con la extensión NeoPixel.'),
        (59, 86, 'Encendido y carga', 'Un clic enciende y doble clic apaga. Los cuatro LED indican la batería.'),
    ], 'Placa WuKong. Imagen del repositorio oficial %s de ELECFREAKS (licencia MIT).' % a('https://github.com/elecfreaks/pxt-wukong', 'pxt-wukong')) +
    P('Además, la WuKong tiene un zumbador en P0, que suena con los bloques de Música.') +
    h2('Componentes que usan los modelos') +
    componentes([
        ['2 motores Geekservo (2 kg)', 'Mueven ruedas y mecanismos', 'M1 y M2'],
        ['Servo Geekservo de 360°', 'Abre puertas, mueve brazos', 'S0 (S0 a S7)'],
        ['Ultrasonidos sonar:bit', 'Mide distancias', 'P1 en los casos 4 y 7'],
        ['Sensor de línea doble', 'Sigue líneas negras', 'P1 y P2'],
        ['Piezas compatibles con LEGO', 'Estructura de cada modelo', '—'],
    ]) +
    P('Comprueba el inventario de tu caja: cada caso del wiki empieza con la lista de piezas que necesita.') +
    box('idea', 'Extensiones', P('En MakeCode, busca <b>wukong</b>. Para el ultrasonido, añade también <code>https://github.com/elecfreaks/pxt-sonarbit</code>.')) +
    P('Fuente: %s y %s.' % (a(EF + 'octopus-series/expansion-board/wukong', 'ficha de la placa WuKong'), a(WB, 'casos del Wonder Building Kit'))),
    group=GW, icono='engranaje')

proyecto(S, 'taller-wonder-building', 'Wonder: la moto', GW,
    'Construimos la moto del caso 1 de la guía oficial y la conducimos con los botones.',
    ['Wonder Building Kit (WuKong, 2 motores y piezas)', 'micro:bit'],
    visor(WB + 'wonder-building-kit-case-01/#bricks-build-up', 'Caso 1: la moto', '12 pasos') +
    tabla(['Componente', 'Puerto de la WuKong'], [['Motor 1', 'M1'], ['Motor 2', 'M2']]),
    ['Monta la moto con el visor.', 'Añade la extensión <b>wukong</b>.',
     'Con A, avanza; con B, retrocede; con A+B, para.', 'Muestra una flecha con el sentido de la marcha.'],
    mc='''input.onButtonPressed(Button.A, function () {
    wuKong.setAllMotor(-60, -60)
    basic.showArrow(ArrowNames.North)
})
input.onButtonPressed(Button.B, function () {
    wuKong.setAllMotor(60, 60)
    basic.showArrow(ArrowNames.South)
})
input.onButtonPressed(Button.AB, function () {
    wuKong.stopAllMotor()
    basic.showIcon(IconNames.No)
})''', pkgs=('wukong',),
    ampliar=['¿Qué pasa si los dos motores van a distinta velocidad?', 'Conduce la moto inclinando otra micro:bit por radio.'],
    docente=P('Basado en el caso 1 del wiki de ELECFREAKS: allí la moto avanza con velocidad negativa por cómo quedan montados los motores. '
              'Si vuestra moto va al revés, cambiad el signo. Velocidad de −100 a 100.'),
    icono='engranaje', tiempo='2 sesiones', etapa='P2')

proyecto(S, 'wonder-coche-sigue-lineas', 'Wonder: coche que sigue líneas', GW,
    'Montamos el coche del caso 2 con el sensor de línea doble y lo programamos para recorrer un circuito negro.',
    ['Wonder Building Kit (WuKong, 2 motores, sensor de línea doble y piezas)', 'micro:bit', 'Circuito de cinta negra'],
    visor(WB + 'wonder-building-kit-case-02/#bricks-build-up', 'Caso 2: coche que sigue líneas', '8 pasos') +
    tabla(['Componente', 'Puerto de la WuKong'], [['Motores', 'M1 y M2'], ['Sensor de línea doble', 'P1 y P2']]),
    ['Al iniciar, activa la resistencia de pull-up en P1 y P2.',
     'Si los dos sensores dan 0 (ven la línea), avanza.',
     'Si P1 da 0 y P2 da 1, gira con un solo motor; si es al revés, con el otro.'],
    mc='''pins.setPull(DigitalPin.P1, PinPullMode.PullUp)
pins.setPull(DigitalPin.P2, PinPullMode.PullUp)
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P1) == 0 && pins.digitalReadPin(DigitalPin.P2) == 0) {
        wuKong.setAllMotor(-60, -60)
    } else if (pins.digitalReadPin(DigitalPin.P1) == 0 && pins.digitalReadPin(DigitalPin.P2) == 1) {
        wuKong.setAllMotor(-60, 0)
    } else if (pins.digitalReadPin(DigitalPin.P1) == 1 && pins.digitalReadPin(DigitalPin.P2) == 0) {
        wuKong.setAllMotor(0, -60)
    }
})''', pkgs=('wukong',),
    ampliar=['Muestra en la pantalla hacia dónde gira.'],
    docente=P('Basado en el caso 2 del wiki de ELECFREAKS, con la misma lógica de sensores (0 sobre la línea). Si gira hacia fuera, intercambia los giros.'),
    icono='coche', tiempo='2 sesiones', etapa='P2')

proyecto(S, 'wonder-coche-esquiva', 'Wonder: coche que esquiva obstáculos', GW,
    'Montamos el coche del caso 4 con el sonar:bit: avanza y gira cuando encuentra algo delante.',
    ['Wonder Building Kit (WuKong, 2 motores, sonar:bit y piezas)', 'micro:bit', 'Cajas como obstáculos'],
    visor(WB + 'wonder-building-kit-case-04/#bricks-build-up', 'Caso 4: coche que esquiva obstáculos', '8 pasos') +
    tabla(['Componente', 'Puerto de la WuKong'], [['Motores', 'M1 y M2'], ['sonar:bit', 'P1']]),
    ['Añade las extensiones <b>wukong</b> y <code>https://github.com/elecfreaks/pxt-sonarbit</code>.',
     'Guarda la distancia del sonar:bit (P1) en %s.' % kbd('distancia'),
     'Si está entre 1 y 20 cm, gira medio segundo; si no, avanza.'],
    mc='''let distancia = 0
basic.forever(function () {
    distancia = sonarbit.sonarbit_distance(Distance_Unit.Distance_Unit_cm, DigitalPin.P1)
    if (distancia > 1 && distancia < 20) {
        wuKong.setAllMotor(-50, 60)
        basic.pause(500)
    } else {
        wuKong.setAllMotor(-80, -80)
    }
})''', pkgs=('wukong', 'sonarbit'),
    ampliar=['Haz que muestre una cara asustada al girar.'],
    docente=P('Basado en el caso 4 del wiki de ELECFREAKS (sonar:bit en P1). Se descartan las lecturas de 0 y 1 cm, que suelen ser errores.'),
    icono='coche', tiempo='2 sesiones', etapa='P2')

proyecto(S, 'wonder-puerta-automatica', 'Wonder: puerta automática', GW,
    'Como en las tiendas: la puerta se abre sola cuando alguien se acerca y se cierra a los 5 segundos.',
    ['Wonder Building Kit (WuKong, servo, sonar:bit y piezas)', 'micro:bit'],
    visor(WB + 'wonder-building-kit-case-09/#bricks-build-up', 'Caso 9: puerta automática', '22 pasos') +
    tabla(['Componente', 'Puerto de la WuKong'], [['sonar:bit', 'P1'], ['Servo', 'S0']]),
    ['Si el sonar:bit detecta algo a 8 cm o menos, muestra ✔, abre la puerta (servo a 138°), espera 5 s y ciérrala (0°).',
     'Si no, muestra ✘ y deja la puerta cerrada.'],
    mc='''basic.forever(function () {
    if (sonarbit.sonarbit_distance(Distance_Unit.Distance_Unit_cm, DigitalPin.P1) <= 8) {
        basic.showIcon(IconNames.Yes)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 138)
        basic.pause(5000)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 0)
    } else {
        basic.showIcon(IconNames.No)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 0)
        basic.pause(500)
    }
})''', pkgs=('wukong', 'sonarbit'),
    ampliar=['Cuenta cuántas personas han entrado.', 'Añade un aviso sonoro al abrir.'],
    docente=P('Basado en el caso 9 del wiki de ELECFREAKS. Su texto conecta el sonar:bit a P1, pero su programa lee P0: usad el pin donde lo hayáis conectado. '
              'Ajustad el ángulo de apertura a vuestro montaje.'),
    icono='casa', tiempo='2 sesiones', etapa='P2')

# =================================================================== SMART AGRICULTURE KIT
AG = EF + 'wisdom-life/microbit-smart-agriculture-kit/'
page(S, 'smart-agriculture-kit', 'Conoce el Smart Agriculture Kit',
    P('Kit de ELECFREAKS con sensores para proyectos de agricultura: regar, vigilar el invernadero, iluminar cultivos o controlar un estanque.') +
    h2('La placa IoT:bit') +
    P('IoT:bit es la placa de expansión del kit. Saca casi todos los pines de la micro:bit en conectores <b>GVS</b> (G tierra, V alimentación, S señal), '
      'así que cada sensor se enchufa con un solo cable de tres hilos. También lleva WiFi, reloj y zumbador. Se alimenta por USB (5 V). Pasa el ratón por los números.') +
    anat('img/kits/iotbit-foto.png', 'Foto de la placa IoT:bit', [
        (18, 35, 'Alimentación USB', 'Entrada de 5 V para toda la placa.'),
        (20, 50, 'Interruptor', 'Enciende y apaga la placa.'),
        (35, 44, 'Reloj DS1307', 'Guarda la hora (RTC).'),
        (51, 36, 'Hueco para pila CR1220', 'Mantiene la hora sin USB (pila no incluida).'),
        (71, 47, 'Módulo WiFi', 'Usa P8 y P12.'),
        (50, 52, 'Zumbador', 'En P0: suena con los bloques de Música.'),
        (50, 63, 'Ranura de la micro:bit', 'Fíjate en el sentido de inserción.'),
        (28, 76, 'Conectores GVS izquierdos', 'P1, P2, P3, P4, P6, P7 y P9 (S señal, V alimentación, G tierra).'),
        (50, 77, 'Conector I2C', 'G, V, P19 y P20: pantalla OLED.'),
        (73, 76, 'Conectores GVS derechos', 'P10, P13, P14, P15, P16, P19 y P20.'),
    ], 'IoT:bit. Foto: %s (captura).' % a(EF + 'octopus-series/expansion-board/iot-bit', 'wiki de ELECFREAKS')) +
    h2('Sensores y componentes') +
    componentes([
        ['Sensor de humedad del suelo', 'Mide si la tierra está seca (0 a 100)', 'GVS (P1 en el caso 1)'],
        ['Sensor de nivel de agua', 'Mide el agua de un depósito (0 a 100)', 'GVS (P2 en el caso 1)'],
        ['Sensor DHT11', 'Temperatura y humedad del aire', 'GVS (P1 en el caso 2)'],
        ['Sensor DS18B20 (sumergible)', 'Temperatura del agua', 'GVS (P1 en el caso 5)'],
        ['Sensor PIR', 'Detecta personas o animales en movimiento', 'GVS (P2 en el caso 4)'],
        ['Ultrasonidos sonar:bit', 'Mide distancias y alturas', 'GVS (P1 en el caso 4)'],
        ['LED de colores (Rainbow LED)', 'Luz de cultivo o avisos', 'GVS (P1 en el caso 3)'],
        ['Servo de 180°', 'Abre válvulas, compuertas o comederos', 'GVS (P9 en el caso 1)'],
        ['Pantalla OLED', 'Muestra textos y números', 'I2C'],
    ]) +
    h2('Montaje de la granja') +
    P('El caso 13 monta una granja de cartón con todos los sensores. Las prácticas de este apartado se pueden hacer sin ella, con una maceta y un vaso de agua.') +
    visor(AG + 'microbit-Smart-Agriculture-Kit-case-13#assembly', 'Caso 13: la granja inteligente', '3 pasos') +
    box('idea', 'Extensiones', P('En MakeCode, busca <b>iot-environment-kit</b> (incluye la pantalla OLED). Para el LED de colores, añade <b>neopixel</b>.')) +
    P('Fuente: %s.' % a(AG, 'wiki de ELECFREAKS')),
    group=GA, icono='planta')

proyecto(S, 'taller-smart-agriculture', 'Smart Agriculture: riego automático', GA,
    'Si la tierra está seca, un servo abre la válvula del riego; el nivel del depósito se ve en la pantalla.',
    ['Smart Agriculture Kit (IoT:bit, sensor de humedad del suelo, sensor de nivel de agua, servo)', 'micro:bit', 'Maceta y un depósito de agua'],
    tabla(['Componente', 'Puerto de la IoT:bit'], [['Sensor de humedad del suelo', 'P1'], ['Sensor de nivel de agua', 'P2'], ['Servo', 'P9']]),
    ['Añade la extensión <b>iot-environment-kit</b>.', 'Muestra el nivel del depósito con un gráfico de barras.',
     'Si la humedad del suelo baja de 30, gira el servo a 180° para regar; si no, ciérralo (0°).'],
    mc='''basic.forever(function () {
    led.plotBarGraph(Environment.ReadWaterLevel(AnalogPin.P2), 100)
    if (Environment.ReadSoilHumidity(AnalogPin.P1) < 30) {
        pins.servoWritePin(AnalogPin.P9, 180)
    } else {
        pins.servoWritePin(AnalogPin.P9, 0)
    }
    basic.pause(500)
})''', pkgs=('environment',),
    ampliar=['Muestra la humedad en la pantalla OLED.'],
    docente=P('Basado en el caso 1 del wiki de ELECFREAKS (umbral 30, servo de 0° a 180°). Calibrad el umbral con vuestra tierra: medid seca y recién regada.'),
    icono='planta', tiempo='2 sesiones', etapa='P2')

proyecto(S, 'agri-invernadero', 'Smart Agriculture: vigilante del invernadero', GA,
    'Medimos la temperatura y la humedad del aire con el DHT11 y las mostramos en la pantalla OLED. La micro:bit pone cara triste si hace demasiado calor.',
    ['IoT:bit, sensor DHT11 y pantalla OLED', 'micro:bit'],
    tabla(['Componente', 'Puerto de la IoT:bit'], [['DHT11', 'P1'], ['Pantalla OLED', 'I2C']]),
    ['Al iniciar, prepara la pantalla OLED (128 × 64).',
     'Para siempre: lee la temperatura y la humedad del DHT11 y escríbelas en la pantalla.',
     'Si la temperatura pasa de 30 °C, muestra una cara triste; si no, una alegre. Espera 5 segundos entre lecturas.'],
    mc='''let temperatura = 0
let humedad = 0
OLED.init(128, 64)
basic.forever(function () {
    temperatura = Environment.dht11value(Environment.DHT11Type.DHT11_temperature_C, DigitalPin.P1)
    basic.pause(1000)
    humedad = Environment.dht11value(Environment.DHT11Type.DHT11_humidity, DigitalPin.P1)
    OLED.clear()
    OLED.writeStringNewLine("Temp: " + temperatura + " C")
    OLED.writeStringNewLine("Humedad: " + humedad + " %")
    if (temperatura > 30) {
        basic.showIcon(IconNames.Sad)
    } else {
        basic.showIcon(IconNames.Happy)
    }
    basic.pause(5000)
})''', pkgs=('environment',),
    ampliar=['Abre una ventana con el servo si hace calor.'],
    docente=P('Basado en el caso 2 del wiki de ELECFREAKS. El DHT11 necesita al menos un segundo entre lecturas.'),
    icono='termometro', tiempo='1 sesión', etapa='P2')

proyecto(S, 'agri-luz-artificial', 'Smart Agriculture: luz para los cultivos', GA,
    'Cuando oscurece, un LED de colores da luz extra a las plantas.',
    ['IoT:bit y LED de colores (Rainbow LED)', 'micro:bit'],
    tabla(['Componente', 'Puerto de la IoT:bit'], [['LED de colores', 'P1']]),
    ['Añade la extensión <b>neopixel</b> y crea una tira de 1 LED en P1.',
     'Si el nivel de luz es menor que 100, enciende el LED en amarillo; si no, apágalo (negro).'],
    mc='''let tira = neopixel.create(DigitalPin.P1, 1, NeoPixelMode.RGB)
basic.forever(function () {
    if (input.lightLevel() < 100) {
        tira.showColor(neopixel.colors(NeoPixelColors.Yellow))
    } else {
        tira.showColor(neopixel.colors(NeoPixelColors.Black))
    }
})''', pkgs=('neopixel',),
    ampliar=['Investiga qué colores de luz aprovechan mejor las plantas y prueba con violeta.'],
    docente=P('Basado en el caso 3 del wiki de ELECFREAKS. El nivel de luz lo mide la pantalla de la micro:bit.'),
    icono='bombilla', tiempo='1 sesión', etapa='P2')

proyecto(S, 'agri-vigilante-huerto', 'Smart Agriculture: vigilante del huerto', GA,
    'Si alguien entra en el huerto, el sensor PIR lo detecta y, si además está cerca, la micro:bit da la alarma con un icono y una melodía.',
    ['IoT:bit, sonar:bit y sensor PIR', 'micro:bit'],
    tabla(['Componente', 'Puerto de la IoT:bit'], [['sonar:bit', 'P1'], ['Sensor PIR', 'P2']]),
    ['Añade la extensión <b>iot-environment-kit</b>.',
     'Guarda la distancia del sonar:bit en %s y la lectura del PIR en %s.' % (kbd('distancia'), kbd('presencia')),
     'Si la distancia está entre 10 y 100 cm y hay presencia (1), muestra un aviso y haz sonar una melodía; si no, borra la pantalla.'],
    mc='''let presencia = 0
let distancia = 0
basic.forever(function () {
    distancia = Environment.sonarbit_distance(Environment.Distance_Unit.Distance_Unit_cm, DigitalPin.P1)
    presencia = pins.digitalReadPin(DigitalPin.P2)
    if (distancia > 10 && distancia < 100 && presencia == 1) {
        basic.showIcon(IconNames.Angry)
        music.startMelody(music.builtInMelody(Melodies.BaDing), MelodyOptions.Once)
        basic.pause(1000)
    } else {
        basic.clearScreen()
    }
})''', pkgs=('environment',),
    ampliar=['Como en el caso oficial, añade el LED de colores en P9 (extensión neopixel) y enciéndelo en rojo con la alarma.', 'Cuenta cuántas veces salta la alarma.'],
    docente=P('Basado en el caso 4 del wiki de ELECFREAKS, que además enciende un LED de colores en P9. El PIR tarda unos segundos en estabilizarse al encenderlo.'),
    icono='aviso', tiempo='1-2 sesiones', etapa='P2')


# ------------------------------------------------------------------ enlace oficial al final de cada página de kit
import common as _c
_DOC = {
    GC: (EF + 'microbit-smart-car/microbit-smart-cutebot/', 'Cutebot en el wiki de ELECFREAKS', '15 casos'),
    GL: (DF_LITE, 'Maqueen Lite en el wiki de DFRobot', '16 ejemplos'),
    GP: (DF_PLUS, 'Maqueen Plus V2 en el wiki de DFRobot', '7 ejemplos'),
    GW: (WB, 'Wonder Building Kit en el wiki de ELECFREAKS', '48 modelos'),
    GA: (AG, 'Smart Agriculture Kit en el wiki de ELECFREAKS', '13 casos'),
}
for _p in _c.PAGES:
    if _p['group'] in _DOC:
        u, t_, n = _DOC[_p['group']]
        _p['body'] += box('sabias', 'Documentación oficial', P('%s: especificaciones, montaje y %s con su programa.' % (a(u, t_), n)))
