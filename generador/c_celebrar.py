# -*- coding: utf-8 -*-
"""Para celebrar: actividades cortas para efemérides (se irá ampliando)."""
from common import page, P, ul, ol, box, h2, soluciones, e
from c_comenzamos import bm

S = 'celebrar'
GRUPOS = {}

from bloques import expand
from iconos import icon

def construir(recortable, ideas, enlaces=()):
    """Bloque «Para construirlo»: recortable imprimible, ideas con cartón y enlaces oficiales."""
    out = '<section class="construir"><h2>Para construirlo</h2><div class="construir-g">'
    out += ('<a class="recortable" href="../recursos/recortables/%s.svg" target="_blank" rel="noopener"><img src="../recursos/recortables/%s.svg" alt="Recortable" loading="lazy">'
            '<span>%s Recortable para imprimir (A4)</span></a>') % (recortable, recortable, icon('descarga', 16))
    out += '<div>' + box('material', 'Ideas con cartón y material de clase', ul(ideas))
    if enlaces:
        out += box('sabias', 'Recursos oficiales de micro:bit', ul(['<a href="%s" target="_blank" rel="noopener">%s</a>: %s' % (u, t, d) for t, u, d in enlaces]))
    return out + '</div></div></section>'

def actividad(slug, titulo, tiempo, objetivo, pasos, mc, mb, py):
    return ('<section class="actividad"><h2>%s</h2><div class="ficha"><span class="chip">⏱ %s</span></div><div class="objetivo"><div><b>Objetivo</b><p>%s</p></div></div>'
            '<h3>Paso a paso</h3>%s<details class="ayuda sol"><summary>Una solución posible</summary>%s</details></section>') % (
        e(titulo), e(tiempo), objetivo, ol([expand(x) for x in pasos]), soluciones(slug, mc, mb, py, desc=titulo))

CAL = ('01110', '11111', '10101', '11111', '01010')
page(S, 'halloween', 'Halloween', P('31 de octubre. Dos actividades de 20 minutos para crear objetos que asustan… un poco.') +
    actividad('halloween-calabaza', 'Calabaza que se despierta', '20 min',
        'Una calabaza dormida que abre los ojos y se ríe cuando apagas la luz.',
        ['Dibuja la calabaza con [[mostrar_leds]] (ojos, boca y tallo).', 'En [[para_siempre]], con [[si_no]]: si [[luz]] [[menor]] el umbral, muestra la calabaza y un [[efecto]] de risa.',
         'Si no, [[mostrar_icono]] con la cara dormida.', 'Mete la placa en una calabaza de cartulina o de verdad (vacía y seca).'],
        'basic.forever(function () {\n    if (input.lightLevel() < 30) {\n        basic.showLeds(`\n            . # # # .\n            # # # # #\n            # . # . #\n            # # # # #\n            . # . # .\n            `)\n        music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.UntilDone)\n    } else {\n        basic.showIcon(IconNames.Asleep)\n    }\n})',
        "whenStarted\nforever {\n  if (('[display:lightLevel]') < 100) {\n    '[display:mbDisplay]' %d\n    repeat 3 {\n      'play tone' 'nt;g' 1 90\n      'play tone' 'nt;e' 1 90\n    }\n  } else {\n    led_displayImage 'asleep'\n  }\n  waitMillis 300\n}" % bm(*CAL),
        'from microbit import *\n\nCALABAZA = Image("09990:99999:90909:99999:09090")\nwhile True:\n    if display.read_light_level() < 30:\n        display.show(CALABAZA)\n        audio.play(Sound.GIGGLE)\n    else:\n        display.show(Image.ASLEEP)\n    sleep(300)') +
    actividad('halloween-fantasma', 'El fantasma asustadizo', '15 min',
        'Un fantasma que aparece cuando agitas la placa y desaparece poco a poco.',
        ['En [[agitar]], [[mostrar_icono]] con el fantasma y un [[efecto]] misterioso.', 'Después, [[borrar]].', 'Escóndelo en una caja: ¿quién se atreve a moverla?'],
        'input.onGesture(Gesture.Shake, function () {\n    basic.showIcon(IconNames.Ghost)\n    music.play(music.builtinPlayableSoundEffect(soundExpression.mysterious), music.PlaybackMode.UntilDone)\n    basic.clearScreen()\n})',
        "whenCondition (('[sensors:acceleration]') > 200)\nled_displayImage 'ghost'\n'play tone' 'nt;e' 0 400\n'play tone' 'nt;d' 0 400\n'play tone' 'nt;c' 0 800\n'[display:mbDisplayOff]'",
        'from microbit import *\n\nwhile True:\n    if accelerometer.was_gesture("shake"):\n        display.show(Image.GHOST)\n        audio.play(Sound.MYSTERIOUS)\n        display.clear()') + construir('calabaza', [
        'Imprime el recortable en cartulina naranja o coloréalo. Recorta la ventana y pega la micro:bit por detrás con cinta de carrocero.',
        'Haz un soporte con un trozo de cartón doblado en forma de triángulo para que la calabaza se tenga en pie.',
        'Para la actividad de la calabaza que se despierta, deja el frente de la placa al descubierto: el sensor de luz son los propios LED.'],
        [('Halloween project', 'https://microbit.org/projects/make-it-code-it/halloween-project/', 'proyecto oficial con dos placas que se comunican por radio (en inglés)')]),
    icono='calabaza', kind='celebrar')

