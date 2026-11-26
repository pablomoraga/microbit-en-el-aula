# -*- coding: utf-8 -*-
"""Talleres: proyectos tipo y kits de ELECFREAKS y DFRobot."""
import conexiones, kits
from common import page, proyecto, P, ul, ol, box, tabla, h2, kbd
import makecode

S = 'talleres'
G1, G2 = 'Proyectos tipo', 'Kits y robots'
GRUPOS = {
    G1: P('Seis proyectos completos que se construyen con la placa y pocos componentes. Sirven como proyecto final de trimestre o como reto por equipos. '
          'Cada uno se puede repartir en fases: diseño en papel, montaje, programación, prueba y presentación.'),
    G2: P('Talleres con productos concretos. Usan las extensiones oficiales de cada fabricante (comprobadas en su documentación y en su código). '
          'Empieza por la página <b>Extensiones y bibliotecas de los kits</b>.'),
}
DOC_FASES = ul(['<b>10 min</b>: presentación del reto y del material.', '<b>15 min</b>: diseño en papel (qué mide, qué decide, qué hace).',
                '<b>25 min</b>: montaje y programación por fases.', '<b>10 min</b>: prueba, mejora y presentación al grupo.'])

# =================================================================== Proyectos tipo
proyecto(S, 'invernadero-inteligente', 'Invernadero inteligente', G1,
    'Un invernadero de cartón o una caja de plástico transparente que vigila sus plantas: mide la humedad de la tierra, la temperatura y la luz, '
    'avisa cuando hay que regar y abre una ventana con un servo si hace demasiado calor.',
    ['micro:bit V2 con portapilas', 'Dos clavos para medir la humedad (práctica S1) o un sensor de humedad del suelo', 'Microservo SG90', 'Cables de cocodrilo', 'Caja, cartón y una planta'],
    conexiones.invernadero() + tabla(['Componente', 'Conexión'], [['Clavos de humedad', 'uno a 3V, el otro a P1'], ['Servo (ventana)', 'señal a P0, rojo a 3V, marrón a GND']]),
    ['Construye el invernadero y fija la placa en un lugar visible.', 'Programa la lectura de la humedad y elige el umbral (con tierra seca y regada).',
     'Si la tierra está seca, muestra una gota y pita.', 'Si la temperatura supera 28 °C, abre la ventana (servo a 90°); si baja de 24 °C, ciérrala.',
     'Con A, muestra la temperatura; con B, la humedad.'],
    mc='''basic.forever(function () {
    if (pins.analogReadPin(AnalogPin.P1) < 300) {
        basic.showLeds(`
            . . # . .
            . # # # .
            # # # # #
            # # # # #
            . # # # .
            `)
        music.play(music.tonePlayable(440, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    } else {
        basic.showIcon(IconNames.Happy)
    }
    if (input.temperature() > 28) {
        pins.servoWritePin(AnalogPin.P0, 90)
    } else if (input.temperature() < 24) {
        pins.servoWritePin(AnalogPin.P0, 0)
    }
    basic.pause(2000)
})
input.onButtonPressed(Button.A, function () {
    basic.showNumber(input.temperature())
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(pins.analogReadPin(AnalogPin.P1))
})''',
    mb='''whenStarted
forever {
  if ((analogReadOp 1) < 300) {
    '[display:mbDisplay]' 15728068
    'play frequency' 440 120
  } else {
    led_displayImage 'happy'
  }
  if (('[sensors:temperature]') > 28) {
    setServoAngle 0 0
  } (('[sensors:temperature]') < 24) {
    setServoAngle 0 -90
  }
  waitMillis 2000
}
---
whenButtonPressed 'A'
scroll_text ('[sensors:temperature]')
---
whenButtonPressed 'B'
scroll_text (analogReadOp 1)''',
    py='''from microbit import *
import music

GOTA = Image("00900:09990:99999:99999:09990")
pin0.set_analog_period(20)

def ventana(grados):
    pin0.write_analog(26 + grados * 102 // 180)

ultimo = 0
while True:
    if running_time() - ultimo > 2000:
        ultimo = running_time()
        if pin1.read_analog() < 300:
            display.show(GOTA)
            music.pitch(440, 120)
        else:
            display.show(Image.HAPPY)
        if temperature() > 28:
            ventana(90)
        elif temperature() < 24:
            ventana(0)
    if button_a.was_pressed():
        display.scroll(temperature())
    if button_b.was_pressed():
        display.scroll(pin1.read_analog())''',
    ampliar=['Envía los datos por radio a una placa en clase.', 'Añade una bomba de agua con un relé y una placa de expansión (con ayuda de un adulto).'],
    docente=P('Usamos dos umbrales para la ventana (28 y 24 °C) para que no esté abriéndose y cerrándose sin parar. Es una buena ocasión para hablar de la <b>histéresis</b>, que usan los termostatos reales.') + DOC_FASES,
    icono='planta', tiempo='2 sesiones', etapa='P2')

