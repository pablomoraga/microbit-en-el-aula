# -*- coding: utf-8 -*-
"""Modo experto: un juego con física sencilla (rebotes), un instrumento con sensor y un mando por radio que sirve de base para los robots."""
from common import practica, kbd
from c_comenzamos import bm
from c_experto import S, J, R

ARR = {'N': ('00100', '01110', '10101', '00100', '00100'), 'S': ('00100', '00100', '10101', '01110', '00100'),
       'O': ('00100', '01000', '11111', '01000', '00100'), 'E': ('00100', '00010', '11111', '00010', '00100')}

practica(S, 'J5', 'pong', 'Pong para uno', 3, 'P2', '45 min', ['juego', 'coordenadas', 'velocidad'],
    'Una versión del clásico Pong: la pelota rebota en las paredes y hay que devolverla con la pala (dos LED abajo) usando A y B. Cada rebote suma un punto y la pelota va cada vez más rápido.',
    ['Variables: <i>pala</i> (columna izquierda de la pala), <i>x</i> e <i>y</i> (posición de la pelota), <i>dx</i> y <i>dy</i> (hacia dónde se mueve, +1 o −1), <i>puntos</i> y <i>jugando</i>.',
     'Con A y B mueve la pala sin que se salga (ocupa dos columnas).',
     'En [[para_siempre]]: [[borrar]], dibuja la pala y la pelota y haz una [[pausa]] que se acorta con los puntos.',
     'Rebotes: si la pelota se saldría por un lado, cambia el signo de <i>dx</i>; si llega arriba, <i>dy</i> pasa a 1.',
     'Si va a llegar a la fila de abajo: si la pala está debajo, <i>dy</i> pasa a −1 y suma un punto; si no, se acaba la partida.'],
    ['La velocidad es «cuánto cambia la posición en cada paso»: por eso sumamos <i>dx</i> a <i>x</i> y <i>dy</i> a <i>y</i>.',
     'Rebotar es cambiar el signo de la velocidad: <i>dx</i> = 0 − <i>dx</i>.',
     'En MicroBlocks las coordenadas van de 1 a 5, así que los límites cambian.',
     'Con %s evitas que la pausa baje de 100 ms y el juego sea imposible.' % kbd('máximo')],
    '''let pala = 2
let x = 2
let y = 0
let dx = 1
let dy = 1
let puntos = 0
let jugando = true
input.onButtonPressed(Button.A, function () {
    if (pala > 0) {
        pala += -1
    }
})
input.onButtonPressed(Button.B, function () {
    if (pala < 3) {
        pala += 1
    }
})
basic.forever(function () {
    if (jugando) {
        basic.clearScreen()
        led.plot(pala, 4)
        led.plot(pala + 1, 4)
        led.plot(x, y)
        basic.pause(Math.max(100, 400 - puntos * 20))
        if (x + dx < 0 || x + dx > 4) {
            dx = 0 - dx
        }
        if (y + dy < 0) {
            dy = 1
        }
        if (y + dy == 4) {
            if (x + dx == pala || x + dx == pala + 1) {
                dy = -1
                puntos += 1
            } else {
                jugando = false
            }
        }
        x += dx
        y += dy
    } else {
        basic.showString("Puntos")
        basic.showNumber(puntos)
    }
})''',
    "whenStarted\npala = 3\nx = 3\ny = 1\ndx = 1\ndy = 1\npuntos = 0\njugando = (booleanConstant true)\nforever {\n  if jugando {\n    '[display:mbDisplayOff]'\n    '[display:mbPlot]' pala 5\n    '[display:mbPlot]' (pala + 1) 5\n    '[display:mbPlot]' x y\n    waitMillis (maximum 100 (400 - (puntos * 20)))\n    if (or ((x + dx) < 1) ((x + dx) > 5)) {\n      dx = (0 - dx)\n    }\n    if ((y + dy) < 1) {\n      dy = 1\n    }\n    if ((y + dy) == 5) {\n      if (or ((x + dx) == pala) ((x + dx) == (pala + 1))) {\n        dy = -1\n        puntos += 1\n      } else {\n        jugando = (booleanConstant false)\n      }\n    }\n    x += dx\n    y += dy\n  } else {\n    scroll_text ('[data:join]' 'Puntos ' puntos)\n  }\n}\n---\nwhenButtonPressed 'A'\nif (pala > 1) {\n  pala += -1\n}\n---\nwhenButtonPressed 'B'\nif (pala < 4) {\n  pala += 1\n}",
    '''from microbit import *

pala, x, y, dx, dy, puntos = 2, 2, 0, 1, 1, 0
while True:
    if button_a.was_pressed() and pala > 0:
        pala -= 1
    if button_b.was_pressed() and pala < 3:
        pala += 1
    display.clear()
    display.set_pixel(pala, 4, 9)
    display.set_pixel(pala + 1, 4, 9)
    display.set_pixel(x, y, 9)
    sleep(max(100, 400 - puntos * 20))
    if x + dx < 0 or x + dx > 4:
        dx = -dx
    if y + dy < 0:
        dy = 1
    if y + dy == 4:
        if x + dx == pala or x + dx == pala + 1:
            dy = -1
            puntos += 1
        else:
            break
    x += dx
    y += dy
display.scroll("Puntos " + str(puntos))''',
    ['Haz la pala de un solo LED para el modo difícil.', 'Versión para dos jugadores por radio: cada placa es un campo y la pelota pasa de una a otra.'],
    group=J, icono='diana')

