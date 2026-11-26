# -*- coding: utf-8 -*-
"""Modo experto: juegos, retos, cables de cocodrilo y sensores."""
from common import practica, P, ul, box, kbd, tabla
from c_comenzamos import bm, pyimg, mcleds
import conexiones

S = 'experto'
J, R, C, SE = 'Juegos', 'Retos', 'Cables de cocodrilo', 'Sensores externos'
COCO = 'Cables de cocodrilo (mejor de colores distintos)'
GRUPOS = {
    J: P('Juegos completos para jugar solo, en pareja o en grupo. Combinan todo lo aprendido: variables, azar, tiempo y condiciones.'),
    R: P('Retos más abiertos: el paso a paso es más corto y se espera que pruebes y busques tu propia solución antes de mirar la nuestra.'),
    C: P('Con <b>cables de cocodrilo</b> conectamos la micro:bit a objetos y componentes sin soldar. Recuerda: todo circuito tiene que volver a <b>GND</b>.') +
       box('ojo', 'Seguridad', ul(['Nunca unas 3V y GND directamente.', 'Pon una resistencia de 220 Ω en serie con cada LED externo.',
                                   'Revisa las conexiones con la placa desconectada.'])),
    SE: P('Sensores sencillos y baratos que se conectan a los anillos P0, P1 y P2. Leemos valores <b>analógicos</b> (de 0 a 1023) y los convertimos en decisiones.'),
}

# =================================================================== Juegos
practica(S, 'J1', 'atrapa-la-estrella', 'Atrapa la estrella', 3, 'P2', '45 min', ['juego', 'coordenadas', 'variables'],
    'Mover una cesta (el LED de abajo) con A y B para atrapar la estrella que cae. Cada estrella atrapada suma un punto; si se escapa tres veces, fin del juego.',
    ['Variables: <i>cesta</i> (columna de la cesta), <i>x</i> e <i>y</i> (posición de la estrella), <i>puntos</i> y <i>vidas</i>.',
     'En [[boton]] A, la cesta va a la izquierda y en B a la derecha; con [[si]] evita que se salga.',
     'En [[para_siempre]]: [[borrar]], [[graficar]] la cesta y la estrella, [[pausa]] y [[cambiar]] y por 1.',
     'Cuando la estrella llega abajo: si está en la columna de la cesta, suma un punto; si no, resta una vida. Después vuelve arriba en una columna al azar.',
     'Cuando las vidas lleguen a 0, muestra los puntos.'],
    ['Las coordenadas van de 0 a 4 (en MicroBlocks, de 1 a 5). La cesta siempre está en la última fila.',
     'Para que el juego sea más difícil, reduce la espera a medida que suben los puntos.',
     'Prueba primero solo la cesta; cuando funcione, añade la estrella.'],
    '''let cesta = 2
let x = randint(0, 4)
let y = 0
let puntos = 0
let vidas = 3
input.onButtonPressed(Button.A, function () {
    if (cesta > 0) {
        cesta += -1
    }
})
input.onButtonPressed(Button.B, function () {
    if (cesta < 4) {
        cesta += 1
    }
})
basic.forever(function () {
    if (vidas > 0) {
        basic.clearScreen()
        led.plot(cesta, 4)
        led.plot(x, y)
        basic.pause(400)
        y += 1
        if (y == 4) {
            if (x == cesta) {
                puntos += 1
            } else {
                vidas += -1
            }
            y = 0
            x = randint(0, 4)
        }
    } else {
        basic.showString("Puntos")
        basic.showNumber(puntos)
    }
})''',
    "whenStarted\ncesta = 3\nx = (random 1 5)\ny = 1\npuntos = 0\nvidas = 3\nforever {\n  if (vidas > 0) {\n    '[display:mbDisplayOff]'\n    '[display:mbPlot]' cesta 5\n    '[display:mbPlot]' x y\n    waitMillis 400\n    y += 1\n    if (y == 5) {\n      if (x == cesta) {\n        puntos += 1\n      } else {\n        vidas += -1\n      }\n      y = 1\n      x = (random 1 5)\n    }\n  } else {\n    scroll_text ('[data:join]' 'Puntos ' puntos)\n  }\n}\n---\nwhenButtonPressed 'A'\nif (cesta > 1) {\n  cesta += -1\n}\n---\nwhenButtonPressed 'B'\nif (cesta < 5) {\n  cesta += 1\n}",
    '''from microbit import *
import random

cesta, x, y = 2, random.randint(0, 4), 0
puntos, vidas = 0, 3
while vidas > 0:
    if button_a.was_pressed() and cesta > 0:
        cesta -= 1
    if button_b.was_pressed() and cesta < 4:
        cesta += 1
    display.clear()
    display.set_pixel(cesta, 4, 9)
    display.set_pixel(x, y, 5)
    sleep(400)
    y += 1
    if y == 4:
        if x == cesta:
            puntos += 1
        else:
            vidas -= 1
        y, x = 0, random.randint(0, 4)
display.scroll("Puntos " + str(puntos))''',
    ['Aumenta la velocidad cada 5 puntos.', 'Añade una estrella «mala» que quita vidas si la atrapas.', 'En MakeCode, rehazlo con los bloques de <b>Juego</b> (sprites).'],
    group=J, icono='estrella',
    explica='En Python el botón solo se comprueba una vez por vuelta del bucle (cada 400 ms). Si notas que se pierden pulsaciones, prueba a acortar la espera.')