MATRAZ1 = ('01110', '00100', '01010', '10001', '11111')
MATRAZ2 = ('00100', '00100', '01010', '11011', '11111')
page(S, 'dia-de-la-nina-en-la-ciencia', 'Día de la Niña y la Mujer en la Ciencia', P(
    '11 de febrero, Día Internacional de la Mujer y la Niña en la Ciencia. La micro:bit es una buena excusa para conocer a científicas e ingenieras. '
    'Por ejemplo, <b>Hedy Lamarr</b> coinventó un sistema de salto de frecuencias en el que se inspiran tecnologías inalámbricas actuales, como el Bluetooth que usa la propia placa.') +
    actividad('ciencia-cientificas', 'Galería de científicas', '25 min',
        'Una lista de científicas que van apareciendo, una a una, cada vez que pulsas A. Con B, una al azar.',
        ['Investigad en grupo y elegid cinco científicas o ingenieras.', 'Guardad sus nombres en una [[lista]] (sin tildes).',
         'En [[boton]] (A), [[mostrar_texto]] con el [[elemento]] siguiente; al llegar al final, vuelve a la primera.', 'En [[boton]] (B), una al [[azar]]. Quien la vea, cuenta qué descubrió.'],
        'let cientificas = ["Ada Lovelace", "Marie Curie", "Hedy Lamarr", "Margarita Salas", "Katherine Johnson"]\nlet i = 0\ninput.onButtonPressed(Button.A, function () {\n    basic.showString(cientificas[i])\n    i = (i + 1) % cientificas.length\n})\ninput.onButtonPressed(Button.B, function () {\n    basic.showString(cientificas[randint(0, cientificas.length - 1)])\n})',
        "whenStarted\ncientificas = ('[data:makeList]' 'Ada Lovelace' 'Marie Curie' 'Hedy Lamarr' 'Margarita Salas' 'Katherine Johnson')\ni = 1\n---\nwhenButtonPressed 'A'\nscroll_text (at i cientificas)\ni = ((i % (size cientificas)) + 1)\n---\nwhenButtonPressed 'B'\nscroll_text (at (random 1 (size cientificas)) cientificas)",
        'from microbit import *\nimport random\n\ncientificas = ["Ada Lovelace", "Marie Curie", "Hedy Lamarr", "Margarita Salas", "Katherine Johnson"]\ni = 0\nwhile True:\n    if button_a.was_pressed():\n        display.scroll(cientificas[i])\n        i = (i + 1) % len(cientificas)\n    if button_b.was_pressed():\n        display.scroll(random.choice(cientificas))') +
    actividad('ciencia-matraz', 'El matraz burbujeante', '15 min',
        'Un matraz de laboratorio animado cuyas burbujas suben, con una frase al tocar el logotipo.',
        ['Dibuja con [[mostrar_leds]] dos fotogramas del matraz con burbujas en distinta posición.', 'Altérnalos dentro de [[para_siempre]].', 'En [[logo]], [[mostrar_texto]] «La ciencia es cosa de todas».'],
        'basic.forever(function () {\n    basic.showLeds(`\n        . # # # .\n        . . # . .\n        . # . # .\n        # . . . #\n        # # # # #\n        `)\n    basic.showLeds(`\n        . . # . .\n        . . # . .\n        . # . # .\n        # # . # #\n        # # # # #\n        `)\n})\ninput.onLogoEvent(TouchButtonEvent.Pressed, function () {\n    basic.showString("La ciencia es cosa de todas")\n})',
        "whenStarted\nforever {\n  '[display:mbDisplay]' %d\n  waitMillis 400\n  '[display:mbDisplay]' %d\n  waitMillis 400\n}\n---\nwhenCondition (touchPin_logoTouched)\nscroll_text 'La ciencia es cosa de todas'" % (bm(*MATRAZ1), bm(*MATRAZ2)),
        'from microbit import *\n\nM1 = Image("09990:00900:09090:90009:99999")\nM2 = Image("00900:00900:09090:99099:99999")\nwhile True:\n    if pin_logo.is_touched():\n        display.scroll("La ciencia es cosa de todas")\n    display.show(M1)\n    sleep(400)\n    display.show(M2)\n    sleep(400)') + construir('matraz', [
        'Imprime el matraz, recorta la ventana y coloca la placa detrás: las burbujas de la animación quedarán dentro del matraz.',
        'Haced un mural de científicas: cada pareja prepara una ficha de cartulina con la foto, el nombre y lo que descubrió.',
        'Pega el matraz en un tubo de cartón (de papel de cocina) para que se tenga en pie.']),
    icono='matraz', kind='celebrar')

