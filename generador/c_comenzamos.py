# -*- coding: utf-8 -*-
"""Comenzamos: 30 prácticas progresivas en seis bloques."""
from common import practica, P, ul, box, kbd
from iconos import icon

S = 'comenzamos'
B1, B2, B3, B4, B5, B6 = ('1 · Pantalla y botones', '2 · Sonido', '3 · Sensores de la placa', '4 · Variables y azar',
                          '5 · Bucles, tiempo y listas', '6 · Radio')
GRUPOS = {
    B1: P('Las primeras órdenes: escribir en la pantalla, dibujar con los LED y reaccionar a los botones y al logotipo. Ideal para empezar a partir de 6-7 años.'),
    B2: P('El altavoz de la micro:bit V2 permite tocar notas, melodías y efectos. Si tu placa es una V1, conecta unos auriculares o un zumbador a P0 y GND.'),
    B3: P('La placa mide la luz, la temperatura, el movimiento, la orientación y el sonido. Aprendemos a leer sensores y a tomar decisiones con <b>si… entonces</b>.'),
    B4: P('Las <b>variables</b> guardan datos que cambian (una puntuación, un número de pasos) y el <b>azar</b> hace que cada partida sea distinta.'),
    B5: P('Bucles dentro de bucles, coordenadas, tiempo y listas: las herramientas de los programas más largos. Pensado para 5.º-6.º y ESO.'),
    B6: P('Las micro:bits se comunican por radio. Para estas prácticas hacen falta <b>al menos dos placas</b> con el mismo programa y el mismo grupo de radio.') +
        box('ojo', 'El mismo editor en las dos placas', P('MakeCode, MicroBlocks y Python preparan los mensajes de radio de forma distinta. '
            'Para que dos placas se entiendan, prográmalas con el mismo editor.')),
}

def bm(*rows):
    """Imagen de 5 × 5 para MicroBlocks: '01010' por fila -> número de 25 bits."""
    n = 0
    for r, row in enumerate(rows):
        for c, ch in enumerate(row):
            if ch == '1': n |= 1 << (r * 5 + c)
    return n

def pyimg(*rows):
    return 'Image("%s")' % ':'.join(r.replace('1', '9') for r in rows)

def mcleds(rows, ind='    '):
    return 'basic.showLeds(`\n' + ''.join(ind + '    ' + ' '.join('#' if ch == '1' else '.' for ch in r) + '\n' for r in rows) + ind + '    `)'

RADIO2 = ['Dos micro:bits (o más) con su cable o portapilas']

# =================================================================== 1 · Pantalla y botones
practica(S, '01', 'hola-microbit', '¡Hola, micro:bit!', 1, 'P1', '10 min', ['secuencia', 'pantalla'],
    'Que la placa se presente: al encenderse escribe un saludo con tu nombre y después muestra una cara sonriente.',
    ['Abre el editor y crea un proyecto nuevo.',
     'Busca [[al_iniciar]]: se ejecuta <b>una vez al encender</b> la placa.',
     'Dentro, coloca [[mostrar_texto]] y cambia el texto por tu saludo.',
     'Debajo, añade [[mostrar_icono]] y elige la cara sonriente.',
     'Pruébalo en el simulador o cárgalo en la placa. Pulsa el botón de reinicio del reverso para verlo otra vez.'],
    ['En MakeCode: %s y %s están en <b>Básico</b>. En MicroBlocks: %s (Control) y %s (Pantalla LED).' % (kbd('al iniciar'), kbd('mostrar cadena'), kbd('al empezar'), kbd('anima el texto')),
     'Escribe sin tildes ni eñes: la pantalla solo tiene las letras del alfabeto inglés.',
     'El orden importa: lo que va arriba se hace primero.'],
    'basic.showString("Hola, soy Ana")\nbasic.showIcon(IconNames.Happy)',
    "whenStarted\nscroll_text 'Hola, soy Ana'\nled_displayImage 'happy'",
    'from microbit import *\n\ndisplay.scroll("Hola, soy Ana")\ndisplay.show(Image.HAPPY)',
    ['Haz que después de la cara aparezca tu edad.', 'Prueba otros iconos: corazón, casa, fantasma…', 'Haz una presentación de tres frases sobre tus aficiones.'],
    group=B1, icono='led')

practica(S, '02', 'caras-y-emociones', 'Caras y emociones', 1, 'P1', '15 min', ['eventos', 'botones'],
    'Que la placa muestre una cara contenta al pulsar A, una triste al pulsar B y una sorprendida al pulsar los dos a la vez.',
    ['Busca el evento [[boton]]: reacciona cuando se pulsa un botón.',
     'Déjalo en A y mete dentro [[mostrar_icono]] con la cara contenta.',
     'Duplica el evento (clic derecho › Duplicar), cámbialo a B y pon la cara triste.',
     'Haz un tercer [[boton]] para A+B con la cara sorprendida.',
     'Pruébalo: ¿qué pasa si pulsas muy rápido los dos botones?'],
    ['Un <b>evento</b> es un bloque que espera a que pase algo. No hace falta ponerlo dentro de «para siempre».',
     'En MakeCode el evento es %s (Entrada); en MicroBlocks, %s (Control). Los dos tienen un menú para elegir A, B o A+B.' % (kbd('al presionarse el botón A'), kbd('cuando se pulse el botón A')),
     'En Python no hay eventos: un bucle pregunta sin parar si se ha pulsado cada botón. Por eso se comprueba primero A+B.'],
    '''input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Happy)
})
input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.Surprised)
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Sad)
})''',
    "whenButtonPressed 'A'\nled_displayImage 'happy'\n---\nwhenButtonPressed 'B'\nled_displayImage 'sad'\n---\nwhenButtonPressed 'A+B'\nled_displayImage 'surprised'",
    '''from microbit import *

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.SURPRISED)
    elif button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        display.show(Image.SAD)''',
    ['Añade un cuarto gesto: al tocar el logotipo, una cara dormida.', 'Haz que cada cara vaya acompañada de un sonido.', 'Inventad en grupo un «emocionómetro» para empezar la clase.'],
    group=B1, icono='pulsador')

practica(S, '03', 'corazon-que-late', 'Corazón que late', 1, 'P1', '10 min', ['bucles', 'animación'],
    'Crear una animación que no se detiene nunca: un corazón grande y uno pequeño que se alternan como un latido.',
    ['Busca [[para_siempre]]: repite sin parar lo que tiene dentro.',
     'Dentro, pon [[mostrar_icono]] con el corazón grande y [[pausa]] de 500 ms (medio segundo).',
     'Después, otro [[mostrar_icono]] con el corazón pequeño y otra [[pausa]] de 500 ms.',
     'Prueba con otras esperas: ¿cómo late un corazón tranquilo? ¿Y después de correr?'],
    ['Las esperas se escriben en <b>milisegundos</b>: 1000 ms = 1 segundo.',
     'En MakeCode: %s y %s (Básico). En MicroBlocks: %s y %s (Control).' % (kbd('para siempre'), kbd('pausa (ms)'), kbd('por siempre'), kbd('espera 500 milisegundos')),
     'Sin la espera, el cambio es tan rápido que parece que no pasa nada.'],
    'basic.forever(function () {\n    basic.showIcon(IconNames.Heart)\n    basic.pause(500)\n    basic.showIcon(IconNames.SmallHeart)\n    basic.pause(500)\n})',
    "whenStarted\nforever {\n  led_displayImage 'heart'\n  waitMillis 500\n  led_displayImage 'small heart'\n  waitMillis 500\n}",
    'from microbit import *\n\nwhile True:\n    display.show(Image.HEART)\n    sleep(500)\n    display.show(Image.HEART_SMALL)\n    sleep(500)',
    ['Haz que el corazón lata dos veces rápido y luego descanse, como uno de verdad.', 'Anima otro objeto con dos imágenes: un rombo grande y uno pequeño, un pato y una casa…'],
    group=B1, icono='corazon')