proyecto(S, 'estacion-meteorologica', 'Estación meteorológica', G1,
    'Una estación que mide temperatura, luz y ruido, muestra los datos en rotación y los envía por radio a una placa «panel» situada en otra parte del aula.',
    ['Dos micro:bits V2', 'Portapilas para la estación', 'Una caja con agujeros para protegerla (puede imprimirse en 3D)'],
    None,
    ['Programa la estación: cada 5 segundos envía por radio la temperatura, la luz y el ruido con un nombre para cada dato.',
     'Programa el panel: al recibir cada dato, lo guarda; con A muestra la temperatura, con B la luz y con el logotipo el ruido.',
     'Coloca la estación en la ventana o en el patio y compara los datos con los de una web meteorológica.'],
    mc='''radio.setGroup(10)
basic.forever(function () {
    radio.sendValue("t", input.temperature())
    radio.sendValue("luz", input.lightLevel())
    radio.sendValue("ruido", input.soundLevel())
    basic.showIcon(IconNames.Umbrella)
    basic.pause(5000)
})''',
    mb='''whenStarted
'[radio:setGroup]' 10
forever {
  '[radio:sendPair]' 't' ('[sensors:temperature]')
  '[radio:sendPair]' 'luz' ('[display:lightLevel]')
  '[radio:sendPair]' 'ruido' (loudness)
  led_displayImage 'umbrella'
  waitMillis 5000
}''',
    py='''from microbit import *
import radio

radio.on()
radio.config(group=10)
while True:
    radio.send("t=" + str(temperature()))
    radio.send("luz=" + str(display.read_light_level()))
    radio.send("ruido=" + str(microphone.sound_level()))
    display.show(Image.UMBRELLA)
    sleep(5000)''',
    extra=box('idea', 'El programa del panel', P('Con MakeCode, el panel usa %s: si el nombre es «t», guarda el valor en la variable <i>temperatura</i>, y así con cada dato. '
        'En Python, separa el texto recibido por el signo «=» con <code>mensaje.split("=")</code>.' % kbd('al recibir radio nombre valor'))),
    ampliar=['Registra los datos (MakeCode: extensión <b>datalogger</b>; Python: módulo <code>log</code>) y haz gráficas.', 'Añade un sensor de humedad del aire con un kit.'],
    docente=P('Este proyecto conecta con Ciencias de la Naturaleza y Matemáticas (tablas, gráficas, medias). La temperatura de la micro:bit es aproximada: contrastadla con un termómetro.') + DOC_FASES,
    icono='nube', tiempo='2 sesiones', etapa='ESO')