practica(S, 'J2', 'patata-caliente', 'Patata caliente', 2, 'P1', '25 min', ['juego', 'azar', 'tiempo'],
    'La placa es una patata caliente que pasa de mano en mano: suena un tic-tac y, tras un tiempo al azar, «explota». Quien la tenga en ese momento, pierde.',
    ['En [[boton]] (A), guarda un tiempo límite con [[azar]] entre 5000 y 15 000 ms.',
     'Con [[mientras]] no se acabe el tiempo ([[tiempo]]), muestra la patata y un [[tono]] corto cada medio segundo.',
     'Cuando se acabe, muestra una calavera y toca un sonido largo.',
     'Sentaos en corro y pasad la placa a quien tengáis al lado en cada tic.'],
    ['Usa el cronómetro (MicroBlocks) o el tiempo de ejecución (MakeCode y Python) para saber cuánto ha pasado.',
     'Un bucle «mientras» repite el tic-tac hasta que se acaba el tiempo.'],
    '''input.onButtonPressed(Button.A, function () {
    let limite = input.runningTime() + randint(5000, 15000)
    while (input.runningTime() < limite) {
        basic.showIcon(IconNames.Ghost)
        music.play(music.tonePlayable(523, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.UntilDone)
        basic.pause(400)
    }
    basic.showIcon(IconNames.Skull)
    music.play(music.tonePlayable(131, music.beat(BeatFraction.Breve)), music.PlaybackMode.UntilDone)
})''',
    "whenButtonPressed 'A'\nresetTimer\nlimite = (random 5000 15000)\nrepeatUntil ((timer) > limite) {\n  led_displayImage 'ghost'\n  'play frequency' 523 60\n  waitMillis 400\n}\nled_displayImage 'skull'\n'play frequency' 131 1200",
    '''from microbit import *
import random
import music

while True:
    if button_a.was_pressed():
        limite = running_time() + random.randint(5000, 15000)
        while running_time() < limite:
            display.show(Image.GHOST)
            music.pitch(523, 60)
            sleep(400)
        display.show(Image.SKULL)
        music.pitch(131, 1200)''',
    ['Haz que el tic-tac vaya más rápido a medida que se acerca la explosión.', 'Lleva la cuenta de los perdedores con B.'],
    group=J, icono='rayo')

practica(S, 'J3', 'duelo-de-reflejos', 'Duelo de reflejos', 2, 'P2', '30 min', ['juego', 'condicionales', 'azar'],
    'Dos jugadores, una placa: cada uno pone el dedo cerca de su botón. Cuando aparece el corazón, gana quien pulse primero. Si alguien pulsa antes de tiempo, pierde.',
    ['En [[logo]], haz una cuenta atrás y una [[pausa]] de [[azar]] entre 1000 y 5000 ms.',
     'Durante la espera, si alguien pulsa, pierde por tramposo (lo resolvemos en el ¿Y si…?).',
     'Muestra el corazón y espera con [[esperar_hasta]] [[boton_pulsado]] [[o]] botón B.',
     'Muestra la letra del ganador y un sonido de victoria.'],
    ['En MakeCode, un %s espera mientras ninguno de los dos botones esté pulsado.' % kbd('mientras'),
     'En MicroBlocks: %s con una condición «botón A o botón B».' % kbd('espera hasta que')],
    '''input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showNumber(3)
    basic.showNumber(2)
    basic.showNumber(1)
    basic.clearScreen()
    basic.pause(randint(1000, 5000))
    basic.showIcon(IconNames.Heart)
    while (!(input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B))) {
        basic.pause(1)
    }
    if (input.buttonIsPressed(Button.A)) {
        basic.showString("A")
    } else {
        basic.showString("B")
    }
    music.play(music.builtInPlayableMelody(Melodies.PowerUp), music.PlaybackMode.UntilDone)
})''',
    "whenCondition (touchPin_logoTouched)\ndisplayCharacter '3'\nwaitMillis 700\ndisplayCharacter '2'\nwaitMillis 700\ndisplayCharacter '1'\nwaitMillis 700\n'[display:mbDisplayOff]'\nwaitMillis (random 1000 5000)\nled_displayImage 'heart'\nwaitUntil (or (buttonA) (buttonB))\nif (buttonA) {\n  displayCharacter 'A'\n} else {\n  displayCharacter 'B'\n}\n'play tone' 'nt;c' 1 150\n'play tone' 'nt;g' 1 300",
    '''from microbit import *
import random
import music

while True:
    if pin_logo.is_touched():
        for n in (3, 2, 1):
            display.show(n)
            sleep(700)
        display.clear()
        sleep(random.randint(1000, 5000))
        display.show(Image.HEART)
        while not (button_a.is_pressed() or button_b.is_pressed()):
            sleep(1)
        if button_a.is_pressed():
            display.show("A")
        else:
            display.show("B")
        music.play(music.POWER_UP)''',
    ['Detecta los saltos en falso: si alguien pulsa durante la espera, gana el otro.', 'Juega al mejor de cinco con marcador para cada jugador.'],
    group=J, icono='pulsador')