F1 = ('01010', '01010', '00000', '10001', '01110')
F2 = ('00010', '11010', '00000', '10001', '01110')
practica(S, '04', 'mi-dibujo-de-led', 'Mi dibujo de LED', 1, 'P1', '20 min', ['píxeles', 'animación'],
    'Diseñar tus propias imágenes LED a LED y animar una cara que guiña un ojo.',
    ['Dibuja en un papel cuadriculado de 5 × 5 una cara con los dos ojos abiertos y otra guiñando un ojo.',
     'En el editor, usa [[mostrar_leds]]: haz clic en los cuadros para encender cada LED.',
     'Dentro de [[para_siempre]], muestra la cara normal, [[pausa]], la cara del guiño y otra [[pausa]] más corta.',
     'Ajusta los tiempos hasta que el guiño parezca natural.'],
    ['En MakeCode: %s (Básico). En MicroBlocks: %s, que trae una cuadrícula para hacer clic.' % (kbd('mostrar LEDs'), kbd('pantalla')),
     'En Python cada imagen es un texto: 5 filas de 5 cifras separadas por dos puntos. 0 es apagado y 9, el máximo brillo.',
     'Un guiño dura poco: prueba 2000 ms con los ojos abiertos y 300 ms con el ojo cerrado.'],
    'basic.forever(function () {\n    ' + mcleds(F1) + '\n    basic.pause(2000)\n    ' + mcleds(F2) + '\n    basic.pause(300)\n})',
    "whenStarted\nforever {\n  '[display:mbDisplay]' %d\n  waitMillis 2000\n  '[display:mbDisplay]' %d\n  waitMillis 300\n}" % (bm(*F1), bm(*F2)),
    'from microbit import *\n\nnormal = %s\nguino = %s\n\nwhile True:\n    display.show(normal)\n    sleep(2000)\n    display.show(guino)\n    sleep(300)' % (pyimg(*F1), pyimg(*F2)),
    ['Añade un tercer fotograma para que la cara saque la lengua.', 'Crea la animación de tu nombre en iniciales grandes.', 'En Python, usa brillos intermedios (por ejemplo, 4) para dar sombras.'],
    group=B1, icono='matriz')

practica(S, '05', 'el-logotipo-magico', 'El logotipo mágico', 1, 'P1', '15 min', ['eventos', 'táctil'],
    'Esconder un mensaje secreto que solo aparece al tocar el logotipo dorado de la placa (micro:bit V2).',
    ['En [[al_iniciar]], pon [[mostrar_caracter]] con un signo de interrogación.',
     'Busca el evento [[logo]].',
     'Dentro, pon [[mostrar_texto]] con tu mensaje secreto y, debajo, vuelve a mostrar la interrogación.',
     'Prueba a tocar el logotipo con un lápiz o con un guante: ¿funciona? ¿Por qué?'],
    ['En MakeCode: %s (Entrada). En MicroBlocks, el bloque %s está en la biblioteca TouchPin; úsalo dentro de %s.' % (kbd('al pulsar el logotipo'), kbd('logo touched'), kbd('cuando')),
     'El logotipo detecta la pequeña carga eléctrica del cuerpo: por eso no responde al lápiz ni al guante.'],
    'basic.showString("?")\ninput.onLogoEvent(TouchButtonEvent.Pressed, function () {\n    basic.showString("Eres genial")\n    basic.showString("?")\n})',
    "whenStarted\ndisplayCharacter '?'\n---\nwhenCondition (touchPin_logoTouched)\nscroll_text 'Eres genial'\ndisplayCharacter '?'",
    'from microbit import *\n\ndisplay.show("?")\nwhile True:\n    if pin_logo.is_touched():\n        display.scroll("Eres genial")\n        display.show("?")',
    ['Haz que cada vez muestre un mensaje distinto (lo verás en la práctica 25).', 'Pon una contraseña: el mensaje solo aparece si antes se ha pulsado el botón B.'],
    group=B1, icono='tactil')

# =================================================================== 2 · Sonido
practica(S, '06', 'timbre', 'El timbre', 1, 'P1', '15 min', ['sonido', 'eventos'],
    'Convertir la placa en un timbre: el botón A hace «ring, ring» y el botón B toca una melodía de cuatro notas.',
    ['En [[boton]] (A), pon dos [[tono]] agudos y cortos seguidos.',
     'En otro [[boton]] (B), toca con [[nota]] Do, Mi, Sol y el Do agudo.',
     'Añade [[mostrar_icono]] en cada botón para ver qué suena.',
     'Prueba otras notas o tiempos hasta que te guste.'],
    ['En MakeCode, los sonidos están en <b>Música</b>. Haz clic en la nota del bloque para elegirla en un pequeño piano.',
     'En MicroBlocks, %s y %s están en la biblioteca <b>Tonos</b>.' % (kbd('toca la frecuencia'), kbd('toca la nota')),
     'La frecuencia se mide en hercios (Hz): cuanto más alta, más agudo el sonido. 988 Hz es un Si agudo.'],
    '''input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.House)
    music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Sixteenth))
    music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.QuarterNote)
    music.play(music.stringPlayable("C E G C5 ", 240), music.PlaybackMode.UntilDone)
})''',
    "whenButtonPressed 'A'\nled_displayImage 'house'\n'play frequency' 988 100\nwaitMillis 50\n'play frequency' 988 100\n---\nwhenButtonPressed 'B'\nled_displayImage 'quarter note'\n'play tone' 'nt;c' 0 250\n'play tone' 'nt;e' 0 250\n'play tone' 'nt;g' 0 250\n'play tone' 'nt;c' 1 250",
    '''from microbit import *
import music

while True:
    if button_a.was_pressed():
        display.show(Image.HOUSE)
        music.pitch(988, 100)
        sleep(50)
        music.pitch(988, 100)
    if button_b.was_pressed():
        display.show(Image.MUSIC_CROTCHET)
        music.play(["C4:4", "E4:4", "G4:4", "C5:4"])''',
    ['Haz un timbre distinto para cada miembro de la familia.', 'Programa el principio de una canción que conozcas.'],
    group=B2, icono='altavoz')

practica(S, '07', 'piano-de-tres-teclas', 'Piano de tres teclas', 1, 'P1', '15 min', ['sonido', 'eventos'],
    'Tocar música con la placa: el botón A es Do, el B es Re y el logotipo es Mi.',
    ['Crea un evento para cada «tecla»: [[boton]] para A, otro para B y [[logo]].',
     'En cada uno, pon [[mostrar_caracter]] con la letra de la nota (C, D, E en notación inglesa) y [[nota]] durante 300 ms.',
     'Toca «Do Re Mi Do» y «Mi Re Do» para comprobarlo.',
     'Inventa una melodía de seis notas con tu compañero o compañera.'],
    ['Las notas en inglés: C = Do, D = Re, E = Mi, F = Fa, G = Sol, A = La, B = Si.',
     'Las frecuencias del Do, Re y Mi centrales son 262, 294 y 330 Hz.',
     'En MicroBlocks el logotipo se usa con %s y %s (biblioteca TouchPin).' % (kbd('cuando'), kbd('logo touched'))],
    '''input.onButtonPressed(Button.A, function () {
    basic.showString("C")
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.B, function () {
    basic.showString("D")
    music.play(music.tonePlayable(294, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showString("E")
    music.play(music.tonePlayable(330, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
})''',
    "whenButtonPressed 'A'\ndisplayCharacter 'C'\n'play tone' 'nt;c' 0 300\n---\nwhenButtonPressed 'B'\ndisplayCharacter 'D'\n'play tone' 'nt;d' 0 300\n---\nwhenCondition (touchPin_logoTouched)\ndisplayCharacter 'E'\n'play tone' 'nt;e' 0 300",
    '''from microbit import *
import music

while True:
    if button_a.was_pressed():
        display.show("C")
        music.pitch(262, 300)
    if button_b.was_pressed():
        display.show("D")
        music.pitch(294, 300)
    if pin_logo.is_touched():
        display.show("E")
        music.pitch(330, 300)''',
    ['Añade el Fa con A+B.', 'Con cables de cocodrilo, convierte P0, P1 y P2 en más teclas (lo verás en el modo experto).'],
    group=B2, icono='musica')

