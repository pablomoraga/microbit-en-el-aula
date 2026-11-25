# -*- coding: utf-8 -*-
"""Encuentra el error: 10 programas con un fallo escondido para aprender a depurar."""
from common import page, P, ul, ol, box, soluciones, e, NIVEL, ETAPA
from iconos import icon
from c_comenzamos import bm

S = 'errores'
GRUPOS = {}

def error(num, slug, title, nivel, etapa, debe, sintoma, pistas, explicacion, mal, bien, icono='lupa'):
    """mal y bien: tuplas (MakeCode, MicroBlocks, Python)."""
    head = ('<div class="ficha"><span class="chip chip-num">%s</span><span class="chip">Dificultad %s</span><span class="chip">%s</span>'
            '<span class="chip">%s 10-15 min</span><span class="chip chip-c">depurar</span></div>') % (e(num), NIVEL[nivel], e(ETAPA[etapa]), icon('reloj', 14))
    body = head + '<div class="objetivo">%s<div><b>Lo que debería hacer</b><p>%s</p></div></div>' % (icon('diana', 28), debe)
    body += box('ojo', 'Lo que pasa', P(sintoma))
    body += '<h2>El programa con el error</h2>' + P('Pruébalo en el simulador o cárgalo en la placa. Lee el programa bloque a bloque y busca la diferencia entre lo que hace y lo que debería hacer.')
    body += soluciones(slug + '-con-error', mal[0], mal[1], mal[2], desc=title + ' (con error)')
    body += '<details class="ayuda"><summary>%s Ayuda: pistas</summary>%s</details>' % (icon('salvavidas', 18), ul(pistas))
    body += ('<details class="ayuda sol"><summary>%s El error y la solución</summary><p>%s</p>%s</details>' % (
        icon('check', 18), explicacion, soluciones(slug, bien[0], bien[1], bien[2], desc=title + ' (corregido)')))
    page(S, slug, title, body, kind='practica', meta=dict(num=num, nivel=nivel, tiempo='10-15 min', etapa=etapa), icono=icono)

error('E1', 'el-corazon-quieto', 'El corazón que no late', 1, 'P1',
    'Un corazón que late sin parar: grande, pequeño, grande, pequeño…',
    'El corazón aparece, pero se queda quieto: no late nunca.',
    ['Mira las dos imágenes que se muestran dentro del bucle. ¿Son distintas?', 'Una animación necesita al menos dos fotogramas diferentes.'],
    'Las dos imágenes son el corazón grande, así que la pantalla nunca cambia. La segunda tiene que ser el <b>corazón pequeño</b>.',
    ('basic.forever(function () {\n    basic.showIcon(IconNames.Heart)\n    basic.pause(500)\n    basic.showIcon(IconNames.Heart)\n    basic.pause(500)\n})',
     "whenStarted\nforever {\n  led_displayImage 'heart'\n  waitMillis 500\n  led_displayImage 'heart'\n  waitMillis 500\n}",
     'from microbit import *\n\nwhile True:\n    display.show(Image.HEART)\n    sleep(500)\n    display.show(Image.HEART)\n    sleep(500)'),
    ('basic.forever(function () {\n    basic.showIcon(IconNames.Heart)\n    basic.pause(500)\n    basic.showIcon(IconNames.SmallHeart)\n    basic.pause(500)\n})',
     "whenStarted\nforever {\n  led_displayImage 'heart'\n  waitMillis 500\n  led_displayImage 'small heart'\n  waitMillis 500\n}",
     'from microbit import *\n\nwhile True:\n    display.show(Image.HEART)\n    sleep(500)\n    display.show(Image.HEART_SMALL)\n    sleep(500)'),
    icono='corazon')