practica(S, 'R5', 'theremin-de-luz', 'Theremin de luz', 2, 'P2', '30 min', ['sensor de luz', 'sonido', 'escalar valores'],
    'El theremin es un instrumento que se toca sin tocarlo. El nuestro convierte la luz en sonido: acerca y aleja la mano de la pantalla para cambiar la nota.',
    ['En [[para_siempre]], guarda la [[luz]] en la variable <i>luz</i>.',
     'Si la luz es [[mayor]] que un mínimo, toca un [[tono]] corto cuya frecuencia sea 200 + <i>luz</i> × 4 (en MicroBlocks, 200 + <i>luz</i>).',
     'Si hay muy poca luz, no suena: así puedes «callarlo» tapando la placa.',
     'Ilumina la placa con una linterna y toca una melodía sencilla.'],
    ['La pantalla de la micro:bit también mide la luz: de 0 a 255 en MakeCode y Python, y hasta unos 1000 en MicroBlocks. Por eso la fórmula cambia.',
     'Convertir un rango de valores en otro se llama <b>escalar</b>: es la misma idea que en el taller del potenciómetro.'],
    '''let luz = 0
basic.forever(function () {
    luz = input.lightLevel()
    if (luz > 10) {
        music.play(music.tonePlayable(200 + luz * 4, 100), music.PlaybackMode.UntilDone)
    } else {
        basic.pause(100)
    }
})''',
    "whenStarted\nforever {\n  luz = ('[display:lightLevel]')\n  if (luz > 40) {\n    'play frequency' (200 + luz) 100\n  } else {\n    waitMillis 100\n  }\n}",
    '''from microbit import *
import music

while True:
    luz = display.read_light_level()
    if luz > 10:
        music.pitch(200 + luz * 4, 100)
    else:
        sleep(100)''',
    ['Haz que solo suenen las notas de una escala (do, re, mi…) según la luz.', 'Investiga quién inventó el theremin y cómo funciona el de verdad.'],
    group=R, icono='musica')