ARR_N = ('00100', '01110', '10101', '00100', '00100')
practica(S, '08', 'cuenta-atras', 'Cuenta atrás espacial', 1, 'P1', '15 min', ['secuencia', 'sonido'],
    'Lanzar un cohete: al pulsar A, cuenta atrás de 3 a 1 con un pitido en cada número y, al final, flecha hacia arriba y sonido de despegue.',
    ['En [[boton]] (A), pon [[mostrar_numero]] con el 3 y un [[tono]] corto.',
     'Repite con el 2 y el 1.',
     'Después, [[flecha]] hacia arriba y un [[tono]] agudo largo.',
     'Termina con [[borrar]].'],
    ['Es una <b>secuencia</b>: los bloques se ejecutan de arriba abajo, uno detrás de otro.',
     'Para la flecha: en MakeCode, %s; en MicroBlocks, dibújala con %s.' % (kbd('mostrar flecha'), kbd('pantalla')),
     'Cuando funcione, fíjate en cuántos bloques se repiten: en la práctica 21 aprenderás a acortarlo.'],
    '''input.onButtonPressed(Button.A, function () {
    basic.showNumber(3)
    music.play(music.tonePlayable(440, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    basic.showNumber(2)
    music.play(music.tonePlayable(440, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    basic.showNumber(1)
    music.play(music.tonePlayable(440, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    basic.showArrow(ArrowNames.North)
    music.play(music.tonePlayable(880, music.beat(BeatFraction.Double)), music.PlaybackMode.UntilDone)
    basic.clearScreen()
})''',
    "whenButtonPressed 'A'\ndisplayCharacter '3'\n'play frequency' 440 250\ndisplayCharacter '2'\n'play frequency' 440 250\ndisplayCharacter '1'\n'play frequency' 440 250\n'[display:mbDisplay]' %d\n'play frequency' 880 1000\n'[display:mbDisplayOff]'" % bm(*ARR_N),
    '''from microbit import *
import music

while True:
    if button_a.was_pressed():
        display.show(3)
        music.pitch(440, 250)
        display.show(2)
        music.pitch(440, 250)
        display.show(1)
        music.pitch(440, 250)
        display.show(Image.ARROW_N)
        music.pitch(880, 1000)
        display.clear()''',
    ['Haz la cuenta desde 5.', 'Al despegar, anima la flecha subiendo por la pantalla.'],
    group=B2, icono='cohete')

practica(S, '09', 'sirena', 'La sirena', 2, 'P1', '15 min', ['condicional', 'bucles', 'sonido'],
    'Hacer una sirena que suena solo mientras mantienes pulsado el botón A, con luces que parpadean.',
    ['Dentro de [[para_siempre]], pon [[si_no]].',
     'Como condición, encaja [[boton_pulsado]].',
     'En la parte «si»: [[mostrar_icono]] rombo grande y [[tono]] de 600 Hz; rombo pequeño y [[tono]] de 900 Hz.',
     'En la parte «si no»: [[borrar]].'],
    ['Aquí no usamos el evento del botón, sino un <b>sensor</b>: «¿está pulsado ahora?». Por eso va dentro de «para siempre».',
     'En MakeCode: %s (Lógica) y %s (Entrada). En MicroBlocks: %s y %s.' % (kbd('si… entonces… si no'), kbd('botón A presionado'), kbd('si'), kbd('botón A'))],
    '''basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        basic.showIcon(IconNames.Diamond)
        music.play(music.tonePlayable(600, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
        basic.showIcon(IconNames.SmallDiamond)
        music.play(music.tonePlayable(900, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    } else {
        basic.clearScreen()
    }
})''',
    "whenStarted\nforever {\n  if (buttonA) {\n    led_displayImage 'diamond'\n    'play frequency' 600 300\n    led_displayImage 'small diamond'\n    'play frequency' 900 300\n  } else {\n    '[display:mbDisplayOff]'\n  }\n}",
    '''from microbit import *
import music

while True:
    if button_a.is_pressed():
        display.show(Image.DIAMOND)
        music.pitch(600, 300)
        display.show(Image.DIAMOND_SMALL)
        music.pitch(900, 300)
    else:
        display.clear()''',
    ['Haz una sirena distinta con el botón B (policía, bomberos…).', 'Investiga: ¿por qué suenan distinto las sirenas de cada país?'],
    group=B2, icono='altavoz')

practica(S, '10', 'mascota-que-habla', 'Mascota que habla', 2, 'P1', '20 min', ['sonido', 'eventos'],
    'Crear una mascota con personalidad que pone caras y hace sonidos: contenta con A, triste con B y con la risa floja al tocar el logotipo.',
    ['Prepara tres eventos: [[boton]] A, [[boton]] B y [[logo]].',
     'En cada uno, pon [[mostrar_icono]] con una cara y un [[efecto]] que exprese esa emoción.',
     'En MakeCode y Python puedes usar los efectos de sonido de la V2; en MicroBlocks, invéntalos con notas.',
     'Al final de cada evento, vuelve a una cara neutra.'],
    ['Un sonido alegre suele <b>subir</b> (notas cada vez más agudas) y uno triste, <b>bajar</b> despacio.',
     'En MakeCode, el bloque %s tiene un menú con risa, feliz, triste, bostezo…' % kbd('reproduce… hasta que termine'),
     'En Python: <code>audio.play(Sound.HAPPY)</code>, <code>Sound.SAD</code>, <code>Sound.GIGGLE</code>…'],
    '''basic.showIcon(IconNames.Meh)
input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Happy)
    music.play(music.builtinPlayableSoundEffect(soundExpression.happy), music.PlaybackMode.UntilDone)
    basic.showIcon(IconNames.Meh)
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Sad)
    music.play(music.builtinPlayableSoundEffect(soundExpression.sad), music.PlaybackMode.UntilDone)
    basic.showIcon(IconNames.Meh)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showIcon(IconNames.Silly)
    music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.UntilDone)
    basic.showIcon(IconNames.Meh)
})''',
    "whenStarted\nled_displayImage 'meh'\n---\nwhenButtonPressed 'A'\nled_displayImage 'happy'\n'play tone' 'nt;c' 1 120\n'play tone' 'nt;e' 1 120\n'play tone' 'nt;g' 1 240\nled_displayImage 'meh'\n---\nwhenButtonPressed 'B'\nled_displayImage 'sad'\n'play tone' 'nt;g' 0 400\n'play tone' 'nt;e' 0 400\n'play tone' 'nt;c' 0 700\nled_displayImage 'meh'\n---\nwhenCondition (touchPin_logoTouched)\nled_displayImage 'silly'\nrepeat 4 {\n  'play tone' 'nt;a' 1 80\n  'play tone' 'nt;f' 1 80\n}\nled_displayImage 'meh'",
    '''from microbit import *

display.show(Image.MEH)
while True:
    if button_a.was_pressed():
        display.show(Image.HAPPY)
        audio.play(Sound.HAPPY)
        display.show(Image.MEH)
    if button_b.was_pressed():
        display.show(Image.SAD)
        audio.play(Sound.SAD)
        display.show(Image.MEH)
    if pin_logo.is_touched():
        display.show(Image.SILLY)
        audio.play(Sound.GIGGLE)
        display.show(Image.MEH)''',
    ['Añade una reacción al agitar la placa (mareo).', 'Construye un cuerpo de cartulina para tu mascota con la placa como cara.'],
    group=B2, icono='robot', explica='En MicroBlocks no hay efectos de sonido ya hechos, así que los construimos con notas: es una buena ocasión para hablar de cómo la música transmite emociones.')

# =================================================================== 3 · Sensores
ALL = ('11111',) * 5
practica(S, '11', 'luz-de-noche', 'Luz de noche', 2, 'P1', '15 min', ['sensor de luz', 'condicional'],
    'Construir una luz de noche automática: cuando está oscuro se encienden todos los LED y, cuando hay luz, se apagan.',
    ['Primero <b>explora</b>: muestra [[luz]] con [[mostrar_numero]] (en MicroBlocks, con [[di]]) y anota el valor con la luz encendida y tapando la placa.',
     'Elige un número intermedio: será el <b>umbral</b>.',
     'Dentro de [[para_siempre]], usa [[si_no]] con la condición [[luz]] [[menor]] umbral: enciende todos los LED con [[mostrar_leds]]; si no, [[borrar]].',
     'Pruébalo apagando la luz de clase o metiendo la placa en una caja.'],
    ['En MakeCode el nivel de luz va de 0 a 255; en MicroBlocks, de 0 a 1023. Por eso el umbral cambia según el editor.',
     'En MicroBlocks, usa el bloque %s para ver el valor en directo mientras tapas la placa.' % kbd('di'),
     'Los LED de la pantalla son a la vez el sensor de luz. Si parpadea, sube o baja un poco el umbral.'],
    '''basic.forever(function () {
    if (input.lightLevel() < 30) {
        ''' + mcleds(ALL, '        ') + '''
    } else {
        basic.clearScreen()
    }
})''',
    "whenStarted\nforever {\n  if (('[display:lightLevel]') < 100) {\n    '[display:mbDisplay]' %d\n  } else {\n    '[display:mbDisplayOff]'\n  }\n  waitMillis 200\n}" % bm(*ALL),
    'from microbit import *\n\nencendido = %s\n\nwhile True:\n    if display.read_light_level() < 30:\n        display.show(encendido)\n    else:\n        display.clear()\n    sleep(200)' % pyimg(*ALL),
    ['Haz que con poca luz se encienda solo la mitad de la pantalla y con oscuridad total, toda.', 'Pon la placa en la ventana: ¿a qué hora «se hace de noche» para ella?'],
    group=B3, icono='sol')