practica(S, 'J4', 'memoria-musical', 'Memoria musical', 3, 'ESO', '45 min', ['listas', 'bucles', 'juego'],
    'La placa toca una secuencia de notas graves (botón A) y agudas (botón B) que crece en cada ronda. El jugador debe repetirla con los botones sin equivocarse.',
    ['Crea una lista vacía <i>secuencia</i>.',
     'En cada ronda, añade al final un 1 o un 2 al azar y toca la secuencia completa (1 = grave con flecha izquierda, 2 = aguda con flecha derecha).',
     'Recorre la lista esperando la pulsación del jugador y compara cada respuesta con el elemento.',
     'Si falla, muestra la puntuación (rondas superadas) y termina. Si acierta toda la secuencia, nueva ronda.'],
    ['Necesitas dos bucles: uno para tocar la secuencia y otro para comprobar las respuestas.',
     'Para leer la respuesta: espera hasta que se pulse A o B, guarda cuál fue y espera a que se suelte.'],
    '''let secuencia: number[] = []
let ok = true
let respuesta = 0
basic.forever(function () {
    if (ok) {
        secuencia.push(randint(1, 2))
        for (let nota of secuencia) {
            if (nota == 1) {
                basic.showArrow(ArrowNames.West)
                music.play(music.tonePlayable(262, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            } else {
                basic.showArrow(ArrowNames.East)
                music.play(music.tonePlayable(523, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            }
            basic.clearScreen()
            basic.pause(200)
        }
        for (let nota2 of secuencia) {
            while (!(input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B))) {
                basic.pause(1)
            }
            if (input.buttonIsPressed(Button.A)) {
                respuesta = 1
            } else {
                respuesta = 2
            }
            while (input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B)) {
                basic.pause(1)
            }
            if (respuesta != nota2) {
                ok = false
            }
        }
        if (ok) {
            basic.showIcon(IconNames.Yes)
            basic.pause(500)
        } else {
            basic.showIcon(IconNames.No)
            basic.showNumber(secuencia.length - 1)
        }
    }
})''',
    "whenStarted\nsecuencia = ('[data:makeList]')\nok = (booleanConstant true)\nwaitMillis 1000\nrepeatUntil (not ok) {\n  '[data:addLast]' (random 1 2) secuencia\n  for nota secuencia {\n    if (nota == 1) {\n      '[display:mbDisplay]' %d\n      'play tone' 'nt;c' 0 400\n    } else {\n      '[display:mbDisplay]' %d\n      'play tone' 'nt;c' 1 400\n    }\n    '[display:mbDisplayOff]'\n    waitMillis 200\n  }\n  for nota secuencia {\n    waitUntil (or (buttonA) (buttonB))\n    if (buttonA) {\n      respuesta = 1\n    } else {\n      respuesta = 2\n    }\n    waitUntil (not (or (buttonA) (buttonB)))\n    if (respuesta != nota) {\n      ok = (booleanConstant false)\n    }\n  }\n  if ok {\n    led_displayImage 'yes'\n    waitMillis 500\n  }\n}\nled_displayImage 'no'\nscroll_text ((size secuencia) - 1)" % (
        bm('00100', '01000', '11111', '01000', '00100'), bm('00100', '00010', '11111', '00010', '00100')),
    '''from microbit import *
import random
import music

secuencia = []
ok = True
while ok:
    secuencia.append(random.randint(1, 2))
    for nota in secuencia:
        if nota == 1:
            display.show(Image.ARROW_W)
            music.pitch(262, 400)
        else:
            display.show(Image.ARROW_E)
            music.pitch(523, 400)
        display.clear()
        sleep(200)
    for nota in secuencia:
        while not (button_a.is_pressed() or button_b.is_pressed()):
            sleep(1)
        respuesta = 1 if button_a.is_pressed() else 2
        while button_a.is_pressed() or button_b.is_pressed():
            sleep(1)
        if respuesta != nota:
            ok = False
            break
    if ok:
        display.show(Image.YES)
        sleep(500)
display.show(Image.NO)
sleep(1000)
display.scroll(len(secuencia) - 1)''',
    ['Añade una tercera nota con el logotipo.', 'Guarda el récord de la sesión y muéstralo al empezar.'],
    group=J, icono='musica')

