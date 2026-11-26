# -*- coding: utf-8 -*-
"""Modo experto: actividades nuevas a partir de ideas de otros materiales educativos (cada una cita de dónde sale la idea).
Textos y programas escritos para este material."""
from common import practica, P, box
from c_experto import S, J, R, C, SE, COCO
import conexiones

def idea(txt):
    return '<b>Referencia</b>: idea inspirada en %s.' % txt

ALMERIBOT = '«¿Hay continuidad?», del <i>Manual de Programación micro:bit</i> de José Francisco Muñoz (Almeribot · Microes.org)'
PEDRO = '<i>Retos de Micro:bit + MakeCode</i>, de <a href="https://github.com/pedroruizf" target="_blank" rel="noopener">Pedro Ruiz Fernández</a>'
CEIBAL = 'la actividad «Alerta cinturón» del <i>Cuaderno de proyectos micro:bit</i> de Plan Ceibal'
MBK = 'la tarjeta «Comprobador de carga de batería» de MicroBlocks (microblocks.fun, CC BY-SA 4.0)'

# =================================================================== Juegos
practica(S, 'J6', 'esquiva-asteroides', 'Esquiva los asteroides', 2, 'P2', '40 min', ['juego', 'coordenadas', 'azar'],
    'Una nave en la fila de abajo y asteroides que caen desde arriba por una columna al azar. Muévete con A y B para esquivarlos: cada asteroide esquivado suma un punto y caen cada vez más rápido.',
    ['Variables: <i>nave</i> (columna de la nave), <i>ax</i> y <i>ay</i> (posición del asteroide), <i>puntos</i> y <i>jugando</i>.',
     'Con A y B mueve la nave a izquierda y derecha sin que se salga de la pantalla.',
     'En [[para_siempre]]: [[borrar]], dibuja la nave abajo y el asteroide, y haz una [[pausa]] que se acorta con los puntos.',
     'Si el asteroide está en la fila de abajo y en la misma columna que la nave, se acaba la partida.',
     'Si llega abajo sin chocar, suma un punto y vuelve arriba en una columna [[azar]]; si no, baja una fila.'],
    ['Comprobar el choque <b>antes</b> de bajar el asteroide evita que «atraviese» la nave.',
     'En MicroBlocks las filas y columnas van de 1 a 5; en MakeCode y Python, de 0 a 4.',
     'Con %s la pausa nunca baja de 150 ms y el juego sigue siendo posible.' % '<b class="blk">máximo</b>'],
    '''let nave = 2
let ax = randint(0, 4)
let ay = 0
let puntos = 0
let jugando = true
input.onButtonPressed(Button.A, function () {
    if (nave > 0) {
        nave += -1
    }
})
input.onButtonPressed(Button.B, function () {
    if (nave < 4) {
        nave += 1
    }
})
basic.forever(function () {
    if (jugando) {
        basic.clearScreen()
        led.plot(nave, 4)
        led.plot(ax, ay)
        basic.pause(Math.max(150, 500 - puntos * 20))
        if (ay == 4 && ax == nave) {
            jugando = false
        } else if (ay == 4) {
            puntos += 1
            ay = 0
            ax = randint(0, 4)
        } else {
            ay += 1
        }
    } else {
        basic.showIcon(IconNames.Skull)
        basic.showString("Puntos")
        basic.showNumber(puntos)
    }
})''',
    "whenStarted\nnave = 3\nax = (random 1 5)\nay = 1\npuntos = 0\njugando = (booleanConstant true)\nforever {\n  if jugando {\n    '[display:mbDisplayOff]'\n    '[display:mbPlot]' nave 5\n    '[display:mbPlot]' ax ay\n    waitMillis (maximum 150 (500 - (puntos * 20)))\n    if (and (ay == 5) (ax == nave)) {\n      jugando = (booleanConstant false)\n    } (ay == 5) {\n      puntos += 1\n      ay = 1\n      ax = (random 1 5)\n    } else {\n      ay += 1\n    }\n  } else {\n    led_displayImage 'skull'\n    scroll_text ('[data:join]' 'Puntos ' puntos)\n  }\n}\n---\nwhenButtonPressed 'A'\nif (nave > 1) {\n  nave += -1\n}\n---\nwhenButtonPressed 'B'\nif (nave < 5) {\n  nave += 1\n}",
    '''from microbit import *
import random

nave, ax, ay, puntos = 2, random.randint(0, 4), 0, 0
while True:
    if button_a.was_pressed() and nave > 0:
        nave -= 1
    if button_b.was_pressed() and nave < 4:
        nave += 1
    display.clear()
    display.set_pixel(nave, 4, 9)
    display.set_pixel(ax, ay, 5)
    sleep(max(150, 500 - puntos * 20))
    if ay == 4 and ax == nave:
        break
    elif ay == 4:
        puntos += 1
        ay = 0
        ax = random.randint(0, 4)
    else:
        ay += 1
display.show(Image.SKULL)
sleep(1000)
display.scroll("Puntos " + str(puntos))''',
    ['Añade un segundo asteroide que caiga a otra velocidad.', 'Da tres vidas a la nave y muéstralas al chocar.', 'Mueve la nave inclinando la placa en lugar de con los botones.'],
    group=J, icono='cohete', fuente=idea('el reto 15, «Esquiva-enemigos», de los ' + PEDRO))