practica(S, 'R6', 'mando-por-inclinacion', 'Mando por inclinación', 3, 'P2', '40 min', ['radio', 'acelerómetro', 'códigos'],
    'Un mando a distancia: al inclinar una placa, la otra muestra una flecha hacia ese lado. Es la base para conducir por radio los robots del apartado Talleres.',
    ['En [[al_iniciar]], [[radio_grupo]] con el mismo número en las dos placas.',
     'En [[para_siempre]], según la [[inclinacion]], envía un código con [[radio_enviar_numero]]: 1 delante, 2 detrás, 3 izquierda, 4 derecha y 0 si está plana. Espera 200 ms.',
     'Con [[radio_recibir_numero]], muestra la [[flecha]] de cada código o [[borrar]] si llega un 0.',
     'Carga el mismo programa en las dos placas y comprueba qué flecha sale al inclinar hacia cada lado; si alguna va al revés, intercambia sus códigos.'],
    ['El mismo programa sirve de mando y de receptor: cada placa envía su inclinación y muestra la de la otra.',
     'Para conducir un robot, el receptor no muestra flechas: mueve los motores según el código. Lo tienes hecho en el taller <a href="../talleres/cutebot-teledirigido.html">Cutebot: teledirigido por radio</a>.',
     'En MicroBlocks la inclinación va de −100 a 100; en MakeCode y Python, de −1024 a 1024.'],
    '''radio.setGroup(7)
basic.forever(function () {
    if (input.acceleration(Dimension.Y) < -300) {
        radio.sendNumber(1)
    } else if (input.acceleration(Dimension.Y) > 300) {
        radio.sendNumber(2)
    } else if (input.acceleration(Dimension.X) < -300) {
        radio.sendNumber(3)
    } else if (input.acceleration(Dimension.X) > 300) {
        radio.sendNumber(4)
    } else {
        radio.sendNumber(0)
    }
    basic.pause(200)
})
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        basic.showArrow(ArrowNames.North)
    } else if (receivedNumber == 2) {
        basic.showArrow(ArrowNames.South)
    } else if (receivedNumber == 3) {
        basic.showArrow(ArrowNames.West)
    } else if (receivedNumber == 4) {
        basic.showArrow(ArrowNames.East)
    } else {
        basic.clearScreen()
    }
})''',
    ("whenStarted\n'[radio:setGroup]' 7\nforever {\n  if (('[sensors:tiltY]') < -30) {\n    '[radio:sendInteger]' 1\n  } (('[sensors:tiltY]') > 30) {\n    '[radio:sendInteger]' 2\n  } (('[sensors:tiltX]') < -30) {\n    '[radio:sendInteger]' 3\n  } (('[sensors:tiltX]') > 30) {\n    '[radio:sendInteger]' 4\n  } else {\n    '[radio:sendInteger]' 0\n  }\n  waitMillis 200\n}\n---\n"
     "whenCondition ('[radio:messageReceived]')\ncodigo = ('[radio:receivedInteger]')\nif (codigo == 1) {\n  '[display:mbDisplay]' %d\n} (codigo == 2) {\n  '[display:mbDisplay]' %d\n} (codigo == 3) {\n  '[display:mbDisplay]' %d\n} (codigo == 4) {\n  '[display:mbDisplay]' %d\n} else {\n  '[display:mbDisplayOff]'\n}") % (
        bm(*ARR['N']), bm(*ARR['S']), bm(*ARR['O']), bm(*ARR['E'])),
    '''from microbit import *
import radio

radio.on()
radio.config(group=7)
flechas = {"1": Image.ARROW_N, "2": Image.ARROW_S, "3": Image.ARROW_W, "4": Image.ARROW_E}
while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    if y < -300:
        radio.send("1")
    elif y > 300:
        radio.send("2")
    elif x < -300:
        radio.send("3")
    elif x > 300:
        radio.send("4")
    else:
        radio.send("0")
    codigo = radio.receive()
    if codigo in flechas:
        display.show(flechas[codigo])
    elif codigo == "0":
        display.clear()
    sleep(200)''',
    ['Convierte la placa receptora en un robot: sustituye las flechas por órdenes a los motores de tu kit.', 'Añade un código 5 para tocar el claxon con el botón A.'],
    group=R, icono='mando', materiales=['Dos micro:bits con su cable o portapilas'])