proyecto(S, 'semaforo-inteligente', 'Cruce con semáforo inteligente', G1,
    'Un cruce de maqueta con semáforo de coches (LED externos) y pulsador de peatones (botón A). Al pulsar, el semáforo de coches pasa a rojo y la pantalla muestra al peatón cruzando.',
    ['micro:bit', 'LED rojo, amarillo y verde con resistencias de 220 Ω', 'Cables de cocodrilo', 'Maqueta de cartón'],
    conexiones.semaforo() + tabla(['LED', 'Pin'], [['Rojo', 'P0'], ['Amarillo', 'P1'], ['Verde', 'P2'], ['Patas cortas', 'GND']]),
    ['Monta los LED como en la práctica C2.', 'Por defecto, el semáforo de coches está en verde.',
     'Al pulsar A: amarillo 2 s, rojo, muestra el muñeco y cuenta atrás de 5 s para los peatones.', 'Vuelve a verde.'],
    mc='''pins.digitalWritePin(DigitalPin.P2, 1)
input.onButtonPressed(Button.A, function () {
    pins.digitalWritePin(DigitalPin.P2, 0)
    pins.digitalWritePin(DigitalPin.P1, 1)
    basic.pause(2000)
    pins.digitalWritePin(DigitalPin.P1, 0)
    pins.digitalWritePin(DigitalPin.P0, 1)
    basic.showIcon(IconNames.StickFigure)
    basic.pause(2000)
    for (let i = 0; i <= 4; i++) {
        basic.showNumber(5 - i)
        music.play(music.tonePlayable(880, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.UntilDone)
    }
    basic.clearScreen()
    pins.digitalWritePin(DigitalPin.P0, 0)
    pins.digitalWritePin(DigitalPin.P2, 1)
})''',
    mb='''whenStarted
digitalWriteOp 2 true
---
whenButtonPressed 'A'
digitalWriteOp 2 false
digitalWriteOp 1 true
waitMillis 2000
digitalWriteOp 1 false
digitalWriteOp 0 true
led_displayImage 'stick figure'
waitMillis 2000
for i 5 {
  scroll_text (6 - i)
  'play frequency' 880 60
}
'[display:mbDisplayOff]'
digitalWriteOp 0 false
digitalWriteOp 2 true''',
    py='''from microbit import *
import music

pin2.write_digital(1)
while True:
    if button_a.was_pressed():
        pin2.write_digital(0)
        pin1.write_digital(1)
        sleep(2000)
        pin1.write_digital(0)
        pin0.write_digital(1)
        display.show(Image.STICKFIGURE)
        sleep(2000)
        for i in range(5, 0, -1):
            display.show(i)
            music.pitch(880, 60)
            sleep(700)
        display.clear()
        pin0.write_digital(0)
        pin2.write_digital(1)''',
    ampliar=['Añade un segundo semáforo coordinado por radio.', 'Programa un modo nocturno con el amarillo parpadeando cuando haya poca luz.'],
    docente=P('Ideal para Educación Vial. Se puede organizar por equipos: uno diseña la maqueta, otro el circuito y otro el programa.') + DOC_FASES,
    icono='semaforo', tiempo='1-2 sesiones', etapa='P2')