# =================================================================== Retos
practica(S, 'R7', 'detector-de-imanes', 'Detector de imanes', 2, 'P2', '35 min', ['brújula', 'sensores', 'umbral'],
    'La brújula de la micro:bit también nota los imanes. Con un imán pequeño haremos una alarma sin cables: en el cierre de un cinturón, en una puerta o en la tapa de una caja. Si el imán se aleja, suena el aviso.',
    ['En [[al_iniciar]], guarda en la variable <i>normal</i> el campo magnético sin el imán cerca: es el de la Tierra y el de lo que hay alrededor.',
     'En [[para_siempre]], guarda el campo de ahora en <i>campo</i>.',
     'Si <i>campo</i> es [[mayor]] que el doble de <i>normal</i>, el imán está cerca: muestra el sí. Si no, muestra el no y toca un [[tono]] de aviso.',
     'Con A, vuelve a medir <i>normal</i> (aleja antes el imán). Con B, muestra el valor de <i>campo</i>.',
     'Pega el imán en la parte que se mueve (la puerta, la tapa, la hebilla) y la placa en la parte fija, muy cerca.'],
    ['Comparar con «el doble de lo normal» hace que el programa funcione igual en los tres editores, aunque cada uno mida el campo en unidades distintas.',
     'Si al empezar la placa te pide inclinarla hasta llenar la pantalla de puntos, es la calibración de la brújula: hazla una vez y el programa sigue.',
     'Prueba con B a qué distancia deja de notarse el imán: con imanes pequeños, unos pocos centímetros.'],
    '''let campo = 0
let normal = input.magneticForce(Dimension.Strength)
basic.forever(function () {
    campo = input.magneticForce(Dimension.Strength)
    if (campo > normal * 2) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
        music.play(music.tonePlayable(880, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    }
})
input.onButtonPressed(Button.A, function () {
    normal = input.magneticForce(Dimension.Strength)
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(Math.round(campo))
})''',
    "whenStarted\nnormal = ('[sensors:magneticField]')\nforever {\n  campo = ('[sensors:magneticField]')\n  if (campo > (normal * 2)) {\n    led_displayImage 'yes'\n  } else {\n    led_displayImage 'no'\n    'play frequency' 880 250\n  }\n}\n---\nwhenButtonPressed 'A'\nnormal = ('[sensors:magneticField]')\n---\nwhenButtonPressed 'B'\nscroll_text campo",
    '''from microbit import *
import music

normal = compass.get_field_strength()
while True:
    campo = compass.get_field_strength()
    if button_a.was_pressed():
        normal = campo
    if button_b.was_pressed():
        display.scroll(campo)
    if campo > normal * 2:
        display.show(Image.YES)
    else:
        display.show(Image.NO)
        music.pitch(880, 250)''',
    ['Cuenta cuántas veces se ha abierto la caja.', 'Avisa por radio a otra placa en lugar de pitar.', 'Investiga qué objetos de clase tienen imán (estuches, tablets, altavoces).'],
    group=R, icono='brujula', materiales=['Un imán pequeño (de nevera o de neodimio)', 'Cinta adhesiva'],
    nota=box('ojo', 'Cuidado con los imanes', P('Los imanes de neodimio son muy fuertes: mantenlos lejos de tarjetas, móviles y marcapasos, y no los dejes al alcance de quien pueda tragárselos.')), fuente=idea(CEIBAL))