error('E2', 'el-dado-tramposo', 'El dado tramposo', 1, 'P1',
    'Al agitar la placa sale un número al azar del 1 al 6, como en un dado.',
    'Después de muchas tiradas, el 6 no sale nunca.',
    ['Fíjate en los dos números del bloque de azar.', 'Lanza el dado 20 veces y apunta los resultados: ¿cuál falta?'],
    'El número al azar va de 1 a <b>5</b>. Hay que cambiarlo por 1 a <b>6</b>.',
    ('input.onGesture(Gesture.Shake, function () {\n    basic.showNumber(randint(1, 5))\n})',
     "whenCondition (('[sensors:acceleration]') > 200)\nscroll_text (random 1 5)\nwaitMillis 500",
     'from microbit import *\nimport random\n\nwhile True:\n    if accelerometer.was_gesture("shake"):\n        display.show(random.randint(1, 5))'),
    ('input.onGesture(Gesture.Shake, function () {\n    basic.showNumber(randint(1, 6))\n})',
     "whenCondition (('[sensors:acceleration]') > 200)\nscroll_text (random 1 6)\nwaitMillis 500",
     'from microbit import *\nimport random\n\nwhile True:\n    if accelerometer.was_gesture("shake"):\n        display.show(random.randint(1, 6))'),
    icono='dado')

error('E3', 'el-contador-atascado', 'El contador atascado', 2, 'P1',
    'Cada vez que pulsas A, el contador sube uno: 1, 2, 3, 4…',
    'Por mucho que pulses A, el contador siempre muestra 1.',
    ['¿El bloque del botón A <b>suma</b> 1 o <b>pone</b> la variable a 1?', 'Compara «fijar contador a 1» con «cambiar contador por 1».'],
    'El programa <b>fija</b> la variable a 1 en cada pulsación, en lugar de <b>aumentarla</b> en 1. Hay que usar «cambiar… por 1» (MakeCode) o «aumenta… en 1» (MicroBlocks), o <code>+= 1</code> en Python.',
    ('let contador = 0\ninput.onButtonPressed(Button.A, function () {\n    contador = 1\n    basic.showNumber(contador)\n})',
     "whenStarted\ncontador = 0\n---\nwhenButtonPressed 'A'\ncontador = 1\nscroll_text contador",
     'from microbit import *\n\ncontador = 0\nwhile True:\n    if button_a.was_pressed():\n        contador = 1\n        display.scroll(contador)'),
    ('let contador = 0\ninput.onButtonPressed(Button.A, function () {\n    contador += 1\n    basic.showNumber(contador)\n})',
     "whenStarted\ncontador = 0\n---\nwhenButtonPressed 'A'\ncontador += 1\nscroll_text contador",
     'from microbit import *\n\ncontador = 0\nwhile True:\n    if button_a.was_pressed():\n        contador += 1\n        display.scroll(contador)'),
    icono='pulsador')

ALL = ('11111',) * 5
error('E4', 'la-luz-al-reves', 'La luz de noche al revés', 2, 'P1',
    'Encender todos los LED cuando está oscuro y apagarlos cuando hay luz.',
    'Funciona justo al revés: con la luz encendida se iluminan los LED y, al tapar la placa, se apagan.',
    ['Mira el signo de la comparación: ¿«menor que» o «mayor que»?', 'Lee la condición en voz alta: «si el nivel de luz es mayor que 30…». ¿Es eso «oscuro»?'],
    'La condición usa <b>mayor que</b> (&gt;) y debería usar <b>menor que</b> (&lt;): está oscuro cuando el nivel de luz es pequeño.',
    ('basic.forever(function () {\n    if (input.lightLevel() > 30) {\n        basic.showLeds(`\n            # # # # #\n            # # # # #\n            # # # # #\n            # # # # #\n            # # # # #\n            `)\n    } else {\n        basic.clearScreen()\n    }\n})',
     "whenStarted\nforever {\n  if (('[display:lightLevel]') > 100) {\n    '[display:mbDisplay]' %d\n  } else {\n    '[display:mbDisplayOff]'\n  }\n  waitMillis 200\n}" % bm(*ALL),
     'from microbit import *\n\nwhile True:\n    if display.read_light_level() > 30:\n        display.show(Image("99999:99999:99999:99999:99999"))\n    else:\n        display.clear()\n    sleep(200)'),
    ('basic.forever(function () {\n    if (input.lightLevel() < 30) {\n        basic.showLeds(`\n            # # # # #\n            # # # # #\n            # # # # #\n            # # # # #\n            # # # # #\n            `)\n    } else {\n        basic.clearScreen()\n    }\n})',
     "whenStarted\nforever {\n  if (('[display:lightLevel]') < 100) {\n    '[display:mbDisplay]' %d\n  } else {\n    '[display:mbDisplayOff]'\n  }\n  waitMillis 200\n}" % bm(*ALL),
     'from microbit import *\n\nwhile True:\n    if display.read_light_level() < 30:\n        display.show(Image("99999:99999:99999:99999:99999"))\n    else:\n        display.clear()\n    sleep(200)'),
    icono='sol')