ARBOL = ('00100', '01110', '11111', '01110', '11111')
page(S, 'navidad', 'Navidad', P('Diciembre. Un árbol con luces que parpadean y una felicitación que viaja por radio a todas las placas de la clase.') +
    actividad('navidad-arbol', 'Árbol con luces', '20 min',
        'Un árbol de Navidad cuyas luces se apagan y encienden al azar. Al pulsar A suena un villancico.',
        ['Dibuja el árbol con [[mostrar_leds]].', 'En [[para_siempre]], [[ocultar]] un LED al [[azar]], [[pausa]] y vuelve a dibujar el árbol.', 'En [[boton]] (A), una [[melodia]] navideña.'],
        'basic.forever(function () {\n    basic.showLeds(`\n        . . # . .\n        . # # # .\n        # # # # #\n        . # # # .\n        # # # # #\n        `)\n    led.unplot(randint(0, 4), randint(1, 4))\n    basic.pause(300)\n})\ninput.onButtonPressed(Button.A, function () {\n    music.play(music.builtInPlayableMelody(Melodies.JumpUp), music.PlaybackMode.InBackground)\n})',
        "whenStarted\nforever {\n  '[display:mbDisplay]' %d\n  '[display:mbUnplot]' (random 1 5) (random 2 5)\n  waitMillis 300\n}\n---\nwhenButtonPressed 'A'\n'play tone' 'nt;e' 1 200\n'play tone' 'nt;e' 1 200\n'play tone' 'nt;e' 1 400\n'play tone' 'nt;e' 1 200\n'play tone' 'nt;e' 1 200\n'play tone' 'nt;e' 1 400" % bm(*ARBOL),
        'from microbit import *\nimport random\nimport music\n\nARBOL = Image("00900:09990:99999:09990:99999")\nwhile True:\n    luces = ARBOL.copy()\n    luces.set_pixel(random.randint(0, 4), random.randint(1, 4), 0)\n    display.show(luces)\n    if button_a.was_pressed():\n        music.play(["E5:2", "E5:2", "E5:4", "E5:2", "E5:2", "E5:4"], wait=False)\n    sleep(300)') +
    actividad('navidad-felicitacion', 'Felicitación por radio', '15 min',
        'Enviar una felicitación a todas las placas de la clase a la vez.',
        ['Todas las placas con el mismo [[radio_grupo]].', 'En [[boton]] (A), [[radio_enviar_texto]] «Felices fiestas».', 'Con [[radio_recibir_texto]], [[mostrar_texto]] y un sonido de campanilla.'],
        'radio.setGroup(25)\ninput.onButtonPressed(Button.A, function () {\n    radio.sendString("Felices fiestas")\n})\nradio.onReceivedString(function (receivedString) {\n    music.play(music.builtinPlayableSoundEffect(soundExpression.twinkle), music.PlaybackMode.InBackground)\n    basic.showString(receivedString)\n})',
        "whenStarted\n'[radio:setGroup]' 25\n---\nwhenButtonPressed 'A'\n'[radio:sendString]' 'Felices fiestas'\n---\nwhenCondition ('[radio:messageReceived]')\n'play tone' 'nt;c' 2 100\n'play tone' 'nt;g' 1 200\nscroll_text ('[radio:receivedString]')",
        'from microbit import *\nimport radio\n\nradio.on()\nradio.config(group=25)\nwhile True:\n    if button_a.was_pressed():\n        radio.send("Felices fiestas")\n    mensaje = radio.receive()\n    if mensaje:\n        audio.play(Sound.TWINKLE, wait=False)\n        display.scroll(mensaje)') + construir('arbol-de-navidad', [
        'Imprime el árbol en cartulina verde, recorta la ventana y coloca la micro:bit detrás: las luces del programa serán las bolas del árbol.',
        'Decora la estrella con papel de aluminio y pega el árbol a una caja de cartón que esconda el portapilas.',
        'Para la felicitación por radio, cada alumno puede decorar su propia tarjeta de cartulina con la placa dentro.'],
        [('Festive decoration', 'https://microbit.org/projects/make-it-code-it/festive-decoration/', 'una estrella que brilla cuando la habitación se oscurece (en inglés)'),
         ('micro:bit holiday activities', 'https://microbit.org/news/2020-12-03/microbit-holiday-activities/', 'ideas y melodías navideñas de la fundación (en inglés)')]),
    icono='arbol', kind='celebrar')