# =================================================================== Retos
practica(S, 'R1', 'reloj-de-arena', 'Reloj de arena', 2, 'P2', '25 min', ['bucles', 'tiempo'],
    'Hacer un reloj de arena de 25 segundos: cada segundo se enciende un LED nuevo. Al llenarse la pantalla, suena una alarma. Agitando la placa se reinicia.',
    ['Piensa cómo recorrer los 25 LED en orden (pista: práctica 21).',
     'Usa dos [[para_indice]] con [[graficar]] y una [[pausa]] de 1000 ms.',
     'Al terminar, toca la alarma.',
     'Mete todo en [[agitar]] para volver a empezar.'],
    ['¿Cuántos segundos tiene que esperar cada LED si quieres un reloj de 1 minuto? 60 / 25 = 2,4 s.'],
    '''input.onGesture(Gesture.Shake, function () {
    basic.clearScreen()
    for (let y = 0; y <= 4; y++) {
        for (let x = 0; x <= 4; x++) {
            led.plot(x, y)
            basic.pause(1000)
        }
    }
    music.play(music.builtInPlayableMelody(Melodies.Entertainer), music.PlaybackMode.UntilDone)
})''',
    "whenCondition (('[sensors:acceleration]') > 200)\n'[display:mbDisplayOff]'\nfor y 5 {\n  for x 5 {\n    '[display:mbPlot]' x y\n    waitMillis 1000\n  }\n}\nrepeat 3 {\n  'play tone' 'nt;a' 1 200\n  waitMillis 100\n}",
    '''from microbit import *
import music

while True:
    if accelerometer.was_gesture("shake"):
        display.clear()
        for y in range(5):
            for x in range(5):
                display.set_pixel(x, y, 9)
                sleep(1000)
        music.play(music.ENTERTAINER)''',
    ['Haz que A elija la duración: 1, 2 o 5 minutos.', 'Que la «arena» caiga desde arriba como en un reloj de verdad.'],
    group=R, icono='reloj')

practica(S, 'R2', 'termometro-maximo-minimo', 'Termómetro de máximas y mínimas', 3, 'ESO', '30 min', ['variables', 'sensores', 'comparar'],
    'Registrar la temperatura más alta y la más baja de un día: A muestra la máxima, B la mínima y A+B reinicia los registros.',
    ['Al iniciar, guarda la temperatura actual en <i>maxima</i> y en <i>minima</i>.',
     'En [[para_siempre]], compara [[temperatura]]: con [[si]] es [[mayor]] que la máxima, [[fijar]] la máxima; si es [[menor]] que la mínima, la mínima.',
     'Programa los botones para consultar y reiniciar.',
     'Deja la placa junto a una ventana durante la jornada.'],
    ['Este es el algoritmo clásico para encontrar el mayor y el menor de una serie de datos.'],
    '''let maxima = input.temperature()
let minima = input.temperature()
basic.forever(function () {
    if (input.temperature() > maxima) {
        maxima = input.temperature()
    }
    if (input.temperature() < minima) {
        minima = input.temperature()
    }
    basic.pause(1000)
})
input.onButtonPressed(Button.A, function () {
    basic.showNumber(maxima)
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(minima)
})
input.onButtonPressed(Button.AB, function () {
    maxima = input.temperature()
    minima = input.temperature()
    basic.showIcon(IconNames.Yes)
})''',
    "whenStarted\nmaxima = ('[sensors:temperature]')\nminima = ('[sensors:temperature]')\nforever {\n  t = ('[sensors:temperature]')\n  if (t > maxima) {\n    maxima = t\n  }\n  if (t < minima) {\n    minima = t\n  }\n  waitMillis 1000\n}\n---\nwhenButtonPressed 'A'\nscroll_text maxima\n---\nwhenButtonPressed 'B'\nscroll_text minima\n---\nwhenButtonPressed 'A+B'\nmaxima = ('[sensors:temperature]')\nminima = ('[sensors:temperature]')\nled_displayImage 'yes'",
    '''from microbit import *

maxima = minima = temperature()
ultimo = 0
while True:
    if running_time() - ultimo > 1000:
        t = temperature()
        maxima = max(maxima, t)
        minima = min(minima, t)
        ultimo = running_time()
    if button_a.is_pressed() and button_b.is_pressed():
        maxima = minima = temperature()
        display.show(Image.YES)
    elif button_a.was_pressed():
        display.scroll(maxima)
    elif button_b.was_pressed():
        display.scroll(minima)''',
    ['Haz lo mismo con el nivel de luz.', 'Calcula la temperatura media (necesitas sumar y contar).'],
    group=R, icono='termometro')

practica(S, 'R3', 'contador-de-palmadas', 'Contador de palmadas', 2, 'P2', '25 min', ['micrófono', 'variables'],
    'Contar palmadas con el micrófono de la V2 y mostrar el total. Con A se pone a cero.',
    ['Usa [[sonido_alto]] para detectar una palmada.',
     '[[cambiar]] palmadas por 1 y [[mostrar_numero]].',
     'Con A, vuelve a cero.',
     'Comprueba si cuenta bien 10 palmadas seguidas. ¿Y si alguien grita?'],
    ['En MakeCode: %s con la opción «alto». En MicroBlocks, la biblioteca Micrófono tiene %s.' % (kbd('al detectar el sonido alto'), kbd('recuento de palmadas')),
     'En Python: <code>microphone.was_event(SoundEvent.LOUD)</code>.'],
    '''let palmadas = 0
input.onSound(DetectedSound.Loud, function () {
    palmadas += 1
    basic.showNumber(palmadas)
})
input.onButtonPressed(Button.A, function () {
    palmadas = 0
    basic.showNumber(palmadas)
})''',
    "whenStarted\npalmadas = 0\nforever {\n  palmadas += (clapCount)\n  scroll_text palmadas\n}\n---\nwhenButtonPressed 'A'\npalmadas = 0\nscroll_text palmadas",
    '''from microbit import *

palmadas = 0
while True:
    if microphone.was_event(SoundEvent.LOUD):
        palmadas += 1
        display.scroll(palmadas)
    if button_a.was_pressed():
        palmadas = 0
        display.scroll(palmadas)''',
    ['Enciende la pantalla con dos palmadas y apágala con tres.', 'Mide el ritmo: palmadas por minuto.'],
    group=R, icono='microfono',
    explica='En MicroBlocks, «recuento de palmadas» espera a que termine una serie de palmadas y devuelve cuántas ha habido, así que la cuenta se actualiza al acabar cada serie.')