practica(S, '12', 'termometro', 'Termómetro de bolsillo', 1, 'P1', '15 min', ['sensor de temperatura', 'eventos'],
    'Medir la temperatura del aula al pulsar A y mostrarla con la letra C de grados Celsius.',
    ['En [[boton]] (A), pon [[mostrar_numero]] con [[temperatura]] dentro.',
     'Después, [[mostrar_caracter]] con la letra C.',
     'Compara la medida con un termómetro de verdad. ¿Coincide?',
     'Calienta la placa con las manos un minuto y vuelve a medir.'],
    ['El sensor está dentro del procesador, así que mide la temperatura del chip: si la placa lleva mucho rato funcionando, puede marcar algún grado más que el aire.',
     'En MakeCode: %s (Entrada). En MicroBlocks: %s (Sensores básicos).' % (kbd('temperatura (°C)'), kbd('temperatura (°C)'))],
    'input.onButtonPressed(Button.A, function () {\n    basic.showNumber(input.temperature())\n    basic.showString("C")\n})',
    "whenButtonPressed 'A'\nscroll_text ('[sensors:temperature]')\ndisplayCharacter 'C'",
    'from microbit import *\n\nwhile True:\n    if button_a.was_pressed():\n        display.scroll(temperature())\n        display.show("C")',
    ['Si tu placa marca 2 grados de más, réstale 2 antes de mostrarlo (calibrar).', 'Mide la temperatura en distintos rincones del centro y haz un mapa.'],
    group=B3, icono='termometro')

practica(S, '13', 'dado-electronico', 'Dado electrónico', 1, 'P1', '15 min', ['azar', 'acelerómetro'],
    'Fabricar un dado: al agitar la placa aparece un número al azar del 1 al 6.',
    ['Busca el evento [[agitar]].',
     'Dentro, pon [[mostrar_numero]] con [[azar]] y cambia los números a 1 y 6.',
     'Lanza el dado 30 veces y apunta cuántas veces sale cada número. ¿Sale todo igual de a menudo?'],
    ['En MakeCode: %s (Entrada) y %s (Matemática).' % (kbd('si agitar'), kbd('escoger al azar de 1 a 6')),
     'MicroBlocks no tiene un evento de agitar: usa %s con la condición %s mayor que 200. En reposo la aceleración vale unos 100.' % (kbd('cuando'), kbd('aceleración'))],
    'input.onGesture(Gesture.Shake, function () {\n    basic.showNumber(randint(1, 6))\n})',
    "whenCondition (('[sensors:acceleration]') > 200)\nscroll_text (random 1 6)\nwaitMillis 500",
    'from microbit import *\nimport random\n\nwhile True:\n    if accelerometer.was_gesture("shake"):\n        display.show(random.randint(1, 6))',
    ['Haz un dado de 10 caras o de 20.', 'Muestra los puntos del dado como en uno de verdad, con imágenes.', 'Añade un sonido de «dado rodando» antes del número.'],
    group=B3, icono='dado')

ARR_W = ('00100', '01000', '11111', '01000', '00100')
ARR_E = ('00100', '00010', '11111', '00010', '00100')
practica(S, '14', 'nivel-de-burbuja', 'Nivel de burbuja', 2, 'P2', '20 min', ['acelerómetro', 'condicionales'],
    'Construir un nivel como el de los albañiles: una flecha señala hacia qué lado está inclinada la placa y una marca de verificación indica que está recta.',
    ['Explora: muestra [[inclinacion]] e inclina la placa a izquierda y derecha. Anota los valores.',
     'En [[para_siempre]], pon [[si_no]]: si x [[menor]] el umbral negativo, [[flecha]] a la izquierda.',
     'Pulsa el + para añadir «si no, si»: si x [[mayor]] el umbral positivo, [[flecha]] a la derecha.',
     'En el último «si no», [[mostrar_icono]] con la marca de verificación.',
     'Comprueba con el nivel si la mesa de clase está recta.'],
    ['Usa un <b>si… si no, si… si no</b> con tres caminos. En MakeCode, pulsa el + del bloque «si» para añadir ramas.',
     'En MakeCode la aceleración va en mili-g (1 g ≈ 1024). En MicroBlocks, %s va de −200 a 200 (100 = 1 g).' % kbd('inclinación x'),
     'Un umbral pequeño hace el nivel muy sensible; uno grande, menos.'],
    '''basic.forever(function () {
    if (input.acceleration(Dimension.X) < -150) {
        basic.showArrow(ArrowNames.West)
    } else if (input.acceleration(Dimension.X) > 150) {
        basic.showArrow(ArrowNames.East)
    } else {
        basic.showIcon(IconNames.Yes)
    }
})''',
    "whenStarted\nforever {\n  if (('[sensors:tiltX]') < -15) {\n    '[display:mbDisplay]' %d\n  } (('[sensors:tiltX]') > 15) {\n    '[display:mbDisplay]' %d\n  } else {\n    led_displayImage 'yes'\n  }\n}" % (bm(*ARR_W), bm(*ARR_E)),
    '''from microbit import *

while True:
    x = accelerometer.get_x()
    if x < -150:
        display.show(Image.ARROW_W)
    elif x > 150:
        display.show(Image.ARROW_E)
    else:
        display.show(Image.YES)''',
    ['Haz lo mismo con el eje y (adelante y atrás).', 'Añade un pitido cuando quede perfectamente recta.'],
    group=B3, icono='acelerometro')

practica(S, '15', 'semaforo-del-ruido', 'Semáforo del ruido', 2, 'P2', '20 min', ['micrófono', 'condicionales'],
    'Avisar del nivel de ruido de la clase (micro:bit V2): cara contenta si hay calma, cara regular si sube el ruido y cara enfadada con pitido si hay demasiado.',
    ['Explora: muestra [[sonido_nivel]] mientras habláis bajo, normal y alto. Anota los valores.',
     'Elige dos umbrales: uno para «ruido medio» y otro para «demasiado ruido».',
     'En [[para_siempre]], con [[si_no]] y sus ramas «si no, si», muestra con [[mostrar_icono]] la cara que corresponda.',
     'En la rama de demasiado ruido, añade un [[tono]] corto.',
     'Déjalo funcionando una sesión y comentad si los umbrales son justos.'],
    ['Empieza comprobando el valor <b>más alto</b> (demasiado ruido): si empiezas por el más bajo, nunca llegarás a los demás.',
     'En MakeCode y Python el nivel de sonido va de 0 a 255. En MicroBlocks, %s (biblioteca Micrófono) da otra escala: explórala con %s.' % (kbd('volumen'), kbd('di'))],
    '''basic.forever(function () {
    if (input.soundLevel() > 120) {
        basic.showIcon(IconNames.Angry)
        music.play(music.tonePlayable(880, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    } else if (input.soundLevel() > 50) {
        basic.showIcon(IconNames.Meh)
    } else {
        basic.showIcon(IconNames.Happy)
    }
})''',
    "whenStarted\nforever {\n  if ((loudness) > 150) {\n    led_displayImage 'angry'\n    'play frequency' 880 150\n  } ((loudness) > 60) {\n    led_displayImage 'meh'\n  } else {\n    led_displayImage 'happy'\n  }\n  waitMillis 100\n}",
    '''from microbit import *
import music

while True:
    nivel = microphone.sound_level()
    if nivel > 120:
        display.show(Image.ANGRY)
        music.pitch(880, 150)
    elif nivel > 50:
        display.show(Image.MEH)
    else:
        display.show(Image.HAPPY)
    sleep(100)''',
    ['Cuenta cuántas veces se ha superado el umbral alto durante la clase.', 'Usa un gráfico de barras en lugar de caras (práctica 22).'],
    group=B3, icono='microfono')