error('E5', 'la-cuenta-atras-loca', 'La cuenta atrás loca', 1, 'P1',
    'Al pulsar A, cuenta atrás 3, 2, 1 y muestra una flecha de despegue.',
    'La cuenta sale en otro orden: 1, 2, 3… y después la flecha.',
    ['Lee los bloques de arriba abajo: ¿en qué orden aparecen los números?', 'En una secuencia, el orden de los bloques es el orden en que pasan las cosas.'],
    'Los números están en orden creciente. En una cuenta atrás el primero tiene que ser el 3 y el último el 1: basta con intercambiar el 3 y el 1.',
    ('input.onButtonPressed(Button.A, function () {\n    basic.showNumber(1)\n    basic.showNumber(2)\n    basic.showNumber(3)\n    basic.showArrow(ArrowNames.North)\n})',
     "whenButtonPressed 'A'\ndisplayCharacter '1'\nwaitMillis 700\ndisplayCharacter '2'\nwaitMillis 700\ndisplayCharacter '3'\nwaitMillis 700\n'[display:mbDisplay]' 4347332",
     'from microbit import *\n\nwhile True:\n    if button_a.was_pressed():\n        display.show(1)\n        sleep(700)\n        display.show(2)\n        sleep(700)\n        display.show(3)\n        sleep(700)\n        display.show(Image.ARROW_N)'),
    ('input.onButtonPressed(Button.A, function () {\n    basic.showNumber(3)\n    basic.showNumber(2)\n    basic.showNumber(1)\n    basic.showArrow(ArrowNames.North)\n})',
     "whenButtonPressed 'A'\ndisplayCharacter '3'\nwaitMillis 700\ndisplayCharacter '2'\nwaitMillis 700\ndisplayCharacter '1'\nwaitMillis 700\n'[display:mbDisplay]' 4347332",
     'from microbit import *\n\nwhile True:\n    if button_a.was_pressed():\n        display.show(3)\n        sleep(700)\n        display.show(2)\n        sleep(700)\n        display.show(1)\n        sleep(700)\n        display.show(Image.ARROW_N)'),
    icono='cohete')

error('E6', 'el-boton-equivocado', 'El botón equivocado', 1, 'P1',
    'Al pulsar A se muestra la temperatura.',
    'Al pulsar A no pasa nada… pero al pulsar B sí aparece la temperatura.',
    ['Revisa el menú del evento: ¿qué botón tiene elegido?'],
    'El evento está configurado para el botón <b>B</b>. Hay que cambiar el menú a <b>A</b> (en Python, <code>button_a</code>).',
    ('input.onButtonPressed(Button.B, function () {\n    basic.showNumber(input.temperature())\n})',
     "whenButtonPressed 'B'\nscroll_text ('[sensors:temperature]')",
     'from microbit import *\n\nwhile True:\n    if button_b.was_pressed():\n        display.scroll(temperature())'),
    ('input.onButtonPressed(Button.A, function () {\n    basic.showNumber(input.temperature())\n})',
     "whenButtonPressed 'A'\nscroll_text ('[sensors:temperature]')",
     'from microbit import *\n\nwhile True:\n    if button_a.was_pressed():\n        display.scroll(temperature())'),
    icono='termometro')

