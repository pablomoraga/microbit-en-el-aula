# -*- coding: utf-8 -*-
"""Comenzamos: prácticas 31-34, que cubren huecos de los bloques (operadores lógicos, fuerza del movimiento,
tempo musical y temporizador con bucle mientras)."""
from common import practica, kbd
from c_comenzamos import S, B2, B3, B4, B5

practica(S, '31', 'metronomo', 'Metrónomo', 2, 'P2', '20 min', ['variables', 'tiempo', 'sonido'],
    'Construir el metrónomo de la clase de música: marca el pulso con un clic y una luz, y con A y B se cambia la velocidad.',
    ['Crea la variable <i>pulsos</i> (pulsos por minuto) y [[fijar]] a 60.',
     'En [[boton]] (A), si <i>pulsos</i> es [[mayor]] que 40, réstale 10 y [[mostrar_numero]]. En B, si es [[menor]] que 200, súmale 10.',
     'En [[para_siempre]]: [[graficar]] el LED central, un [[tono]] corto de 1000 Hz, apágalo y haz una [[pausa]] de 60000 [[dividir]] entre <i>pulsos</i> (menos lo que dura el clic).',
     'Comprueba con un metrónomo de verdad o con un cronómetro: a 60 pulsos debe sonar uno por segundo.'],
    ['Un minuto son 60000 ms. Si hay 60 pulsos por minuto, entre pulso y pulso pasan 60000 ÷ 60 = 1000 ms.',
     'Al tiempo de espera hay que restarle los 50 ms que dura el clic.'],
    '''let pulsos = 60
input.onButtonPressed(Button.A, function () {
    if (pulsos > 40) {
        pulsos += -10
    }
    basic.showNumber(pulsos)
})
input.onButtonPressed(Button.B, function () {
    if (pulsos < 200) {
        pulsos += 10
    }
    basic.showNumber(pulsos)
})
basic.forever(function () {
    led.plot(2, 2)
    music.play(music.tonePlayable(1000, 50), music.PlaybackMode.UntilDone)
    led.unplot(2, 2)
    basic.pause(60000 / pulsos - 50)
})''',
    "whenStarted\npulsos = 60\nforever {\n  '[display:mbPlot]' 3 3\n  'play frequency' 1000 50\n  '[display:mbUnplot]' 3 3\n  waitMillis ((60000 / pulsos) - 50)\n}\n---\nwhenButtonPressed 'A'\nif (pulsos > 40) {\n  pulsos += -10\n}\nscroll_text pulsos\n---\nwhenButtonPressed 'B'\nif (pulsos < 200) {\n  pulsos += 10\n}\nscroll_text pulsos",
    '''from microbit import *
import music

pulsos = 60
while True:
    if button_a.was_pressed() and pulsos > 40:
        pulsos -= 10
        display.scroll(pulsos)
    if button_b.was_pressed() and pulsos < 200:
        pulsos += 10
        display.scroll(pulsos)
    display.set_pixel(2, 2, 9)
    music.pitch(1000, 50)
    display.set_pixel(2, 2, 0)
    sleep(60000 // pulsos - 50)''',
    ['Marca el primer pulso de cada compás (cada 4) con un sonido más agudo.', 'Busca en internet a cuántos pulsos va una canción que te guste y tócala con el metrónomo.'],
    group=B2, icono='musica')