# =================================================================== 4 · Variables y azar
practica(S, '16', 'contador', 'Contador de personas', 2, 'P2', '20 min', ['variables', 'eventos'],
    'Contar cuántas personas entran en clase: A suma uno, B resta uno y A+B pone el contador a cero.',
    ['Pulsa [[crear_variable]] y llámala <i>contador</i>. En [[al_iniciar]], pon [[fijar]] contador a 0.',
     'En [[boton]] (A), pon [[cambiar]] y después [[mostrar_numero]] con la variable <i>contador</i>.',
     'En [[boton]] (B), [[cambiar]] con −1 y muéstrala.',
     'En [[boton]] (A+B), [[fijar]] contador a 0 y muéstrala.'],
    ['Una variable es como una caja con nombre donde guardamos un número que puede cambiar.',
     'En MakeCode: <b>Variables</b> › Crear una variable; luego %s y %s. En MicroBlocks: %s, %s y %s.' % (kbd('fijar'), kbd('cambiar… por'), kbd('Añadir una variable'), kbd('asigna a'), kbd('aumenta')),
     'Para restar, aumenta en −1.'],
    '''let contador = 0
basic.showNumber(contador)
input.onButtonPressed(Button.A, function () {
    contador += 1
    basic.showNumber(contador)
})
input.onButtonPressed(Button.B, function () {
    contador += -1
    basic.showNumber(contador)
})
input.onButtonPressed(Button.AB, function () {
    contador = 0
    basic.showNumber(contador)
})''',
    "whenStarted\ncontador = 0\nscroll_text contador\n---\nwhenButtonPressed 'A'\ncontador += 1\nscroll_text contador\n---\nwhenButtonPressed 'B'\ncontador += -1\nscroll_text contador\n---\nwhenButtonPressed 'A+B'\ncontador = 0\nscroll_text contador",
    '''from microbit import *

contador = 0
display.scroll(contador)
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        contador = 0
        display.scroll(contador)
    elif button_a.was_pressed():
        contador += 1
        display.scroll(contador)
    elif button_b.was_pressed():
        contador -= 1
        display.scroll(contador)''',
    ['Haz que no pueda bajar de cero.', 'Avisa con un sonido cuando el aforo llegue a 25.'],
    group=B4, icono='pulsador')

practica(S, '17', 'podometro', 'Podómetro', 2, 'P2', '25 min', ['variables', 'acelerómetro'],
    'Contar los pasos que das: cada sacudida suma un paso y el botón A muestra el total.',
    ['Crea la variable <i>pasos</i> con [[crear_variable]] y, en [[al_iniciar]], [[fijar]] pasos a 0.',
     'En [[agitar]], [[cambiar]] pasos por 1 y enciende un instante el LED central con [[graficar]] y [[ocultar]].',
     'En [[boton]] (A), [[mostrar_numero]] con <i>pasos</i>.',
     'Sujeta la placa al tobillo o a un bolsillo con una goma y da 20 pasos. ¿Cuenta bien?'],
    ['En MicroBlocks, espera a que la aceleración pase de 150 y luego a que baje de 120: así cada paso cuenta una sola vez.',
     'Si cuenta de más o de menos, cambia los umbrales: esto se llama <b>calibrar</b>.'],
    '''let pasos = 0
input.onGesture(Gesture.Shake, function () {
    pasos += 1
    led.plot(2, 2)
    basic.pause(100)
    led.unplot(2, 2)
})
input.onButtonPressed(Button.A, function () {
    basic.showNumber(pasos)
})''',
    "whenStarted\npasos = 0\nforever {\n  waitUntil (('[sensors:acceleration]') > 150)\n  pasos += 1\n  '[display:mbPlot]' 3 3\n  waitUntil (('[sensors:acceleration]') < 120)\n  '[display:mbUnplot]' 3 3\n}\n---\nwhenButtonPressed 'A'\nscroll_text pasos",
    '''from microbit import *

pasos = 0
while True:
    if accelerometer.was_gesture("shake"):
        pasos += 1
        display.set_pixel(2, 2, 9)
        sleep(100)
        display.set_pixel(2, 2, 0)
    if button_a.was_pressed():
        display.scroll(pasos)''',
    ['Calcula los metros recorridos multiplicando los pasos por la longitud de tu paso.', 'Marca un objetivo diario y celebra con un icono al llegar.'],
    group=B4, icono='acelerometro')

practica(S, '18', 'cronometro', 'Cronómetro', 2, 'P2', '20 min', ['tiempo', 'variables'],
    'Medir cuánto tardas en hacer algo: A pone el cronómetro en marcha y B muestra los segundos que han pasado.',
    ['En [[boton]] (A), guarda el momento de salida con [[reiniciar_tiempo]] y [[mostrar_icono]].',
     'En [[boton]] (B), calcula el tiempo transcurrido con [[tiempo]], [[dividir]] entre 1000 para pasarlo a segundos y [[mostrar_numero]].',
     'Mide cuánto tardas en decir el abecedario o en dar una vuelta al patio.'],
    ['La placa cuenta los milisegundos desde que se encendió. Restando dos momentos sabemos cuánto tiempo ha pasado.',
     'En MakeCode: %s (Entrada › más). En MicroBlocks hay un %s que se reinicia con %s.' % (kbd('tiempo de ejecución (ms)'), kbd('cronómetro'), kbd('reinicia cronómetro'))],
    '''let inicio = 0
input.onButtonPressed(Button.A, function () {
    inicio = input.runningTime()
    basic.showIcon(IconNames.Yes)
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(Math.round((input.runningTime() - inicio) / 1000))
})''',
    "whenButtonPressed 'A'\nresetTimer\nled_displayImage 'yes'\n---\nwhenButtonPressed 'B'\nscroll_text ((timer) / 1000)",
    '''from microbit import *

inicio = 0
while True:
    if button_a.was_pressed():
        inicio = running_time()
        display.show(Image.YES)
    if button_b.was_pressed():
        display.scroll((running_time() - inicio) // 1000)''',
    ['Muestra también las décimas de segundo.', 'Haz un temporizador al revés: cuenta atrás de 30 segundos y suena una alarma.'],
    group=B4, icono='reloj')

practica(S, '19', 'piedra-papel-tijera', 'Piedra, papel o tijera', 2, 'P2', '20 min', ['azar', 'variables', 'condicionales'],
    'Jugar a piedra, papel o tijera contra un compañero o compañera: al agitar, la placa elige una de las tres al azar.',
    ['En [[agitar]], [[fijar]] la variable <i>mano</i> a [[azar]] del 0 al 2.',
     'Con [[si_no]] y [[igual]]: si mano es 0, [[mostrar_icono]] cuadrado pequeño (piedra).',
     'Si es 1, el papel (cuadrado grande).',
     'Si es 2, la tijera.',
     'Jugad al mejor de cinco partidas.'],
    ['Necesitas guardar el número en una variable: si pidieras un número al azar en cada «si», ¡cada uno sería distinto!',
     'En MicroBlocks el agitado se detecta con la aceleración, como en el dado.'],
    '''input.onGesture(Gesture.Shake, function () {
    let mano = randint(0, 2)
    if (mano == 0) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (mano == 1) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
})''',
    "whenCondition (('[sensors:acceleration]') > 200)\nmano = (random 0 2)\nif (mano == 0) {\n  led_displayImage 'small square'\n} (mano == 1) {\n  led_displayImage 'square'\n} else {\n  led_displayImage 'scissors'\n}\nwaitMillis 500",
    '''from microbit import *
import random

while True:
    if accelerometer.was_gesture("shake"):
        mano = random.randint(0, 2)
        if mano == 0:
            display.show(Image.SQUARE_SMALL)
        elif mano == 1:
            display.show(Image.SQUARE)
        else:
            display.show(Image.SCISSORS)''',
    ['Añade lagarto y Spock (cinco opciones).', 'Lleva la cuenta de tus victorias con el botón A.'],
    group=B4, icono='dado')