# =================================================================== Cables de cocodrilo
practica(S, 'C5', 'conduce-la-electricidad', '¿Conduce la electricidad?', 1, 'P2', '30 min', ['entradas digitales', 'ciencia'],
    'Un detector de conductores: pon las dos pinzas sobre un objeto y la placa dirá si deja pasar la corriente. Sirve para clasificar materiales en clase de Ciencias.',
    ['Conecta un cable a P0 y otro a GND. Las dos pinzas libres son las puntas del detector.',
     'Al empezar, activa la resistencia interna de P0 hacia arriba: así P0 vale 1 si no toca nada.',
     'En [[para_siempre]], lee P0 con [[pin_digital]]. Si vale 0, las pinzas están unidas por un conductor: muestra el sí y toca un [[tono]] agudo.',
     'Si vale 1, muestra el no.',
     'Prueba primero juntando las dos pinzas (sí) y separándolas (no). Después, prueba objetos: haz una tabla con los que conducen y los que no.'],
    ['Conducen bien los <b>metales</b>: clips, monedas, papel de aluminio, llaves. No conducen el plástico, la madera seca, la goma ni el papel.',
     'Algunos materiales conducen poco (una línea gruesa de lápiz, agua con sal, una fruta): puede que el detector no los note. No es que no conduzcan nada, sino que dejan pasar muy poca corriente.',
     'Usa solo objetos sueltos: nunca enchufes, aparatos ni pilas.'],
    '''pins.setPull(DigitalPin.P0, PinPullMode.PullUp)
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P0) == 0) {
        basic.showIcon(IconNames.Yes)
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    } else {
        basic.showIcon(IconNames.No)
    }
})''',
    "whenStarted\nforever {\n  if (not (digitalReadOp 0 'up')) {\n    led_displayImage 'yes'\n    'play frequency' 988 120\n  } else {\n    led_displayImage 'no'\n  }\n}",
    '''from microbit import *
import music

pin0.set_pull(pin0.PULL_UP)
while True:
    if pin0.read_digital() == 0:
        display.show(Image.YES)
        music.pitch(988, 120)
    else:
        display.show(Image.NO)''',
    ['Cuenta con A cuántos objetos conductores has encontrado.', 'Dibuja con lápiz blando una línea muy gruesa en un papel y busca hasta qué longitud la detecta.'],
    conexion=conexiones.conduce(), group=C, icono='rayo', materiales=[COCO + ' (2)', 'Objetos para probar: clip, moneda, goma, lápiz, cuchara de madera, papel de aluminio…'],
    fuente=idea(ALMERIBOT))

practica(S, 'C6', 'comprobador-de-pilas', 'Comprobador de pilas', 2, 'ESO', '40 min', ['entradas analógicas', 'voltaje', 'condicionales'],
    'Medir si una pila de 1,5 V está nueva o gastada. La micro:bit lee el voltaje por un pin y lo muestra con un icono y, al pulsar A, en milivoltios.',
    ['Conecta un cable a GND y otro a P1. Entre el cable de P1 y la pila pon una resistencia de 1 kΩ: protege el pin si te equivocas de polo.',
     'Toca con el cable de GND el polo − de la pila y con el de la resistencia el polo +.',
     'En [[para_siempre]], lee P1 con [[pin_leer]] (de 0 a 1023) y conviértelo en milivoltios: lectura × 3300 ÷ 1023.',
     'Con [[si_no]]: más de 1400 mV, pila buena (sí); más de 1200 mV, a medias (dormida); menos, gastada (no).',
     'En [[boton]] A, muestra los milivoltios.'],
    ['La micro:bit compara la entrada con su propia alimentación, unos 3,3 V por USB. Por eso 1023 equivale a unos 3300 mV. Conéctala por USB para que la medida sea más fiable.',
     'Una pila alcalina nueva da algo más de 1,5 V; por debajo de 1,2 V ya está casi gastada.',
     'Sin pila, el pin queda «al aire» y la lectura puede bailar: no le hagas caso.'],
    '''let mv = 0
basic.forever(function () {
    mv = Math.round(pins.analogReadPin(AnalogPin.P1) * 3300 / 1023)
    if (mv > 1400) {
        basic.showIcon(IconNames.Yes)
    } else if (mv > 1200) {
        basic.showIcon(IconNames.Asleep)
    } else {
        basic.showIcon(IconNames.No)
    }
    basic.pause(200)
})
input.onButtonPressed(Button.A, function () {
    basic.showNumber(mv)
})''',
    "whenStarted\nforever {\n  mv = (((analogReadOp 1) * 3300) / 1023)\n  if (mv > 1400) {\n    led_displayImage 'yes'\n  } (mv > 1200) {\n    led_displayImage 'asleep'\n  } else {\n    led_displayImage 'no'\n  }\n  waitMillis 200\n}\n---\nwhenButtonPressed 'A'\nscroll_text mv",
    '''from microbit import *

while True:
    mv = pin1.read_analog() * 3300 // 1023
    if button_a.was_pressed():
        display.scroll(mv)
    if mv > 1400:
        display.show(Image.YES)
    elif mv > 1200:
        display.show(Image.ASLEEP)
    else:
        display.show(Image.NO)
    sleep(200)''',
    ['Muestra una barra de 0 a 5 filas según la carga.', 'Mide las pilas usadas de la clase y haz una gráfica con los resultados.'],
    conexion=conexiones.pila(), group=C, icono='bateria', materiales=[COCO + ' (2)', 'Una resistencia de 1 kΩ', 'Pilas sueltas de 1,5 V (AA o AAA) nuevas y usadas'],
    nota=box('ojo', 'Solo pilas de 1,5 V', P('Prueba <b>solo una pila de 1,5 V cada vez</b> (AA, AAA, C o D). Nunca pilas de 9 V, pilas en serie, baterías de litio ni cargadores: '
        'superan los 3,3 V que aguanta el pin y pueden estropear la placa. Repasa <a href="../conoce/precauciones.html">Precauciones y cuidados</a>.')), fuente=idea(MBK))