error('E7', 'los-pasos-que-se-borran', 'Los pasos que se borran', 2, 'P2',
    'Un podómetro: cada sacudida suma un paso y se ve el total.',
    'Por muchos pasos que des, la pantalla siempre muestra 1.',
    ['¿Dónde se pone la variable a 0? ¿Cuántas veces se ejecuta ese bloque?', 'Poner a cero debería pasar una sola vez, al principio.'],
    'La variable se pone a 0 <b>dentro</b> del evento, justo antes de sumar: en cada paso vuelve a empezar. El «fijar pasos a 0» tiene que ir en <b>al iniciar</b> (o fuera del bucle en Python).',
    ('let pasos = 0\ninput.onGesture(Gesture.Shake, function () {\n    pasos = 0\n    pasos += 1\n    basic.showNumber(pasos)\n})',
     "whenCondition (('[sensors:acceleration]') > 200)\npasos = 0\npasos += 1\nscroll_text pasos",
     'from microbit import *\n\nwhile True:\n    if accelerometer.was_gesture("shake"):\n        pasos = 0\n        pasos += 1\n        display.scroll(pasos)'),
    ('let pasos = 0\ninput.onGesture(Gesture.Shake, function () {\n    pasos += 1\n    basic.showNumber(pasos)\n})',
     "whenStarted\npasos = 0\n---\nwhenCondition (('[sensors:acceleration]') > 200)\npasos += 1\nscroll_text pasos",
     'from microbit import *\n\npasos = 0\nwhile True:\n    if accelerometer.was_gesture("shake"):\n        pasos += 1\n        display.scroll(pasos)'),
    icono='acelerometro')

error('E8', 'el-ruido-que-nunca-enfada', 'El ruido que nunca se enfada', 3, 'P2',
    'Cara contenta con poco ruido, cara regular con ruido medio y cara enfadada con mucho ruido.',
    'Aunque gritéis, la cara enfadada no aparece nunca: como mucho, la regular.',
    ['Cuando el ruido es muy alto, ¿qué condición se cumple primero?', 'En un «si… si no, si…» solo se ejecuta la <b>primera</b> rama que se cumple.'],
    'Las condiciones están en mal orden: un ruido de 150 ya cumple «mayor que 50», así que nunca llega a comprobar «mayor que 120». Hay que comprobar primero el valor <b>más alto</b>.',
    ('basic.forever(function () {\n    if (input.soundLevel() > 50) {\n        basic.showIcon(IconNames.Meh)\n    } else if (input.soundLevel() > 120) {\n        basic.showIcon(IconNames.Angry)\n    } else {\n        basic.showIcon(IconNames.Happy)\n    }\n})',
     "whenStarted\nforever {\n  if ((loudness) > 60) {\n    led_displayImage 'meh'\n  } ((loudness) > 150) {\n    led_displayImage 'angry'\n  } else {\n    led_displayImage 'happy'\n  }\n  waitMillis 100\n}",
     'from microbit import *\n\nwhile True:\n    nivel = microphone.sound_level()\n    if nivel > 50:\n        display.show(Image.MEH)\n    elif nivel > 120:\n        display.show(Image.ANGRY)\n    else:\n        display.show(Image.HAPPY)\n    sleep(100)'),
    ('basic.forever(function () {\n    if (input.soundLevel() > 120) {\n        basic.showIcon(IconNames.Angry)\n    } else if (input.soundLevel() > 50) {\n        basic.showIcon(IconNames.Meh)\n    } else {\n        basic.showIcon(IconNames.Happy)\n    }\n})',
     "whenStarted\nforever {\n  if ((loudness) > 150) {\n    led_displayImage 'angry'\n  } ((loudness) > 60) {\n    led_displayImage 'meh'\n  } else {\n    led_displayImage 'happy'\n  }\n  waitMillis 100\n}",
     'from microbit import *\n\nwhile True:\n    nivel = microphone.sound_level()\n    if nivel > 120:\n        display.show(Image.ANGRY)\n    elif nivel > 50:\n        display.show(Image.MEH)\n    else:\n        display.show(Image.HAPPY)\n    sleep(100)'),
    icono='microfono')