ARR_S = ('00100', '00100', '10101', '01110', '00100')
practica(S, '20', 'adivina-el-numero', 'Adivina el número', 3, 'P2', '30 min', ['variables', 'azar', 'condicionales'],
    'La placa piensa un número del 1 al 9. Con A eliges tu respuesta y con B la compruebas: la placa te dice si es más alto, más bajo o si has acertado.',
    ['En [[al_iniciar]], [[fijar]] <i>secreto</i> a [[azar]] del 1 al 9 y <i>respuesta</i> a 1. Muestra la respuesta.',
     'En [[boton]] (A), [[cambiar]] respuesta por 1; con [[si]] respuesta [[mayor]] 9, vuelve a 1. Muéstrala.',
     'En [[boton]] (B), usa [[si_no]]: si respuesta [[igual]] secreto, muestra el sí, suena una [[melodia]] y se elige otro secreto.',
     'Si no, si la respuesta es menor, muestra una flecha hacia arriba («más»); si es mayor, hacia abajo («menos»).'],
    ['Necesitas dos variables: <i>secreto</i> y <i>respuesta</i>.',
     'Para que vuelva a 1: «si respuesta > 9, fijar respuesta a 1».',
     '¿Cuál es la mejor estrategia para acertar en pocos intentos? Empezar por el 5.'],
    '''let secreto = randint(1, 9)
let respuesta = 1
basic.showNumber(respuesta)
input.onButtonPressed(Button.A, function () {
    respuesta += 1
    if (respuesta > 9) {
        respuesta = 1
    }
    basic.showNumber(respuesta)
})
input.onButtonPressed(Button.B, function () {
    if (respuesta == secreto) {
        basic.showIcon(IconNames.Yes)
        music.play(music.builtInPlayableMelody(Melodies.PowerUp), music.PlaybackMode.UntilDone)
        secreto = randint(1, 9)
    } else if (respuesta < secreto) {
        basic.showArrow(ArrowNames.North)
    } else {
        basic.showArrow(ArrowNames.South)
    }
})''',
    "whenStarted\nsecreto = (random 1 9)\nrespuesta = 1\nscroll_text respuesta\n---\nwhenButtonPressed 'A'\nrespuesta += 1\nif (respuesta > 9) {\n  respuesta = 1\n}\nscroll_text respuesta\n---\nwhenButtonPressed 'B'\nif (respuesta == secreto) {\n  led_displayImage 'yes'\n  'play tone' 'nt;c' 1 150\n  'play tone' 'nt;g' 1 300\n  secreto = (random 1 9)\n} (respuesta < secreto) {\n  '[display:mbDisplay]' %d\n} else {\n  '[display:mbDisplay]' %d\n}" % (bm(*ARR_N), bm(*ARR_S)),
    '''from microbit import *
import random
import music

secreto = random.randint(1, 9)
respuesta = 1
display.show(respuesta)
while True:
    if button_a.was_pressed():
        respuesta += 1
        if respuesta > 9:
            respuesta = 1
        display.show(respuesta)
    if button_b.was_pressed():
        if respuesta == secreto:
            display.show(Image.YES)
            music.play(music.POWER_UP)
            secreto = random.randint(1, 9)
        elif respuesta < secreto:
            display.show(Image.ARROW_N)
        else:
            display.show(Image.ARROW_S)''',
    ['Cuenta los intentos y muéstralos al acertar.', 'Amplía a números del 1 al 50.'],
    group=B4, icono='lupa')

# =================================================================== 5 · Bucles, tiempo y listas
practica(S, '21', 'barrido-de-leds', 'Barrido de LED', 2, 'P2', '20 min', ['bucles anidados', 'coordenadas'],
    'Encender los 25 LED uno a uno, fila a fila, como una impresora, usando un bucle dentro de otro.',
    ['Recuerda las <b>coordenadas</b>: x es la columna y y es la fila. En MakeCode y Python van de 0 a 4; en MicroBlocks, de 1 a 5.',
     'Pon [[para_indice]] para recorrer las filas (y).',
     'Dentro, otro [[para_indice]] para las columnas (x) con [[graficar]] y una [[pausa]] corta.',
     'Al terminar, [[borrar]]. Todo ello dentro de [[para_siempre]].'],
    ['En MakeCode: %s (Bucles) y %s (LED).' % (kbd('para índice de 0 a 4'), kbd('graficar x y')),
     'En MicroBlocks: %s recorre 1, 2, 3, 4 y 5. Usa %s.' % (kbd('por cada i en 5'), kbd('enciende x y')),
     'Si intercambias los bucles, el barrido se hace por columnas.'],
    '''basic.forever(function () {
    for (let y = 0; y <= 4; y++) {
        for (let x = 0; x <= 4; x++) {
            led.plot(x, y)
            basic.pause(50)
        }
    }
    basic.clearScreen()
})''',
    "whenStarted\nforever {\n  for y 5 {\n    for x 5 {\n      '[display:mbPlot]' x y\n      waitMillis 50\n    }\n  }\n  '[display:mbDisplayOff]'\n}",
    '''from microbit import *

while True:
    for y in range(5):
        for x in range(5):
            display.set_pixel(x, y, 9)
            sleep(50)
    display.clear()''',
    ['Haz que apague los LED en orden inverso.', 'Reescribe la cuenta atrás de la práctica 8 con un bucle.', 'Haz una espiral (reto difícil).'],
    group=B5, icono='matriz')

practica(S, '22', 'grafico-de-luz', 'Gráfico de luz', 2, 'P2', '20 min', ['sensores', 'escalar valores'],
    'Dibujar en la pantalla una barra que sube y baja con la luz: más luz, más filas encendidas.',
    ['En MakeCode, dentro de [[para_siempre]] usa [[barras]] con [[luz]] y su máximo, 255.',
     'En MicroBlocks y Python, convierte el nivel de luz a un número de filas del 0 al 5 (<b>reescalar</b>).',
     '[[borrar]] y enciende con [[graficar]] tantas filas como indique ese número, empezando por abajo.',
     'Prueba con una linterna y tapando la placa.'],
    ['Reescalar es pasar un valor de un rango a otro: de 0-1023 a 0-5, por ejemplo.',
     'La fila de abajo es la y = 5 en MicroBlocks (y = 4 en Python). Por eso dibujamos la fila 6 − i.'],
    'basic.forever(function () {\n    led.plotBarGraph(input.lightLevel(), 255)\n})',
    "whenStarted\nforever {\n  filas = ('[misc:rescale]' ('[display:lightLevel]') 0 1023 0 5)\n  '[display:mbDisplayOff]'\n  for i filas {\n    for x 5 {\n      '[display:mbPlot]' x (6 - i)\n    }\n  }\n  waitMillis 200\n}",
    '''from microbit import *

while True:
    filas = display.read_light_level() * 6 // 256
    display.clear()
    for i in range(filas):
        for x in range(5):
            display.set_pixel(x, 4 - i, 9)
    sleep(200)''',
    ['Haz lo mismo con la temperatura o con el nivel de sonido.', 'Envía los datos al ordenador y dibuja una gráfica (MakeCode: Serial; Python: print).'],
    group=B5, icono='sol')

practica(S, '23', 'brujula', 'Brújula', 3, 'ESO', '25 min', ['sensores', 'condicionales'],
    'Construir una brújula que muestra N, E, S u O según hacia dónde apunte la parte superior de la placa.',
    ['Lee [[brujula]]: un ángulo de 0 a 359 grados (0 = norte) y guárdalo con [[fijar]].',
     'Con [[si_no]]: si el ángulo [[menor]] 45 [[o]] mayor o igual que 315, [[mostrar_caracter]] N.',
     'Si no, si es menor que 135, muestra E; si es menor que 225, S; si no, O.',
     'La primera vez la placa pedirá <b>calibrar</b>: inclínala en todas direcciones hasta llenar la pantalla.'],
    ['Haz el dibujo de una rosa de los vientos y marca los grados de cada sector.',
     'Aleja la placa de imanes, altavoces y objetos de hierro: alteran la medida.',
     'MicroBlocks no tiene un bloque de rumbo para la micro:bit, así que esta práctica se hace con MakeCode o Python.'],
    '''basic.forever(function () {
    let grados = input.compassHeading()
    if (grados < 45 || grados >= 315) {
        basic.showString("N")
    } else if (grados < 135) {
        basic.showString("E")
    } else if (grados < 225) {
        basic.showString("S")
    } else {
        basic.showString("O")
    }
})''',
    None,
    '''from microbit import *

while True:
    grados = compass.heading()
    if grados < 45 or grados >= 315:
        display.show("N")
    elif grados < 135:
        display.show("E")
    elif grados < 225:
        display.show("S")
    else:
        display.show("O")''',
    ['Añade los puntos intermedios (NE, SE, SO, NO) con flechas.', 'Haz un juego de orientación en el patio: buscar un objeto siguiendo rumbos.'],
    group=B5, icono='brujula')