# =================================================================== Sensores externos
practica(S, 'S4', 'aparcamiento', 'Aparcamiento con barrera', 3, 'ESO', '50 min', ['servomotor', 'variables', 'contador'],
    'Un aparcamiento de juguete con tres plazas: la pantalla muestra las plazas libres y un servo hace de barrera. A es un coche que entra y B, uno que sale. Si está lleno, la barrera no se abre.',
    ['Conecta el servo como en «Servo que saluda»: marrón a GND, rojo a 3V y naranja a P0. Pégale un palito o una tira de cartulina como barrera.',
     'Al empezar: la variable <i>plazas</i> vale 3, la barrera baja (0°) y se muestran las plazas.',
     'En [[boton]] A: si quedan plazas, resta una, sube la barrera (90°), espera 2 segundos y bájala. Si no quedan, muestra el no y un [[tono]] grave.',
     'En [[boton]] B: si hay menos de 3 plazas libres, suma una y abre la barrera igual.',
     'Al final de cada botón, muestra las plazas.'],
    ['El programa no deja que las plazas bajen de 0 ni pasen de 3: así el contador nunca miente.',
     'En MicroBlocks el servo va de −90° a 90°: la barrera bajada es −90 y subida, 0.',
     'Abrir y cerrar la barrera se repite en los dos botones: en Python lo hemos guardado en una función.'],
    '''let plazas = 3
pins.servoWritePin(AnalogPin.P0, 0)
basic.showNumber(plazas)
input.onButtonPressed(Button.A, function () {
    if (plazas > 0) {
        plazas += -1
        pins.servoWritePin(AnalogPin.P0, 90)
        basic.pause(2000)
        pins.servoWritePin(AnalogPin.P0, 0)
    } else {
        basic.showIcon(IconNames.No)
        music.play(music.tonePlayable(196, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    }
    basic.showNumber(plazas)
})
input.onButtonPressed(Button.B, function () {
    if (plazas < 3) {
        plazas += 1
        pins.servoWritePin(AnalogPin.P0, 90)
        basic.pause(2000)
        pins.servoWritePin(AnalogPin.P0, 0)
    }
    basic.showNumber(plazas)
})''',
    "whenStarted\nplazas = 3\nsetServoAngle 0 -90\nscroll_text plazas\n---\nwhenButtonPressed 'A'\nif (plazas > 0) {\n  plazas += -1\n  setServoAngle 0 0\n  waitMillis 2000\n  setServoAngle 0 -90\n} else {\n  led_displayImage 'no'\n  'play frequency' 196 500\n}\nscroll_text plazas\n---\nwhenButtonPressed 'B'\nif (plazas < 3) {\n  plazas += 1\n  setServoAngle 0 0\n  waitMillis 2000\n  setServoAngle 0 -90\n}\nscroll_text plazas",
    '''from microbit import *
import music

pin0.set_analog_period(20)

def angulo(grados):
    # de 0-180 grados a impulsos de 0,5-2,5 ms (valores de 26 a 128)
    pin0.write_analog(26 + grados * 102 // 180)

def abrir_barrera():
    angulo(90)
    sleep(2000)
    angulo(0)

plazas = 3
angulo(0)
display.show(plazas)
while True:
    if button_a.was_pressed():
        if plazas > 0:
            plazas -= 1
            abrir_barrera()
        else:
            display.show(Image.NO)
            music.pitch(196, 500)
        display.show(plazas)
    if button_b.was_pressed():
        if plazas < 3:
            plazas += 1
            abrir_barrera()
        display.show(plazas)''',
    ['Detecta los coches con el sensor de luz: cuando un coche tapa la placa, se abre la barrera.', 'Usa dos placas y la radio: una en la entrada y otra en la salida.', 'Construye la maqueta del aparcamiento con cartón.'],
    conexion=conexiones.servo(), group=SE, icono='coche', materiales=[COCO + ' (3) o cables macho para el conector del servo', 'Un microservo SG90', 'Cartón, palitos y cinta para la maqueta'],
    fuente=idea('los retos 20, «Contador de coches en parking», y 21, «Control de barrera servomotor con luz», de los ' + PEDRO))