practica(S, 'R4', 'canica', 'La canica', 3, 'ESO', '35 min', ['acelerómetro', 'coordenadas', 'límites'],
    'Mover un LED por la pantalla inclinando la placa, como una canica sobre una mesa, sin que se salga de los bordes.',
    ['Guarda la posición de la canica en <i>x</i> e <i>y</i>, empezando en el centro.',
     'Con [[si_no]] y [[inclinacion]]: si se inclina a la derecha, [[cambiar]] x por 1; a la izquierda, por −1. Igual con y.',
     'Limita x e y para que no se salgan de la pantalla.',
     '[[borrar]] y [[graficar]] la canica en su nueva posición.'],
    ['Usa un umbral para que la canica no se mueva con temblores pequeños.',
     'Para limitar: «si x > 4, x = 4» y «si x < 0, x = 0». En Python: <code>min(4, max(0, x))</code>.'],
    '''let x = 2
let y = 2
basic.forever(function () {
    if (input.acceleration(Dimension.X) > 200 && x < 4) {
        x += 1
    } else if (input.acceleration(Dimension.X) < -200 && x > 0) {
        x += -1
    }
    if (input.acceleration(Dimension.Y) > 200 && y < 4) {
        y += 1
    } else if (input.acceleration(Dimension.Y) < -200 && y > 0) {
        y += -1
    }
    basic.clearScreen()
    led.plot(x, y)
    basic.pause(150)
})''',
    "whenStarted\nx = 3\ny = 3\nforever {\n  if (and (('[sensors:tiltX]') > 20) (x < 5)) {\n    x += 1\n  } (and (('[sensors:tiltX]') < -20) (x > 1)) {\n    x += -1\n  }\n  if (and (('[sensors:tiltY]') > 20) (y < 5)) {\n    y += 1\n  } (and (('[sensors:tiltY]') < -20) (y > 1)) {\n    y += -1\n  }\n  '[display:mbDisplayOff]'\n  '[display:mbPlot]' x y\n  waitMillis 150\n}",
    '''from microbit import *

x, y = 2, 2
while True:
    ax, ay = accelerometer.get_x(), accelerometer.get_y()
    if ax > 200:
        x += 1
    elif ax < -200:
        x -= 1
    if ay > 200:
        y += 1
    elif ay < -200:
        y -= 1
    x = min(4, max(0, x))
    y = min(4, max(0, y))
    display.clear()
    display.set_pixel(x, y, 9)
    sleep(150)''',
    ['Añade un «agujero» en una posición al azar: si la canica cae en él, suma un punto.', 'Haz que cuanto más inclines, más rápido vaya.'],
    group=R, icono='acelerometro')

# =================================================================== Cables de cocodrilo
practica(S, 'C1', 'piano-de-frutas', 'Piano de frutas', 2, 'P1', '40 min', ['pines táctiles', 'sonido'],
    'Convertir tres frutas (o plastilina, o papel de aluminio) en teclas de piano conectadas a P0, P1 y P2.',
    ['Conecta un cable de cocodrilo de P0 a una fruta, otro de P1 a otra y otro de P2 a la tercera.',
     'Conecta un cuarto cable a GND y sujeta su pinza con la mano (o pégala a tu muñeca).',
     'Usa [[pin_tocado]] para cada fruta, con [[mostrar_caracter]] y una [[nota]] distinta.',
     'Tocad una canción sencilla.'],
    ['Tu cuerpo cierra el circuito entre GND y el pin. Sin tocar GND, no funciona.',
     'En MakeCode: %s. En MicroBlocks: %s (biblioteca TouchPin).' % (kbd('al presionarse pin P0'), kbd('pin 0 touched'))],
    '''input.onPinPressed(TouchPin.P0, function () {
    basic.showString("C")
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
})
input.onPinPressed(TouchPin.P1, function () {
    basic.showString("E")
    music.play(music.tonePlayable(330, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
})
input.onPinPressed(TouchPin.P2, function () {
    basic.showString("G")
    music.play(music.tonePlayable(392, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
})''',
    "whenCondition (touchPin_pinTouched 0)\ndisplayCharacter 'C'\n'play tone' 'nt;c' 0 300\n---\nwhenCondition (touchPin_pinTouched 1)\ndisplayCharacter 'E'\n'play tone' 'nt;e' 0 300\n---\nwhenCondition (touchPin_pinTouched 2)\ndisplayCharacter 'G'\n'play tone' 'nt;g' 0 300",
    '''from microbit import *
import music

while True:
    if pin0.is_touched():
        display.show("C")
        music.pitch(262, 300)
    if pin1.is_touched():
        display.show("E")
        music.pitch(330, 300)
    if pin2.is_touched():
        display.show("G")
        music.pitch(392, 300)''',
    ['Prueba con otros materiales: ¿cuáles conducen y cuáles no?', 'Haced una orquesta: cada pareja con un instrumento distinto.'],
    conexion=conexiones.piano(), group=C, icono='cocodrilo', materiales=[COCO + ' (4)', 'Tres frutas, plastilina o trozos de papel de aluminio'])