practica(S, '24', 'reflejos-de-rayo', 'Reflejos de rayo', 3, 'P2', '25 min', ['tiempo', 'azar', 'esperas'],
    'Medir tus reflejos: pulsa B, espera a que aparezca la diana en un momento al azar y pulsa A lo más rápido que puedas.',
    ['En [[boton]] (B), [[borrar]] y haz una [[pausa]] de [[azar]] entre 1000 y 4000 ms.',
     '[[mostrar_icono]] con la diana y guarda el momento con [[reiniciar_tiempo]].',
     'Espera a que se pulse A: [[esperar_hasta]] [[boton_pulsado]].',
     'Calcula con [[tiempo]] los milisegundos que has tardado y [[mostrar_numero]].',
     'Haz cinco intentos y calcula tu media.'],
    ['El tiempo al azar evita que el jugador se anticipe.',
     'En MakeCode, un %s vacío espera a que se pulse A.' % kbd('mientras no botón A presionado'),
     'En MicroBlocks: %s y %s.' % (kbd('espera hasta que'), kbd('cronómetro'))],
    '''input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    basic.pause(randint(1000, 4000))
    basic.showIcon(IconNames.Target)
    let salida = input.runningTime()
    while (!(input.buttonIsPressed(Button.A))) {
        basic.pause(1)
    }
    basic.showNumber(input.runningTime() - salida)
})''',
    "whenButtonPressed 'B'\n'[display:mbDisplayOff]'\nwaitMillis (random 1000 4000)\nled_displayImage 'target'\nresetTimer\nwaitUntil (buttonA)\nscroll_text (timer)",
    '''from microbit import *
import random

while True:
    if button_b.was_pressed():
        display.clear()
        sleep(random.randint(1000, 4000))
        display.show(Image.TARGET)
        salida = running_time()
        while not button_a.is_pressed():
            sleep(1)
        display.scroll(running_time() - salida)''',
    ['Detecta a los tramposos: si se pulsa A antes de la diana, muestra una calavera.', 'Hazlo para dos jugadores: A contra B, gana el más rápido.'],
    group=B5, icono='rayo')

practica(S, '25', 'frases-de-animo', 'Frases de ánimo', 2, 'P2', '20 min', ['listas', 'azar'],
    'Guardar varias frases en una <b>lista</b> y, al pulsar A, mostrar una elegida al azar.',
    ['En [[al_iniciar]], [[fijar]] <i>frases</i> a una [[lista]] con cuatro o cinco frases cortas de ánimo.',
     'En [[boton]] (A), [[mostrar_texto]] con el [[elemento]] de la posición [[azar]].',
     'Piensa: si la lista tiene 5 frases, ¿qué números de posición son válidos?'],
    ['En MakeCode y Python la primera posición de la lista es la 0; en MicroBlocks, la 1.',
     'En MakeCode las listas están en <b>Avanzado › Arreglos</b>; en MicroBlocks, en <b>Datos</b>.',
     'Recuerda: sin tildes ni eñes en la pantalla.'],
    '''let frases = ["Tu puedes", "Sigue asi", "Genial", "Paso a paso", "Animo"]
input.onButtonPressed(Button.A, function () {
    basic.showString(frases[randint(0, frases.length - 1)])
})''',
    "whenStarted\nfrases = ('[data:makeList]' 'Tu puedes' 'Sigue asi' 'Genial' 'Paso a paso' 'Animo')\n---\nwhenButtonPressed 'A'\nscroll_text (at (random 1 (size frases)) frases)",
    '''from microbit import *
import random

frases = ["Tu puedes", "Sigue asi", "Genial", "Paso a paso", "Animo"]
while True:
    if button_a.was_pressed():
        display.scroll(random.choice(frases))''',
    ['Haz una «bola mágica» que responda a preguntas de sí o no.', 'Haz un generador de retos para educación física.'],
    group=B5, icono='lista')

# =================================================================== 6 · Radio
practica(S, '26', 'hola-por-radio', 'Hola por radio', 2, 'P2', '20 min', ['radio', 'eventos'],
    'Enviar un saludo de una placa a otra: al pulsar A, todas las placas del mismo grupo muestran el mensaje.',
    ['En [[al_iniciar]], pon [[radio_grupo]] con un número del 0 al 255. Todas las placas que se comuniquen deben tener el mismo.',
     'En [[boton]] (A), [[radio_enviar_texto]] «Hola».',
     'Con [[radio_recibir_texto]], [[mostrar_texto]] con lo recibido.',
     'Carga el programa en dos placas y prueba. ¿Hasta qué distancia llega el mensaje?'],
    ['Cada pareja de la clase debe usar un grupo distinto para no mezclar mensajes.',
     'En MakeCode: %s y %s (Radio). En MicroBlocks, biblioteca Radio: %s y %s.' % (kbd('radio establecer grupo'), kbd('al recibir radio recibirCadena'), kbd('envía texto por radio'), kbd('¿mensaje de radio recibido?')),
     'Una placa no recibe sus propios mensajes.'],
    '''radio.setGroup(1)
input.onButtonPressed(Button.A, function () {
    radio.sendString("Hola")
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})''',
    "whenStarted\n'[radio:setGroup]' 1\n---\nwhenButtonPressed 'A'\n'[radio:sendString]' 'Hola'\n---\nwhenCondition ('[radio:messageReceived]')\nscroll_text ('[radio:receivedString]')",
    '''from microbit import *
import radio

radio.on()
radio.config(group=1)
while True:
    if button_a.was_pressed():
        radio.send("Hola")
    mensaje = radio.receive()
    if mensaje:
        display.scroll(mensaje)''',
    ['Con B, envía otro mensaje distinto.', 'Haz una cadena: cada placa reenvía el mensaje que recibe.'],
    group=B6, icono='antena', materiales=RADIO2)

practica(S, '27', 'emoticonos-por-radio', 'Emoticonos por radio', 2, 'P2', '25 min', ['radio', 'condicionales', 'códigos'],
    'Enviar emociones sin palabras: A manda un 1 (contento), B un 2 (triste) y el logotipo un 3 (corazón). La placa que recibe el número muestra el icono.',
    ['Acordad un <b>código</b>: 1 = contento, 2 = triste, 3 = corazón.',
     'En [[boton]] A, B y [[logo]], [[radio_enviar_numero]] con su código.',
     'Con [[radio_recibir_numero]], usa [[si_no]] y [[igual]] para mostrar el icono de cada código.',
     'Probadlo en parejas y añadid un código nuevo.'],
    ['Enviar números es más rápido que enviar textos, y así funcionan muchos protocolos reales.',
     'En Python todo se envía como texto, así que el código es "1", "2" o "3".'],
    '''radio.setGroup(2)
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(1)
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(2)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    radio.sendNumber(3)
})
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        basic.showIcon(IconNames.Happy)
    } else if (receivedNumber == 2) {
        basic.showIcon(IconNames.Sad)
    } else if (receivedNumber == 3) {
        basic.showIcon(IconNames.Heart)
    }
})''',
    "whenStarted\n'[radio:setGroup]' 2\n---\nwhenButtonPressed 'A'\n'[radio:sendInteger]' 1\n---\nwhenButtonPressed 'B'\n'[radio:sendInteger]' 2\n---\nwhenCondition (touchPin_logoTouched)\n'[radio:sendInteger]' 3\nwaitMillis 300\n---\nwhenCondition ('[radio:messageReceived]')\ncodigo = ('[radio:receivedInteger]')\nif (codigo == 1) {\n  led_displayImage 'happy'\n} (codigo == 2) {\n  led_displayImage 'sad'\n} (codigo == 3) {\n  led_displayImage 'heart'\n}",
    '''from microbit import *
import radio

radio.on()
radio.config(group=2)
while True:
    if button_a.was_pressed():
        radio.send("1")
    if button_b.was_pressed():
        radio.send("2")
    if pin_logo.is_touched():
        radio.send("3")
        sleep(300)
    codigo = radio.receive()
    if codigo == "1":
        display.show(Image.HAPPY)
    elif codigo == "2":
        display.show(Image.SAD)
    elif codigo == "3":
        display.show(Image.HEART)''',
    ['Usad la radio para votar en clase: cada placa envía su voto y una placa central los cuenta (taller «Votación por radio»).'],
    group=B6, icono='antena', materiales=RADIO2)