page(S, 'verano', 'Verano', P('Junio. Dos actividades para despedir el curso pensando en el sol y el calor.') +
    actividad('verano-sombra', 'Busca la sombra', '15 min',
        'Un avisador que, si hace mucho calor o mucha luz, recomienda buscar la sombra.',
        ['En [[para_siempre]], con [[si_no]]: si [[temperatura]] [[mayor]] 30 [[o]] [[luz]] es muy alto, [[mostrar_texto]] «Sombra».', 'Si no, [[mostrar_icono]] con la cara feliz.', 'Pruébalo al sol en el patio (unos minutos, sin dejar la placa al sol mucho rato).'],
        'basic.forever(function () {\n    if (input.temperature() > 30 || input.lightLevel() > 240) {\n        basic.showString("Sombra")\n    } else {\n        basic.showIcon(IconNames.Happy)\n    }\n    basic.pause(1000)\n})',
        "whenStarted\nforever {\n  if (or (('[sensors:temperature]') > 30) (('[display:lightLevel]') > 900)) {\n    scroll_text 'Sombra'\n  } else {\n    led_displayImage 'happy'\n  }\n  waitMillis 1000\n}",
        'from microbit import *\n\nwhile True:\n    if temperature() > 30 or display.read_light_level() > 240:\n        display.scroll("Sombra")\n    else:\n        display.show(Image.HAPPY)\n    sleep(1000)') +
    actividad('verano-crema', 'Recordatorio de crema solar', '15 min',
        'Un temporizador que avisa cada cierto tiempo de que toca ponerse crema y beber agua.',
        ['En [[boton]] (A), [[pausa]] de 60 000 ms (para probar; en la playa, unas 2 horas).', 'Al terminar, con [[repetir]] 5 veces, [[mostrar_leds]] una gota y un [[tono]].', 'Con B, se apaga la alarma y empieza otra vez.'],
        'input.onButtonPressed(Button.A, function () {\n    basic.showIcon(IconNames.Yes)\n    basic.pause(60000)\n    for (let index = 0; index < 5; index++) {\n        basic.showLeds(`\n            . . # . .\n            . # # # .\n            # # # # #\n            # # # # #\n            . # # # .\n            `)\n        music.play(music.tonePlayable(988, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)\n        basic.clearScreen()\n        basic.pause(300)\n    }\n})',
        "whenButtonPressed 'A'\nled_displayImage 'yes'\nwaitMillis 60000\nrepeat 5 {\n  '[display:mbDisplay]' %d\n  'play frequency' 988 250\n  '[display:mbDisplayOff]'\n  waitMillis 300\n}" % bm('00100', '01110', '11111', '11111', '01110'),
        'from microbit import *\nimport music\n\nGOTA = Image("00900:09990:99999:99999:09990")\nwhile True:\n    if button_a.was_pressed():\n        display.show(Image.YES)\n        sleep(60000)\n        for i in range(5):\n            display.show(GOTA)\n            music.pitch(988, 250)\n            display.clear()\n            sleep(300)') + construir('sol', [
        'Imprime el sol en cartulina amarilla y coloca la placa detrás: será el avisador del patio.',
        'Protege la placa del sol directo con una caja de cartón abierta por delante: el sensor de temperatura está en el procesador y se calienta.',
        'Haz un abanico de cartulina y comprueba si cambia la temperatura que mide la placa.']),
    icono='playa', kind='celebrar')

page(S, 'proximamente', 'Próximas fechas', P('Este apartado irá creciendo. Fechas que se añadirán: Día de la Paz (30 de enero), Carnaval, Día de Andalucía (28 de febrero), '
    'Día del Libro (23 de abril) y Día del Medio Ambiente (5 de junio).') +
    box('idea', 'Ideas para adelantar', ul(['<b>Día de la Paz</b>: una paloma animada y un mensaje de paz que viaja por radio de placa en placa.',
        '<b>Día del Libro</b>: un marcapáginas con temporizador de lectura de 20 minutos.',
        '<b>Medio Ambiente</b>: un medidor de ruido para el patio o un registrador de temperatura de la ventana.'])),
    icono='calendario')