practica(S, '32', 'alarma-de-mochila', 'Alarma de mochila', 2, 'P2', '20 min', ['acelerómetro', 'variables', 'condicionales'],
    'Proteger la mochila o el estuche: con A se activa la alarma y, si alguien lo mueve, suena hasta que se pulse B.',
    ['Crea dos variables: <i>armada</i> y <i>sonando</i>, las dos en falso.',
     'En [[boton]] (A), [[mostrar_icono]] ✔, haz una [[pausa]] de 1 segundo para dejar la placa quieta, [[borrar]] y pon <i>armada</i> a verdadero.',
     'En [[para_siempre]]: si <i>armada</i> [[y]] la fuerza de la [[aceleracion]] es [[mayor]] que el umbral, pon <i>sonando</i> a verdadero.',
     'Si <i>sonando</i> es verdadero, muestra ✘ y toca dos [[tono]] alternos.',
     'En [[boton]] (B), pon las dos variables a falso y [[borrar]].'],
    ['La <b>fuerza</b> de la aceleración suma los tres ejes. En reposo vale lo mismo que la gravedad: unos 1024 en MakeCode y unos 100 en MicroBlocks.',
     'El bloque %s solo es verdadero si se cumplen las dos condiciones a la vez.' % kbd('y'),
     'La pausa de 1 segundo al armarla evita que salte al pulsar el botón.'],
    '''let armada = false
let sonando = false
input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Yes)
    basic.pause(1000)
    basic.clearScreen()
    armada = true
})
input.onButtonPressed(Button.B, function () {
    armada = false
    sonando = false
    basic.clearScreen()
})
basic.forever(function () {
    if (armada && input.acceleration(Dimension.Strength) > 1500) {
        sonando = true
    }
    if (sonando) {
        basic.showIcon(IconNames.No)
        music.play(music.tonePlayable(880, 150), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(440, 150), music.PlaybackMode.UntilDone)
    }
})''',
    "whenStarted\narmada = (booleanConstant false)\nsonando = (booleanConstant false)\nforever {\n  if (and armada (('[sensors:acceleration]') > 150)) {\n    sonando = (booleanConstant true)\n  }\n  if sonando {\n    led_displayImage 'no'\n    'play frequency' 880 150\n    'play frequency' 440 150\n  }\n}\n---\nwhenButtonPressed 'A'\nled_displayImage 'yes'\nwaitMillis 1000\n'[display:mbDisplayOff]'\narmada = (booleanConstant true)\n---\nwhenButtonPressed 'B'\narmada = (booleanConstant false)\nsonando = (booleanConstant false)\n'[display:mbDisplayOff]'",
    '''from microbit import *
import music
import math

armada = False
sonando = False
while True:
    if button_a.was_pressed():
        display.show(Image.YES)
        sleep(1000)
        display.clear()
        armada = True
    if button_b.was_pressed():
        armada = False
        sonando = False
        display.clear()
    x, y, z = accelerometer.get_values()
    if armada and math.sqrt(x * x + y * y + z * z) > 1500:
        sonando = True
    if sonando:
        display.show(Image.NO)
        music.pitch(880, 150)
        music.pitch(440, 150)''',
    ['Cambia el umbral: ¿cuál detecta que se abre la cremallera sin saltar por un portazo?', 'Haz que la alarma solo se pueda apagar con un código (práctica 33).'],
    group=B3, icono='aviso')