practica(S, 'C2', 'semaforo-de-led', 'Semáforo de LED', 2, 'P2', '40 min', ['salidas digitales', 'secuencia'],
    'Montar un semáforo con tres LED (rojo, amarillo y verde) conectados a P0, P1 y P2, y programar su secuencia.',
    ['Cada LED tiene una pata larga (+) y una corta (−). Conecta la pata larga de cada LED a su pin a través de una resistencia de 220 Ω.',
     'Une todas las patas cortas a GND.',
     'En [[para_siempre]], programa la secuencia con [[pin_escribir]] y [[pausa]]: verde 4 s, amarillo 1 s, rojo 4 s.',
     'En cada fase enciende solo el LED que corresponde (1) y apaga los demás (0).'],
    ['En MakeCode: %s (Pines). En MicroBlocks: %s (Pines), con el interruptor verde para encender.' % (kbd('escritura digital pin P0 a 1'), kbd('pon pin digital 0 a')),
     'Si un LED no se enciende, dale la vuelta: puede estar al revés.'],
    '''basic.forever(function () {
    pins.digitalWritePin(DigitalPin.P2, 1)
    pins.digitalWritePin(DigitalPin.P1, 0)
    pins.digitalWritePin(DigitalPin.P0, 0)
    basic.pause(4000)
    pins.digitalWritePin(DigitalPin.P2, 0)
    pins.digitalWritePin(DigitalPin.P1, 1)
    basic.pause(1000)
    pins.digitalWritePin(DigitalPin.P1, 0)
    pins.digitalWritePin(DigitalPin.P0, 1)
    basic.pause(4000)
})''',
    "whenStarted\nforever {\n  digitalWriteOp 2 true\n  digitalWriteOp 1 false\n  digitalWriteOp 0 false\n  waitMillis 4000\n  digitalWriteOp 2 false\n  digitalWriteOp 1 true\n  waitMillis 1000\n  digitalWriteOp 1 false\n  digitalWriteOp 0 true\n  waitMillis 4000\n}",
    '''from microbit import *

while True:
    pin2.write_digital(1)
    pin1.write_digital(0)
    pin0.write_digital(0)
    sleep(4000)
    pin2.write_digital(0)
    pin1.write_digital(1)
    sleep(1000)
    pin1.write_digital(0)
    pin0.write_digital(1)
    sleep(4000)''',
    ['Añade un pulsador de peatones: al pulsar A, el semáforo pasa a rojo antes.', 'Muestra en la pantalla un muñeco andando cuando el semáforo esté en rojo para los coches.'],
    conexion=conexiones.semaforo(), group=C, icono='semaforo',
    materiales=[COCO + ' (6)', 'Tres LED: rojo, amarillo y verde', 'Tres resistencias de 220 Ω'])

practica(S, 'C3', 'juego-del-pulso', 'El juego del pulso', 3, 'P2', '50 min', ['entradas', 'variables', 'construcción'],
    'Construir el clásico juego del pulso: recorrer un camino de alambre con una anilla sin tocarlo. Cada roce suena y suma un fallo.',
    ['Dobla un alambre (o una tira de papel de aluminio sobre cartón) con curvas y fíjalo a una base. Conéctalo a GND.',
     'Haz una anilla con otro trozo de alambre y conéctala a P0.',
     'Cuando la anilla toque el camino, el circuito se cierra: P0 detecta el contacto.',
     'En [[pin_tocado]] (P0), [[cambiar]] fallos por 1, un [[tono]] y [[mostrar_numero]].',
     'Con A reinicia la partida.'],
    ['Usa el evento de pin presionado de P0: funciona porque el alambre une P0 con GND.',
     'Añade una espera tras cada roce para que un solo toque no cuente varias veces.'],
    '''let fallos = 0
input.onPinPressed(TouchPin.P0, function () {
    fallos += 1
    music.play(music.tonePlayable(196, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    basic.showNumber(fallos)
})
input.onButtonPressed(Button.A, function () {
    fallos = 0
    basic.showIcon(IconNames.Happy)
})''',
    "whenStarted\nfallos = 0\nled_displayImage 'happy'\n---\nwhenCondition ((digitalReadOp 0 'up') == false)\nfallos += 1\n'play frequency' 196 250\nscroll_text fallos\n---\nwhenButtonPressed 'A'\nfallos = 0\nled_displayImage 'happy'",
    '''from microbit import *
import music

fallos = 0
display.show(Image.HAPPY)
pin0.set_pull(pin0.PULL_UP)
while True:
    if pin0.read_digital() == 0:
        fallos += 1
        music.pitch(196, 250)
        display.scroll(fallos)
    if button_a.was_pressed():
        fallos = 0
        display.show(Image.HAPPY)''',
    ['Pon una zona de meta conectada a P1: al llegar, muestra los fallos y el tiempo.', 'Haz un ranking de la clase.'],
    conexion=conexiones.pulso(), group=C, icono='cocodrilo',
    materiales=[COCO + ' (2)', 'Alambre rígido (o papel de aluminio y cartón)', 'Plastilina o una base de corcho para sujetarlo'],
    explica='En MicroBlocks y Python leemos el pin en modo digital con resistencia interna hacia arriba (pull up): vale 1 en reposo y 0 cuando la anilla toca el alambre unido a GND.')