proyecto(S, 'casa-segura', 'Casa segura', G1,
    'Una alarma para una casa de cartón: vigila la puerta con un interruptor de aluminio y la luz de una habitación. Se desactiva con una clave secreta de botones.',
    ['micro:bit V2', 'Papel de aluminio y cables de cocodrilo (interruptor de puerta en P1 y GND)', 'Casa de cartón'],
    None,
    ['Monta el interruptor de la puerta como en la práctica C4.', 'Si la alarma está activa y la puerta se abre o se enciende la luz dentro de la casa a oscuras, suena la sirena.',
     'Para desactivarla hay que pulsar la clave: A, A, B.', 'El logotipo vuelve a activarla.'],
    mc='''let activa = true
let clave = ""
pins.setPull(DigitalPin.P1, PinPullMode.PullUp)
input.onButtonPressed(Button.A, function () {
    clave = clave + "A"
})
input.onButtonPressed(Button.B, function () {
    clave = clave + "B"
    if (clave == "AAB") {
        activa = false
        basic.showIcon(IconNames.No)
    }
    clave = ""
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    activa = true
    basic.showIcon(IconNames.Yes)
})
basic.forever(function () {
    if (activa && pins.digitalReadPin(DigitalPin.P1) == 1) {
        basic.showIcon(IconNames.Skull)
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(784, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    }
})''',
    mb='''whenStarted
activa = (booleanConstant true)
clave = ''
forever {
  if (and activa ((digitalReadOp 1 'up') == true)) {
    led_displayImage 'skull'
    'play frequency' 988 250
    'play frequency' 784 250
  }
}
---
whenButtonPressed 'A'
clave = ('[data:join]' clave 'A')
---
whenButtonPressed 'B'
clave = ('[data:join]' clave 'B')
if (clave == 'AAB') {
  activa = (booleanConstant false)
  led_displayImage 'no'
}
clave = ''
---
whenCondition (touchPin_logoTouched)
activa = (booleanConstant true)
led_displayImage 'yes\'''',
    py='''from microbit import *
import music

pin1.set_pull(pin1.PULL_UP)
activa = True
clave = ""
while True:
    if button_a.was_pressed():
        clave += "A"
    if button_b.was_pressed():
        clave += "B"
        if clave == "AAB":
            activa = False
            display.show(Image.NO)
        clave = ""
    if pin_logo.is_touched():
        activa = True
        display.show(Image.YES)
    if activa and pin1.read_digital() == 1:
        display.show(Image.SKULL)
        music.pitch(988, 250)
        music.pitch(784, 250)''',
    ampliar=['Avisa por radio a una placa «móvil» del dueño.', 'Cambia la clave por un patrón de inclinaciones de la placa.'],
    docente=P('Introduce la idea de <b>contraseña</b> y de <b>seguridad</b>: ¿cuántas claves de tres pulsaciones hay? (2 × 2 × 2 = 8). ¿Y de cinco? Es fácil adivinar una clave corta.') + DOC_FASES,
    icono='casa', tiempo='1-2 sesiones', etapa='P2')

proyecto(S, 'votacion-por-radio', 'Votación por radio', G1,
    'Toda la clase vota con su micro:bit: A es «sí» y B es «no». La placa del profesorado cuenta los votos y muestra el resultado al tocar el logotipo.',
    ['Una micro:bit por alumno o pareja (votantes) y una para el profesorado (urna)'],
    None,
    ['Programa de los votantes: A envía 1 y muestra el sí; B envía 0 y muestra el no.',
     'Programa de la urna: al recibir 1 suma a <i>si</i>; al recibir 0, a <i>no</i>.',
     'Al tocar el logotipo de la urna, muestra los dos totales. Con A+B, pone los contadores a cero.'],
    mc='''radio.setGroup(20)
let si = 0
let no = 0
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(1)
    basic.showIcon(IconNames.Yes)
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(0)
    basic.showIcon(IconNames.No)
})
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        si += 1
    } else {
        no += 1
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showString("SI")
    basic.showNumber(si)
    basic.showString("NO")
    basic.showNumber(no)
})
input.onButtonPressed(Button.AB, function () {
    si = 0
    no = 0
})''',
    mb='''whenStarted
'[radio:setGroup]' 20
si = 0
no = 0
---
whenButtonPressed 'A'
'[radio:sendInteger]' 1
led_displayImage 'yes'
---
whenButtonPressed 'B'
'[radio:sendInteger]' 0
led_displayImage 'no'
---
whenCondition ('[radio:messageReceived]')
if (('[radio:receivedInteger]') == 1) {
  si += 1
} else {
  no += 1
}
---
whenCondition (touchPin_logoTouched)
scroll_text ('[data:join]' 'SI ' si ' NO ' no)''',
    py='''from microbit import *
import radio

radio.on()
radio.config(group=20)
si = no = 0
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        si = no = 0
    elif button_a.was_pressed():
        radio.send("1")
        display.show(Image.YES)
    elif button_b.was_pressed():
        radio.send("0")
        display.show(Image.NO)
    voto = radio.receive()
    if voto == "1":
        si += 1
    elif voto == "0":
        no += 1
    if pin_logo.is_touched():
        display.scroll("SI " + str(si) + " NO " + str(no))''',
    extra=box('ojo', 'Un mismo programa para todas', P('Todas las placas llevan el mismo programa: cualquiera puede votar y cualquiera puede contar. Para usarlo como urna basta con tocar su logotipo.')),
    ampliar=['Evita que alguien vote dos veces (cada placa solo puede enviar un voto hasta el reinicio).', 'Haz una encuesta con tres opciones (A, B y logotipo).'],
    docente=P('Sirve para hablar de democracia, privacidad del voto y fiabilidad: ¿qué pasa si alguien pulsa muchas veces? ¿Cómo lo resolverían las elecciones reales?') + DOC_FASES,
    icono='antena', tiempo='1 sesión', etapa='P2')