practica(S, '33', 'caja-fuerte', 'Caja fuerte', 2, 'P2', '20 min', ['variables', 'operadores lógicos', 'condicionales'],
    'Programar la cerradura de una caja fuerte: la combinación secreta es pulsar A tres veces y B dos veces; el logotipo comprueba si es correcta.',
    ['Crea las variables <i>a</i> y <i>b</i> y [[fijar]] las dos a 0.',
     'En [[boton]] (A), [[cambiar]] <i>a</i> por 1. En [[boton]] (B), [[cambiar]] <i>b</i> por 1.',
     'En [[logo]]: si <i>a</i> [[igual]] 3 [[y]] <i>b</i> [[igual]] 2, [[mostrar_icono]] ✔ y suena un [[tono]]; si no, ✘.',
     'Después de comprobar, vuelve a poner <i>a</i> y <i>b</i> a 0.',
     'Inventa tu propia combinación y reta a un compañero a descubrirla.'],
    ['Con %s las dos condiciones tienen que cumplirse; con %s basta con una.' % (kbd('y'), kbd('o')),
     '¿Cuántas combinaciones distintas hay si cada botón se puede pulsar de 0 a 5 veces? (6 × 6 = 36).'],
    '''let a = 0
let b = 0
input.onButtonPressed(Button.A, function () {
    a += 1
})
input.onButtonPressed(Button.B, function () {
    b += 1
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    if (a == 3 && b == 2) {
        basic.showIcon(IconNames.Yes)
        music.play(music.tonePlayable(988, 500), music.PlaybackMode.UntilDone)
    } else {
        basic.showIcon(IconNames.No)
    }
    a = 0
    b = 0
})''',
    "whenStarted\na = 0\nb = 0\n---\nwhenButtonPressed 'A'\na += 1\n---\nwhenButtonPressed 'B'\nb += 1\n---\nwhenCondition (touchPin_logoTouched)\nif (and (a == 3) (b == 2)) {\n  led_displayImage 'yes'\n  'play frequency' 988 500\n} else {\n  led_displayImage 'no'\n}\na = 0\nb = 0\nwaitMillis 500",
    '''from microbit import *
import music

a = 0
b = 0
while True:
    if button_a.was_pressed():
        a += 1
    if button_b.was_pressed():
        b += 1
    if pin_logo.is_touched():
        if a == 3 and b == 2:
            display.show(Image.YES)
            music.pitch(988, 500)
        else:
            display.show(Image.NO)
        a = 0
        b = 0
        sleep(500)''',
    ['Bloquea la caja tres minutos si se falla tres veces.', 'Envía un aviso por radio a otra placa cuando alguien falle (bloque 6).'],
    group=B4, icono='pulsador')

practica(S, '34', 'temporizador', 'Temporizador de tareas', 2, 'P2', '20 min', ['bucle mientras', 'variables', 'tiempo'],
    'Un temporizador para el trabajo en clase: A añade minutos, B empieza la cuenta atrás y al final suena una melodía.',
    ['Crea la variable <i>minutos</i>. En [[boton]] (A), [[cambiar]] por 1 y [[mostrar_numero]].',
     'En [[boton]] (B), usa [[mientras]] <i>minutos</i> [[mayor]] que 0: muestra los minutos, haz una [[pausa]] de 60000 ms y réstale 1.',
     'Al salir del bucle, [[mostrar_icono]] ✔ y toca una [[melodia]].',
     'Para probarlo sin esperar, cambia 60000 por 1000 (segundos en vez de minutos).'],
    ['El bucle %s repite mientras la condición sea verdadera: no sabemos de antemano cuántas vueltas dará.' % kbd('mientras'),
     'En MicroBlocks se usa %s, que repite <b>hasta que</b> la condición se cumpla: la condición va al revés.' % kbd('repite hasta que')],
    '''let minutos = 0
input.onButtonPressed(Button.A, function () {
    minutos += 1
    basic.showNumber(minutos)
})
input.onButtonPressed(Button.B, function () {
    while (minutos > 0) {
        basic.showNumber(minutos)
        basic.pause(60000)
        minutos += -1
    }
    basic.showIcon(IconNames.Yes)
    music.startMelody(music.builtInMelody(Melodies.PowerUp), MelodyOptions.Once)
})''',
    "whenStarted\nminutos = 0\n---\nwhenButtonPressed 'A'\nminutos += 1\nscroll_text minutos\n---\nwhenButtonPressed 'B'\nrepeatUntil (minutos == 0) {\n  scroll_text minutos\n  waitMillis 60000\n  minutos += -1\n}\nled_displayImage 'yes'\n'play tone' 'nt;c' 1 200\n'play tone' 'nt;e' 1 200\n'play tone' 'nt;g' 1 400",
    '''from microbit import *
import music

minutos = 0
while True:
    if button_a.was_pressed():
        minutos += 1
        display.scroll(minutos)
    if button_b.was_pressed():
        while minutos > 0:
            display.scroll(minutos)
            sleep(60000)
            minutos -= 1
        display.show(Image.YES)
        music.play(music.POWER_UP)''',
    ['Avisa con un pitido cuando quede 1 minuto.', 'Úsalo para las rotaciones de un trabajo por estaciones.'],
    group=B5, icono='reloj')