practica(S, '28', 'termometro-a-distancia', 'Termómetro a distancia', 2, 'ESO', '25 min', ['radio', 'sensores'],
    'Medir la temperatura en un sitio y verla en otro: una placa envía su temperatura cada dos segundos y la otra la muestra.',
    ['Este programa sirve para las dos placas: cada una envía su temperatura y muestra la que recibe.',
     'En [[para_siempre]], [[radio_enviar_numero]] con [[temperatura]] y una [[pausa]] de 2000 ms.',
     'Con [[radio_recibir_numero]], [[mostrar_numero]].',
     'Deja una placa en la ventana o en el patio y comprueba la temperatura desde clase.'],
    ['Así funcionan muchas estaciones meteorológicas: un sensor lejano y una pantalla en casa.',
     'Si una placa solo debe mostrar, quítale el envío; si solo debe medir, quítale la recepción.'],
    '''radio.setGroup(3)
basic.forever(function () {
    radio.sendNumber(input.temperature())
    basic.pause(2000)
})
radio.onReceivedNumber(function (receivedNumber) {
    basic.showNumber(receivedNumber)
})''',
    "whenStarted\n'[radio:setGroup]' 3\nforever {\n  '[radio:sendInteger]' ('[sensors:temperature]')\n  waitMillis 2000\n}\n---\nwhenCondition ('[radio:messageReceived]')\nscroll_text ('[radio:receivedInteger]')",
    '''from microbit import *
import radio

radio.on()
radio.config(group=3)
ultimo_envio = 0
while True:
    if running_time() - ultimo_envio > 2000:
        radio.send(str(temperature()))
        ultimo_envio = running_time()
    dato = radio.receive()
    if dato:
        display.scroll(dato)''',
    ['Envía también el nivel de luz y elige con A cuál ver.', 'Si la temperatura remota supera 30 °C, haz sonar una alarma en la placa receptora.'],
    group=B6, icono='termometro', materiales=RADIO2,
    explica='En Python no conviene usar sleep(2000) dentro del bucle, porque durante esa espera la placa no comprobaría los mensajes. Por eso comparamos el tiempo.')

practica(S, '29', 'busca-el-tesoro', 'Busca el tesoro', 3, 'ESO', '30 min', ['radio', 'intensidad de señal'],
    'Esconder una placa «tesoro» que emite sin parar y buscarla con otra que muestra un corazón más grande cuanto más cerca está.',
    ['Al pulsar A, la placa se convierte en tesoro: guarda <i>tesoro = verdadero</i> y muestra un rombo.',
     'Si es tesoro, envía un número cada 200 ms.',
     'Al recibir un mensaje, lee la <b>intensidad de la señal</b> (un número negativo: cuanto más cerca de 0, más cerca está).',
     'Muestra un corazón grande si la señal es mayor que −60, uno pequeño si es mayor que −75 y un punto si no.',
     'Esconde el tesoro en clase y que otro grupo lo busque.'],
    ['La intensidad de la señal va aproximadamente de −95 (muy lejos) a −40 (pegadas). Ajusta los umbrales en tu aula.',
     'Las paredes y los cuerpos debilitan la señal: forma parte del juego.',
     'En Python, <code>radio.receive_full()</code> devuelve el mensaje, la intensidad y el momento de llegada.'],
    '''let tesoro = false
radio.setGroup(4)
input.onButtonPressed(Button.A, function () {
    tesoro = true
    basic.showIcon(IconNames.Diamond)
})
basic.forever(function () {
    if (tesoro) {
        radio.sendNumber(0)
        basic.pause(200)
    }
})
radio.onReceivedNumber(function (receivedNumber) {
    let senal = radio.receivedPacket(RadioPacketProperty.SignalStrength)
    if (senal > -60) {
        basic.showIcon(IconNames.Heart)
    } else if (senal > -75) {
        basic.showIcon(IconNames.SmallHeart)
    } else {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
    }
})''',
    "whenStarted\n'[radio:setGroup]' 4\ntesoro = (booleanConstant false)\nforever {\n  if tesoro {\n    '[radio:sendInteger]' 0\n    waitMillis 200\n  }\n}\n---\nwhenButtonPressed 'A'\ntesoro = (booleanConstant true)\nled_displayImage 'diamond'\n---\nwhenCondition ('[radio:messageReceived]')\nsenal = ('[radio:signalStrength]')\nif (senal > -60) {\n  led_displayImage 'heart'\n} (senal > -75) {\n  led_displayImage 'small heart'\n} else {\n  '[display:mbDisplay]' %d\n}" % bm('00000', '00000', '00100', '00000', '00000'),
    '''from microbit import *
import radio

radio.on()
radio.config(group=4)
tesoro = False
while True:
    if button_a.was_pressed():
        tesoro = True
        display.show(Image.DIAMOND)
    if tesoro:
        radio.send("0")
        sleep(200)
    paquete = radio.receive_full()
    if paquete:
        senal = paquete[1]
        if senal > -60:
            display.show(Image.HEART)
        elif senal > -75:
            display.show(Image.HEART_SMALL)
        else:
            display.show(Image("00000:00000:00900:00000:00000"))''',
    ['Usa un gráfico de barras para mostrar la distancia con más detalle.', 'Esconde varios tesoros con grupos de radio distintos.'],
    group=B6, icono='antena', materiales=RADIO2)

DOT = ('00000', '00000', '00100', '00000', '00000')
DASH = ('00000', '00000', '11111', '00000', '00000')
practica(S, '30', 'morse-por-radio', 'Telégrafo Morse', 3, 'ESO', '35 min', ['radio', 'códigos', 'condicionales'],
    'Construir un telégrafo: A envía un punto y B una raya. La placa que recibe los muestra y los suena, para descifrar mensajes en código Morse.',
    ['En [[boton]] (A), [[radio_enviar_texto]] «.» (punto); en B, «-» (raya).',
     'Con [[radio_recibir_texto]] y [[si_no]]: si es un punto, [[mostrar_leds]] con el LED central y un [[tono]] corto.',
     'Si es una raya: muestra una línea y toca un pitido largo (el triple de largo).',
     'Después de cada señal, [[borrar]].',
     'Buscad el alfabeto Morse y enviad vuestro nombre. SOS es · · · — — — · · ·'],
    ['Comparar textos funciona igual que comparar números: «si texto recibido = "."».',
     'En Morse, la raya dura tres veces lo que el punto.'],
    '''radio.setGroup(5)
input.onButtonPressed(Button.A, function () {
    radio.sendString(".")
})
input.onButtonPressed(Button.B, function () {
    radio.sendString("-")
})
radio.onReceivedString(function (receivedString) {
    if (receivedString == ".") {
        ''' + mcleds(DOT, '        ') + '''
        music.play(music.tonePlayable(698, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    } else {
        ''' + mcleds(DASH, '        ') + '''
        music.play(music.tonePlayable(698, music.beat(BeatFraction.Breve)), music.PlaybackMode.UntilDone)
    }
    basic.clearScreen()
})''',
    "whenStarted\n'[radio:setGroup]' 5\n---\nwhenButtonPressed 'A'\n'[radio:sendString]' '.'\n---\nwhenButtonPressed 'B'\n'[radio:sendString]' '-'\n---\nwhenCondition ('[radio:messageReceived]')\nif (('[radio:receivedString]') == '.') {\n  '[display:mbDisplay]' %d\n  'play frequency' 698 200\n} else {\n  '[display:mbDisplay]' %d\n  'play frequency' 698 600\n}\n'[display:mbDisplayOff]'" % (bm(*DOT), bm(*DASH)),
    '''from microbit import *
import radio
import music

radio.on()
radio.config(group=5)
while True:
    if button_a.was_pressed():
        radio.send(".")
    if button_b.was_pressed():
        radio.send("-")
    senal = radio.receive()
    if senal == ".":
        display.show(Image("00000:00000:00900:00000:00000"))
        music.pitch(698, 200)
        display.clear()
    elif senal == "-":
        display.show(Image("00000:00000:99999:00000:00000"))
        music.pitch(698, 600)
        display.clear()''',
    ['Con el logotipo, envía «espacio» entre letras.', 'Reto final: que la placa receptora traduzca las letras más usadas (E, T, A, O, S).'],
    group=B6, icono='onda', materiales=RADIO2)