proyecto(S, 'orquesta', 'Orquesta micro:bit', G1,
    'Una placa hace de directora y marca el compás por radio; cada placa músico toca su nota en cada compás. Juntas forman acordes y melodías.',
    ['Varias micro:bits V2 (una directora y varias músicas)'],
    None,
    ['La directora: al pulsar A empieza a enviar un número cada medio segundo (1, 2, 3, 4, 1, 2…).',
     'Cada música elige su nota con B (Do, Mi o Sol) y la muestra.',
     'Al recibir un 1 o un 3, la música toca su nota. Así sonarán todas a la vez, como un acorde.'],
    mc='''radio.setGroup(30)
let notas = [262, 330, 392]
let mia = 0
let tocando = false
let tiempo = 1
input.onButtonPressed(Button.A, function () {
    tocando = !(tocando)
})
input.onButtonPressed(Button.B, function () {
    mia = (mia + 1) % 3
    basic.showNumber(mia + 1)
})
basic.forever(function () {
    if (tocando) {
        radio.sendNumber(tiempo)
        basic.showNumber(tiempo)
        tiempo = tiempo % 4 + 1
        basic.pause(500)
    }
})
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1 || receivedNumber == 3) {
        music.play(music.tonePlayable(notas[mia], music.beat(BeatFraction.Quarter)), music.PlaybackMode.InBackground)
    }
})''',
    mb='''whenStarted
'[radio:setGroup]' 30
notas = ('[data:makeList]' 262 330 392)
mia = 1
tocando = (booleanConstant false)
tiempo = 1
forever {
  if tocando {
    '[radio:sendInteger]' tiempo
    scroll_text tiempo
    tiempo = ((tiempo % 4) + 1)
    waitMillis 500
  }
}
---
whenButtonPressed 'A'
tocando = (not tocando)
---
whenButtonPressed 'B'
mia = ((mia % 3) + 1)
scroll_text mia
---
whenCondition ('[radio:messageReceived]')
golpe = ('[radio:receivedInteger]')
if (or (golpe == 1) (golpe == 3)) {
  'play frequency' (at mia notas) 250
}''',
    py='''from microbit import *
import radio
import music

radio.on()
radio.config(group=30)
notas = [262, 330, 392]
mia = 0
tocando = False
tiempo = 1
ultimo = 0
while True:
    if button_a.was_pressed():
        tocando = not tocando
    if button_b.was_pressed():
        mia = (mia + 1) % 3
        display.show(mia + 1)
    if tocando and running_time() - ultimo > 500:
        ultimo = running_time()
        radio.send(str(tiempo))
        display.show(tiempo)
        tiempo = tiempo % 4 + 1
    golpe = radio.receive()
    if golpe in ("1", "3"):
        music.pitch(notas[mia], 250, wait=False)''',
    ampliar=['Que la directora envíe también la nota que debe tocar cada grupo y así interpretar una canción.', 'Cambia el tempo con la inclinación de la placa directora.'],
    docente=P('Una placa directora no recibe sus propios mensajes, así que no suena: es perfecta para el profesorado. Funciona bien con grupos de 3 a 12 placas.') + DOC_FASES,
    icono='musica', tiempo='1 sesión', etapa='ESO')