error('E9', 'la-radio-sorda', 'La radio sorda', 3, 'P2',
    'Al pulsar A, una placa envía «Hola» por radio y las demás lo muestran.',
    'Las dos placas tienen el programa y el mismo grupo, pero el mensaje no aparece nunca.',
    ['¿Qué tipo de dato se envía: un número o un texto?', '¿Y qué tipo de dato espera recibir el programa?'],
    'Se envía un <b>texto</b>, pero el programa solo escucha <b>números</b>. El evento de recepción tiene que ser el de texto (en MicroBlocks, «último texto recibido por radio»).',
    ('radio.setGroup(1)\ninput.onButtonPressed(Button.A, function () {\n    radio.sendString("Hola")\n})\nradio.onReceivedNumber(function (receivedNumber) {\n    basic.showNumber(receivedNumber)\n})',
     "whenStarted\n'[radio:setGroup]' 1\n---\nwhenButtonPressed 'A'\n'[radio:sendString]' 'Hola'\n---\nwhenCondition ('[radio:messageReceived]')\nscroll_text ('[radio:receivedInteger]')",
     'from microbit import *\nimport radio\n\nradio.on()\nradio.config(group=1)\nwhile True:\n    if button_a.was_pressed():\n        radio.send("Hola")\n    mensaje = radio.receive()\n    if mensaje == 1:\n        display.scroll(mensaje)'),
    ('radio.setGroup(1)\ninput.onButtonPressed(Button.A, function () {\n    radio.sendString("Hola")\n})\nradio.onReceivedString(function (receivedString) {\n    basic.showString(receivedString)\n})',
     "whenStarted\n'[radio:setGroup]' 1\n---\nwhenButtonPressed 'A'\n'[radio:sendString]' 'Hola'\n---\nwhenCondition ('[radio:messageReceived]')\nscroll_text ('[radio:receivedString]')",
     'from microbit import *\nimport radio\n\nradio.on()\nradio.config(group=1)\nwhile True:\n    if button_a.was_pressed():\n        radio.send("Hola")\n    mensaje = radio.receive()\n    if mensaje:\n        display.scroll(mensaje)'),
    icono='antena')

error('E10', 'la-canica-escapista', 'La canica escapista', 3, 'ESO',
    'Un LED que se mueve al inclinar la placa a izquierda y derecha, sin salirse de la pantalla.',
    'Al inclinar a la derecha, la canica desaparece por el borde y tarda en volver.',
    ['¿Qué pasa con x cuando ya vale 4 y sigues inclinando?', 'Falta comprobar un límite: la pantalla solo tiene columnas de 0 a 4.'],
    'Al moverse a la derecha no se comprueba el límite, así que x pasa de 4 y la canica sale de la pantalla. Hay que añadir la condición «y x &lt; 4» (en MicroBlocks, «x &lt; 5»).',
    ('let x = 2\nbasic.forever(function () {\n    if (input.acceleration(Dimension.X) > 200) {\n        x += 1\n    } else if (input.acceleration(Dimension.X) < -200 && x > 0) {\n        x += -1\n    }\n    basic.clearScreen()\n    led.plot(x, 2)\n    basic.pause(150)\n})',
     "whenStarted\nx = 3\nforever {\n  if (('[sensors:tiltX]') > 20) {\n    x += 1\n  } (and (('[sensors:tiltX]') < -20) (x > 1)) {\n    x += -1\n  }\n  '[display:mbDisplayOff]'\n  '[display:mbPlot]' x 3\n  waitMillis 150\n}",
     'from microbit import *\n\nx = 2\nwhile True:\n    ax = accelerometer.get_x()\n    if ax > 200:\n        x += 1\n    elif ax < -200 and x > 0:\n        x -= 1\n    display.clear()\n    if 0 <= x <= 4:\n        display.set_pixel(x, 2, 9)\n    sleep(150)'),
    ('let x = 2\nbasic.forever(function () {\n    if (input.acceleration(Dimension.X) > 200 && x < 4) {\n        x += 1\n    } else if (input.acceleration(Dimension.X) < -200 && x > 0) {\n        x += -1\n    }\n    basic.clearScreen()\n    led.plot(x, 2)\n    basic.pause(150)\n})',
     "whenStarted\nx = 3\nforever {\n  if (and (('[sensors:tiltX]') > 20) (x < 5)) {\n    x += 1\n  } (and (('[sensors:tiltX]') < -20) (x > 1)) {\n    x += -1\n  }\n  '[display:mbDisplayOff]'\n  '[display:mbPlot]' x 3\n  waitMillis 150\n}",
     'from microbit import *\n\nx = 2\nwhile True:\n    ax = accelerometer.get_x()\n    if ax > 200 and x < 4:\n        x += 1\n    elif ax < -200 and x > 0:\n        x -= 1\n    display.clear()\n    display.set_pixel(x, 2, 9)\n    sleep(150)'),
    icono='acelerometro')