practica(S, 'C4', 'alarma-de-puerta', 'Alarma de puerta', 3, 'ESO', '45 min', ['entradas digitales', 'condicionales'],
    'Vigilar una puerta o una caja: dos láminas de aluminio se tocan cuando está cerrada. Si se abre, salta la alarma.',
    ['Pega una lámina de aluminio en el marco y otra en la puerta (o la tapa de una caja), de modo que se toquen al cerrar.',
     'Conecta una lámina a P1 y la otra a GND.',
     'Lee P1 con [[pin_digital]] (con resistencia interna hacia arriba): con la puerta cerrada vale 0; abierta, 1.',
     'Si vale 1, muestra una cara sorprendida y haz sonar una sirena; si vale 0, muestra el sí.',
     'Con A, activa o desactiva la vigilancia.'],
    ['Esto es un <b>interruptor</b> hecho a mano: dos conductores que se tocan o se separan.',
     'Recuerda la práctica 9: la sirena alterna dos frecuencias.'],
    '''pins.setPull(DigitalPin.P1, PinPullMode.PullUp)
let vigilando = true
input.onButtonPressed(Button.A, function () {
    vigilando = !(vigilando)
    if (vigilando) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
})
basic.forever(function () {
    if (vigilando && pins.digitalReadPin(DigitalPin.P1) == 1) {
        basic.showIcon(IconNames.Surprised)
        music.play(music.tonePlayable(880, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(660, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    }
})''',
    "whenStarted\nvigilando = (booleanConstant true)\nforever {\n  if (and vigilando ((digitalReadOp 1 'up') == true)) {\n    led_displayImage 'surprised'\n    'play frequency' 880 250\n    'play frequency' 660 250\n  }\n}\n---\nwhenButtonPressed 'A'\nvigilando = (not vigilando)\nif vigilando {\n  led_displayImage 'yes'\n} else {\n  led_displayImage 'no'\n}",
    '''from microbit import *
import music

pin1.set_pull(pin1.PULL_UP)
vigilando = True
while True:
    if button_a.was_pressed():
        vigilando = not vigilando
        display.show(Image.YES if vigilando else Image.NO)
    if vigilando and pin1.read_digital() == 1:
        display.show(Image.SURPRISED)
        music.pitch(880, 250)
        music.pitch(660, 250)''',
    ['Avisa por radio a otra placa en lugar de pitar (alarma silenciosa).', 'Cuenta cuántas veces se ha abierto la puerta durante el recreo.'],
    conexion=conexiones.alarma(), group=C, icono='casa', materiales=[COCO + ' (2)', 'Papel de aluminio y cinta adhesiva', 'Una caja con tapa o una puerta'])

# =================================================================== Sensores externos
practica(S, 'S1', 'humedad-de-la-tierra', 'Humedad de la tierra', 2, 'P2', '45 min', ['entradas analógicas', 'umbral'],
    'Saber si una planta necesita agua midiendo con dos clavos cuánto conduce la tierra: la tierra húmeda conduce más.',
    ['Clava dos clavos (o dos tornillos) en la maceta, separados unos 3 cm.',
     'Conecta un clavo a 3V y el otro a P1.',
     'Lee P1 con [[pin_leer]] (de 0 a 1023) y explora los valores con la tierra seca y recién regada.',
     'Con [[si_no]]: si el valor es [[menor]] que el umbral, cara triste y un [[tono]]; si no, cara contenta.'],
    ['Cuanta más agua, más corriente llega a P1 y mayor es el valor.',
     'Los clavos se oxidan con el tiempo: para medidas largas, sácalos de la tierra entre medida y medida o usa un sensor de humedad comercial.'],
    '''basic.forever(function () {
    if (pins.analogReadPin(AnalogPin.P1) < 300) {
        basic.showIcon(IconNames.Sad)
        music.play(music.tonePlayable(440, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    } else {
        basic.showIcon(IconNames.Happy)
    }
    basic.pause(2000)
})''',
    "whenStarted\nforever {\n  humedad = (analogReadOp 1)\n  sayIt humedad\n  if (humedad < 300) {\n    led_displayImage 'sad'\n    'play frequency' 440 250\n  } else {\n    led_displayImage 'happy'\n  }\n  waitMillis 2000\n}",
    '''from microbit import *
import music

while True:
    humedad = pin1.read_analog()
    if humedad < 300:
        display.show(Image.SAD)
        music.pitch(440, 250)
    else:
        display.show(Image.HAPPY)
    sleep(2000)''',
    ['Registra la humedad cada hora durante una semana y haz una gráfica.', 'Compara macetas con distintos tipos de tierra.'],
    conexion=conexiones.humedad(), group=SE, icono='planta', materiales=[COCO + ' (2)', 'Dos clavos o tornillos', 'Una maceta con tierra'])