# =================================================================== Kits
EXT_ROWS = [
    ['<b>Cutebot</b> (ELECFREAKS)', '<code>cutebot</code> · <a href="https://github.com/elecfreaks/pxt-cutebot" target="_blank" rel="noopener">github.com/elecfreaks/pxt-cutebot</a>', 'Biblioteca <b>Cutebot</b> (Robots)'],
    ['<b>Maqueen</b> (DFRobot)', '<code>maqueen</code> · <a href="https://github.com/DFRobot/pxt-maqueen" target="_blank" rel="noopener">github.com/DFRobot/pxt-maqueen</a>', 'Biblioteca <b>Maqueen</b> (Robots)'],
    ['<b>Maqueen Plus V2</b> (DFRobot)', 'Pega <code>https://github.com/DFRobot/pxt-DFRobot_MaqueenPlus_v20</code>', 'No hay biblioteca específica: usa MakeCode'],
    ['<b>Wonder Building Kit</b> (ELECFREAKS, placa WuKong)', '<code>wukong</code> · <a href="https://github.com/elecfreaks/pxt-wukong" target="_blank" rel="noopener">github.com/elecfreaks/pxt-wukong</a>; para el ultrasonido, <code>https://github.com/elecfreaks/pxt-sonarbit</code>', 'Biblioteca <b>Wukong</b> (Kits y placas)'],
    ['<b>Smart Agriculture Kit</b> (ELECFREAKS, placa IoT:bit)', '<code>iot-environment-kit</code> · <a href="https://github.com/elecfreaks/pxt-iot-environment-kit" target="_blank" rel="noopener">github.com/elecfreaks/pxt-iot-environment-kit</a>; además <code>neopixel</code> y <code>servo</code>', 'Sensores con bloques de Pines (lectura analógica)'],
]
page(S, 'extensiones-de-los-kits', 'Extensiones y bibliotecas de los kits', P(
    'Cada kit necesita sus propios bloques. Esta tabla reúne lo que hay que añadir en cada editor antes de empezar. En MakeCode, pulsa <b>Extensiones</b> y escribe el nombre en el buscador '
    '(o pega la dirección de GitHub cuando se indica). En MicroBlocks, pulsa <b>Añadir biblioteca</b> y busca en la carpeta indicada.') +
    tabla(['Kit', 'MakeCode (extensión)', 'MicroBlocks'], EXT_ROWS) +
    box('ojo', 'Comprueba la versión de tu robot', P('Los robots cambian de versión y cada versión puede tener su extensión (por ejemplo, Maqueen Lite, Maqueen Plus y Maqueen Plus V2). '
        'Mira la pegatina o la placa de tu robot y, ante la duda, sigue la documentación del fabricante: '
        '<a href="https://wiki.elecfreaks.com/en/microbit/" target="_blank" rel="noopener">wiki de ELECFREAKS</a> y <a href="https://wiki.dfrobot.com" target="_blank" rel="noopener">wiki de DFRobot</a>.')) +
    box('idea', 'Python', P('Los fabricantes ofrecen bibliotecas de MicroPython para algunos robots (por ejemplo, Cutebot), pero los talleres de este apartado usan MakeCode, que es lo que documentan sus guías.')),
    group=G2, icono='pieza')