practica(S, 'S2', 'potenciometro', 'El potenciómetro', 2, 'P2', '35 min', ['entradas analógicas', 'reescalar'],
    'Usar un potenciómetro (una rueda giratoria) como mando: al girarlo, una barra sube y baja en la pantalla y el tono cambia.',
    ['El potenciómetro tiene tres patas: conecta las de los extremos a 3V y GND, y la del centro a P2.',
     'Lee P2 con [[pin_leer]] y comprueba que va de 0 a 1023 al girar.',
     'Dibuja una barra con el valor (MakeCode: gráfico de barras).',
     'Al pulsar A, toca una nota cuya frecuencia dependa del valor.'],
    ['Un potenciómetro es un <b>divisor de tensión</b>: según la posición, a P2 le llega más o menos tensión.',
     'Para el tono, reescala de 0-1023 a 200-1000 Hz.'],
    '''basic.forever(function () {
    led.plotBarGraph(pins.analogReadPin(AnalogPin.P2), 1023)
})
input.onButtonPressed(Button.A, function () {
    music.play(music.tonePlayable(pins.map(pins.analogReadPin(AnalogPin.P2), 0, 1023, 200, 1000), music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
})''',
    "whenStarted\nforever {\n  filas = ('[misc:rescale]' (analogReadOp 2) 0 1023 0 5)\n  '[display:mbDisplayOff]'\n  for i filas {\n    for x 5 {\n      '[display:mbPlot]' x (6 - i)\n    }\n  }\n  waitMillis 100\n}\n---\nwhenButtonPressed 'A'\n'play frequency' ('[misc:rescale]' (analogReadOp 2) 0 1023 200 1000) 300",
    '''from microbit import *
import music

while True:
    valor = pin2.read_analog()
    filas = valor * 6 // 1024
    display.clear()
    for i in range(filas):
        for x in range(5):
            display.set_pixel(x, 4 - i, 9)
    if button_a.was_pressed():
        music.pitch(200 + valor * 800 // 1023, 300)
    sleep(100)''',
    ['Usa el potenciómetro para controlar la velocidad del juego «Atrapa la estrella».', 'Haz un theremín: que suene sin parar con el tono del potenciómetro.'],
    conexion=conexiones.potenciometro(), group=SE, icono='sensor', materiales=[COCO + ' (3)', 'Un potenciómetro de 10 kΩ'])

practica(S, 'S3', 'servo-que-saluda', 'Servo que saluda', 3, 'ESO', '40 min', ['servomotor', 'salidas analógicas'],
    'Mover un pequeño servomotor (SG90) con los botones: A lo lleva a un lado, B al otro y el logotipo lo hace saludar.',
    ['Conecta el servo: cable marrón (o negro) a GND, rojo a 3V y naranja (señal) a P0.',
     'En [[boton]] (A), [[servo]] a 0°; en B, a 180°.',
     'En [[logo]], con [[repetir]] 3 veces, alterna el [[servo]] entre 45° y 135°.',
     'Pega un brazo de cartulina al servo para que se vea mejor el movimiento.'],
    ['Un servo no gira sin parar: va al ángulo que le pidas y se queda ahí.',
     'MicroBlocks usa ángulos de −90 a 90 (0 es el centro).',
     'Python no tiene un bloque de servo: generamos la señal con <code>write_analog</code> (impulsos de 0,5 a 2,5 ms cada 20 ms).'],
    '''input.onButtonPressed(Button.A, function () {
    pins.servoWritePin(AnalogPin.P0, 0)
})
input.onButtonPressed(Button.B, function () {
    pins.servoWritePin(AnalogPin.P0, 180)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    for (let index = 0; index < 3; index++) {
        pins.servoWritePin(AnalogPin.P0, 45)
        basic.pause(300)
        pins.servoWritePin(AnalogPin.P0, 135)
        basic.pause(300)
    }
})''',
    "whenButtonPressed 'A'\nsetServoAngle 0 -90\n---\nwhenButtonPressed 'B'\nsetServoAngle 0 90\n---\nwhenCondition (touchPin_logoTouched)\nrepeat 3 {\n  setServoAngle 0 -45\n  waitMillis 300\n  setServoAngle 0 45\n  waitMillis 300\n}",
    '''from microbit import *

pin0.set_analog_period(20)

def angulo(grados):
    # de 0-180 grados a impulsos de 0,5-2,5 ms (valores de 26 a 128)
    pin0.write_analog(26 + grados * 102 // 180)

while True:
    if button_a.was_pressed():
        angulo(0)
    if button_b.was_pressed():
        angulo(180)
    if pin_logo.is_touched():
        for i in range(3):
            angulo(45)
            sleep(300)
            angulo(135)
            sleep(300)''',
    ['Usa el potenciómetro para mover el servo a mano.', 'Construye una barrera de aparcamiento que se abre al pulsar A.'],
    conexion=conexiones.servo(), group=SE, icono='servo', materiales=[COCO + ' (3) o cables macho para el conector del servo', 'Un microservo SG90'],
    nota=box('ojo', 'Alimentación', P('Un microservo SG90 suele funcionar con los 3 V de la micro:bit si se alimenta con pilas nuevas o USB, pero si se reinicia la placa o tiembla, '
        'usa una placa de expansión con alimentación propia. No conectes servos grandes directamente.')))