proyecto(S, 'taller-cutebot', 'Cutebot: sigue la línea y esquiva obstáculos', G2,
    'Cutebot es un coche robot de ELECFREAKS con dos motores, sensor de ultrasonidos, dos sensores de línea y faros de colores. En este taller lo programamos para seguir una línea negra y para frenar ante obstáculos.',
    ['Robot Cutebot con su micro:bit', 'Pilas para el robot', 'Cinta aislante negra sobre un suelo claro (circuito)'],
    kits.cutebot() + tabla(['Elemento', 'Dónde está'], [['Sensores de línea', 'Abajo, delante (P13 izquierdo y P14 derecho)'], ['Ultrasonidos', 'Delante (P8 y P12)'], ['Faros RGB', 'Controlados por la placa del robot (I2C)']]),
    ['Añade la extensión <b>cutebot</b>.', 'Prueba los motores: avanza 2 segundos y para.',
     'Con A, activa el modo <b>seguir la línea</b>: si los dos sensores ven línea, recto; si solo la ve el izquierdo, gira a la izquierda; si solo el derecho, a la derecha.',
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
    ampliar=['Ajusta la velocidad: ¿cuál es la más rápida a la que no se sale?', 'Haz una carrera de seguidores de línea por equipos.'],
    docente=P('Basado en las funciones de la extensión oficial <code>pxt-cutebot</code>. Si el robot se sale en las curvas, baja la velocidad: los sensores necesitan tiempo para detectar la línea.'),
    icono='coche', tiempo='2 sesiones', etapa='P2')

proyecto(S, 'taller-maqueen', 'Maqueen: robot que esquiva obstáculos', G2,
    'Maqueen (Lite) es un robot de DFRobot para la micro:bit. Lo programamos para avanzar, detectar obstáculos con el ultrasonido, encender sus LED y girar para esquivarlos.',
    ['Robot Maqueen con su micro:bit y el sensor de ultrasonidos montado', 'Pilas para el robot', 'Cajas o libros como obstáculos'],
    kits.maqueen_lite(),
    ['Añade la extensión <b>maqueen</b>.', 'Lee la distancia del ultrasonido y muéstrala para comprobar que funciona.',
     'Si la distancia es mayor que 15 cm, avanza con los LED apagados.', 'Si es menor, enciende los LED, retrocede un poco y gira hacia un lado.'],
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
    docente=P('Basado en las funciones de la extensión oficial <code>pxt-maqueen</code> (motor M1 = izquierdo, M2 = derecho). Si tu Maqueen es de una versión más nueva, revisa la extensión en la página de extensiones.'),
    icono='robot', tiempo='1 sesión', etapa='P2')

proyecto(S, 'taller-maqueen-plus', 'Maqueen Plus V2: seguidor de línea', G2,
    'Maqueen Plus V2 tiene cinco sensores de línea, faros, LED RGB y conector para ultrasonidos. Lo programamos para seguir una línea con el sensor central y los dos interiores.',
    ['Robot Maqueen Plus V2 con su micro:bit', 'Pilas para el robot', 'Circuito de cinta negra'],
    kits.maqueen_plus(),
    ['Añade la extensión pegando <code>https://github.com/DFRobot/pxt-DFRobot_MaqueenPlus_v20</code> en el buscador de extensiones.',
     'Al iniciar, llama a %s.' % kbd('I2CInit'),
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
    ampliar=['Usa también los sensores exteriores (L2 y R2) para las curvas cerradas.', 'Enciende los faros con %s cuando corrija la dirección.' % kbd('control left led light')],
    docente=P('Adaptado del ejemplo de seguimiento de línea de la extensión oficial <code>pxt-DFRobot_MaqueenPlus_v20</code>, en el que el estado 1 indica que el sensor detecta la línea.'),
    icono='robot', tiempo='1-2 sesiones', etapa='ESO')

proyecto(S, 'taller-wonder-building', 'Wonder Building Kit: la moto', G2,
    'El Wonder Building Kit de ELECFREAKS combina piezas de construcción compatibles con LEGO, la placa de expansión WuKong y motores. Construimos la moto del caso 1 de su guía y la programamos con los botones.',
    ['Wonder Building Kit (placa WuKong, motores y piezas)', 'micro:bit', 'Instrucciones de montaje del caso «The Motorcycle» en el wiki de ELECFREAKS'],
    kits.wonder_moto() + tabla(['Componente', 'Puerto de la WuKong'], [['Motor 1', 'M1'], ['Motor 2', 'M2']]),
    ['Monta la moto siguiendo las instrucciones del wiki de ELECFREAKS.', 'Añade la extensión <b>wukong</b>.',
     'Con A, los dos motores avanzan; con B, retroceden; con A+B, se paran.', 'Muestra una flecha con el sentido de la marcha.'],
    mc='''input.onButtonPressed(Button.A, function () {
    wuKong.setAllMotor(60, 60)
    basic.showArrow(ArrowNames.North)
})
input.onButtonPressed(Button.B, function () {
    wuKong.setAllMotor(-60, -60)
    basic.showArrow(ArrowNames.South)
})
input.onButtonPressed(Button.AB, function () {
    wuKong.stopAllMotor()
    basic.showIcon(IconNames.No)
})''', pkgs=('wukong',),
    extra=box('idea', 'Más modelos', P('La guía del kit tiene decenas de modelos (coche seguidor de línea, brazo robot, puertas automáticas, noria…). '
        'Para el coche que esquiva obstáculos, añade también la extensión <code>https://github.com/elecfreaks/pxt-sonarbit</code> y lee la distancia con %s.' % kbd('Ultrasonic distance in unit cm at pin P1'))),
    ampliar=['Si los motores giran en sentidos opuestos, cambia el signo de la velocidad de uno de ellos.', 'Controla la moto inclinando otra micro:bit por radio.'],
    docente=P('Basado en el caso 1 del wiki de ELECFREAKS y en las funciones de la extensión oficial <code>pxt-wukong</code> (velocidad de −100 a 100).'),
    icono='engranaje', tiempo='2 sesiones', etapa='P2')

proyecto(S, 'taller-smart-agriculture', 'Smart Agriculture Kit: riego automático', G2,
    'El Smart Agriculture Kit de ELECFREAKS incluye la placa de expansión IoT:bit y sensores para proyectos de agricultura. Montamos un riego automático: si la tierra está seca, un servo abre la válvula; el nivel del depósito se muestra en la pantalla.',
    ['Smart Agriculture Kit (IoT:bit, sensor de humedad del suelo, sensor de nivel de agua, servo 180°)', 'micro:bit', 'Maceta y un depósito de agua'],
    kits.smart_agri() + tabla(['Componente', 'Puerto de la IoT:bit'], [['Sensor de humedad del suelo', 'P1'], ['Sensor de nivel de agua', 'P2'], ['Servo', 'P9']]),
    ['Conecta los sensores y el servo como en la tabla (igual que el caso 1 de la guía del kit).', 'Añade la extensión <b>iot-environment-kit</b>.',
     'Muestra el nivel del depósito con un gráfico de barras.', 'Si la humedad del suelo baja de 50, gira el servo para regar; si no, ciérralo.'],
    mc='''basic.forever(function () {
    led.plotBarGraph(Environment.ReadWaterLevel(AnalogPin.P2), 100)
    if (Environment.ReadSoilHumidity(AnalogPin.P1) < 50) {
        pins.servoWritePin(AnalogPin.P9, 90)
    } else {
        pins.servoWritePin(AnalogPin.P9, 0)
    }
    basic.pause(1000)
})''', pkgs=('environment',),
    extra=box('idea', 'Más casos del kit', P('La guía del kit propone 13 casos: control de temperatura y humedad del invernadero (DHT11 y pantalla OLED), luz artificial con LED de colores, '
        'protección de cultivos con sensor PIR, temperatura del agua (DS18B20), nivel de un estanque, comedero automático y una granja inteligente completa.')),
    ampliar=['Añade la pantalla OLED para mostrar los valores.', 'Programa un riego por horario además de por humedad.'],
    docente=P('Basado en el caso 1 del wiki de ELECFREAKS (humedad en P1, nivel en P2, servo en P9) y en las funciones de la extensión oficial <code>pxt-iot-environment-kit</code>, que dan valores de 0 a 100. '
              'El umbral de 50 es orientativo: calibradlo con vuestra tierra.'),
    icono='planta', tiempo='2 sesiones', etapa='ESO')
