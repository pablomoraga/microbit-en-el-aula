# -*- coding: utf-8 -*-
"""Manual básico de MicroPython para la micro:bit V2: cada apartado con una explicación corta y un ejemplo que funciona
en python.microbit.org (API comprobada en la documentación oficial de MicroPython para micro:bit)."""
from common import P, ul, box, tabla, h2, h3, py_html

def code(src):
    return '<pre class="code py"><code>%s</code></pre>' % py_html(src)

def ej(titulo, texto, src, notas=None):
    return h3(titulo) + P(texto) + code(src) + (ul(notas) if notas else '')

INDICE = ('<nav class="indice-py"><b>En esta página</b><ol>'
          + ''.join('<li><a href="#py-%d">%s</a></li>' % (i + 1, t) for i, t in enumerate([
              'Cómo es un programa', 'La pantalla', 'Variables y operaciones', 'Decisiones', 'Bucles',
              'Botones y logotipo', 'Sensores', 'Sonido', 'Números al azar', 'Listas', 'Funciones',
              'Radio', 'Pines', 'Errores y cómo leerlos', 'Tres programas completos']))
          + '</ol></nav>')

def sec(n, t):
    return '<h2 id="py-%d">%d. %s</h2>' % (n, n, t)

BODY = (
    P('Una guía de consulta rápida de <b>MicroPython</b> para la micro:bit V2. Cada apartado explica una idea y la acompaña de un ejemplo corto: '
      'cópialo en el <a href="https://python.microbit.org" target="_blank" rel="noopener">editor de Python</a>, pruébalo en el simulador y después cámbialo.') +
    INDICE +

    sec(1, 'Cómo es un programa') +
    code('''# Esto es un comentario: Python no lo ejecuta
from microbit import *

display.scroll("Hola")      # se ejecuta una vez, al empezar

while True:                 # repite para siempre
    display.show(Image.HEART)
    sleep(500)
    display.clear()
    sleep(500)''') +
    ul(['<code>from microbit import *</code> carga las instrucciones de la placa. Va siempre en la primera línea.',
        'Las instrucciones se ejecutan de arriba abajo, una detrás de otra.',
        '<code>while True:</code> es el bucle <b>para siempre</b>. Lo que va dentro lleva <b>cuatro espacios</b> delante (sangría).',
        '<code>sleep(500)</code> espera 500 milisegundos (medio segundo).',
        'Con <code>#</code> escribes comentarios: notas para personas que el programa no lee.']) +

    sec(2, 'La pantalla') +
    ej('Texto, números e iconos', '<code>scroll</code> desplaza un texto o un número; <code>show</code> muestra una imagen (o un carácter) y se queda fijo.',
       '''from microbit import *

display.scroll("Hola clase")
display.scroll(42)
display.show(Image.HAPPY)
sleep(1000)
display.show("A")''',
       ['Algunas imágenes: <code>Image.HEART</code>, <code>Image.HAPPY</code>, <code>Image.SAD</code>, <code>Image.YES</code>, <code>Image.NO</code>, '
        '<code>Image.ARROW_N</code>, <code>Image.SKULL</code>, <code>Image.MUSIC_QUAVER</code>. La lista completa está en la pestaña <b>API</b> del editor.']) +
    ej('LED a LED', 'La pantalla tiene coordenadas: <i>x</i> es la columna (0 a 4, de izquierda a derecha) e <i>y</i> la fila (0 a 4, de arriba abajo). '
       'El brillo va de 0 (apagado) a 9 (máximo).',
       '''from microbit import *

display.clear()
display.set_pixel(0, 0, 9)   # esquina de arriba a la izquierda
display.set_pixel(4, 4, 3)   # esquina de abajo a la derecha, flojito
display.set_pixel(2, 2, 9)   # el centro''') +
    ej('Tu propia imagen', 'Una imagen son cinco filas de cinco números (brillo de 0 a 9) separadas por dos puntos.',
       '''from microbit import *

barco = Image("00900:"
              "00990:"
              "00900:"
              "99999:"
              "09990")
display.show(barco)''') +

    sec(3, 'Variables y operaciones') +
    P('Una <b>variable</b> es una caja con nombre donde guardas un valor. El signo <code>=</code> significa «guarda», no «es igual».') +
    code('''from microbit import *

puntos = 0
puntos = puntos + 1      # ahora vale 1
puntos += 5              # forma corta: ahora vale 6
nombre = "Lucía"
display.scroll(nombre + " tiene " + str(puntos))''') +
    tabla(['Operación', 'Python', 'Ejemplo'], [
        ['Sumar, restar, multiplicar', '<code>+ - *</code>', '<code>3 * 4</code> → 12'],
        ['Dividir', '<code>/</code>', '<code>7 / 2</code> → 3.5'],
        ['División entera', '<code>//</code>', '<code>7 // 2</code> → 3'],
        ['Resto', '<code>%</code>', '<code>7 % 2</code> → 1 (sirve para saber si es par)'],
        ['Potencia', '<code>**</code>', '<code>2 ** 3</code> → 8'],
        ['Número a texto', '<code>str()</code>', '<code>"Tengo " + str(10)</code>'],
        ['Texto a número', '<code>int()</code>', '<code>int("25")</code> → 25'],
    ]) +
    P('Los nombres de variable no llevan espacios ni tildes y no pueden empezar por un número: <code>vidas</code>, <code>nivel_1</code>, <code>temperatura_max</code>.') +

    sec(4, 'Decisiones') +
    P('<code>if</code> ejecuta unas instrucciones solo si se cumple una condición; <code>elif</code> («si no, si…») añade más casos y <code>else</code> recoge el resto.') +
    code('''from microbit import *

while True:
    t = temperature()
    if t > 28:
        display.show(Image.SURPRISED)
    elif t < 18:
        display.show(Image.ASLEEP)
    else:
        display.show(Image.HAPPY)
    sleep(1000)''') +
    tabla(['Comparar', 'Python'], [
        ['igual', '<code>==</code> (dos iguales)'], ['distinto', '<code>!=</code>'], ['mayor, menor', '<code>&gt;</code>, <code>&lt;</code>'],
        ['mayor o igual, menor o igual', '<code>&gt;=</code>, <code>&lt;=</code>'],
        ['las dos cosas, al menos una, lo contrario', '<code>and</code>, <code>or</code>, <code>not</code>'],
    ]) +

    sec(5, 'Bucles') +
    ej('Repetir un número de veces', '<code>for i in range(5):</code> repite cinco veces; la variable <i>i</i> vale 0, 1, 2, 3 y 4.',
       '''from microbit import *

for i in range(5):
    display.set_pixel(i, 2, 9)   # enciende la fila del centro, LED a LED
    sleep(200)''') +
    ej('Repetir mientras se cumpla algo', '<code>while</code> repite mientras la condición sea verdadera. <code>break</code> sale del bucle.',
       '''from microbit import *

cuenta = 10
while cuenta > 0:
    display.scroll(cuenta)
    cuenta -= 1
display.show(Image.YES)''') +

    sec(6, 'Botones y logotipo') +
    code('''from microbit import *

while True:
    if button_a.was_pressed():
        display.show("A")
    if button_b.is_pressed():
        display.show("B")
    if pin_logo.is_touched():
        display.show(Image.HEART)
    sleep(50)''') +
    ul(['<code>was_pressed()</code> dice si el botón <b>se ha pulsado</b> desde la última vez que preguntaste: cuenta una vez por pulsación.',
        '<code>is_pressed()</code> dice si <b>está pulsado ahora</b>: sirve para acciones que duran mientras lo mantienes.',
        '<code>button_a.get_presses()</code> devuelve cuántas veces se ha pulsado y pone la cuenta a cero.',
        'Para A y B a la vez: <code>if button_a.is_pressed() and button_b.is_pressed():</code>']) +

    sec(7, 'Sensores') +
    tabla(['Sensor', 'Python', 'Qué devuelve'], [
        ['Temperatura', '<code>temperature()</code>', 'Grados (°C) del procesador: algo más que la del aula.'],
        ['Luz', '<code>display.read_light_level()</code>', 'De 0 (oscuro) a 255 (mucha luz).'],
        ['Acelerómetro', '<code>accelerometer.get_x()</code>, <code>get_y()</code>, <code>get_z()</code>', 'Inclinación en cada eje, de unos −2000 a 2000.'],
        ['Gestos', '<code>accelerometer.was_gesture("shake")</code>', 'Verdadero si se ha agitado. Otros: <code>"up"</code>, <code>"down"</code>, <code>"left"</code>, <code>"right"</code>, <code>"face up"</code>, <code>"face down"</code>, <code>"freefall"</code>.'],
        ['Brújula', '<code>compass.heading()</code>', 'Grados de 0 a 359 (0 es el norte). La primera vez pide calibrar inclinando la placa.'],
        ['Micrófono', '<code>microphone.sound_level()</code>', 'De 0 (silencio) a 255 (mucho ruido).'],
        ['Ruido fuerte', '<code>microphone.was_event(SoundEvent.LOUD)</code>', 'Verdadero si ha habido un sonido fuerte (una palmada).'],
        ['Tiempo', '<code>running_time()</code>', 'Milisegundos desde que se encendió la placa.'],
    ]) +
    code('''from microbit import *

while True:
    if accelerometer.was_gesture("shake"):
        display.show(Image.SURPRISED)
        sleep(1000)
    display.scroll(display.read_light_level())''') +

    sec(8, 'Sonido') +
    P('La V2 tiene altavoz. El módulo <code>music</code> toca notas y melodías; <code>audio</code> reproduce los sonidos expresivos.') +
    code('''from microbit import *
import music

music.play(music.BA_DING)          # melodía incluida
music.pitch(440, 500)              # nota de 440 Hz durante 500 ms
music.play(["C4:4", "E4:4", "G4:8"])   # do, mi, sol (nota + octava : duración)
audio.play(Sound.HAPPY)            # sonido expresivo de la V2''') +
    ul(['Otras melodías: <code>music.BIRTHDAY</code>, <code>music.POWER_UP</code>, <code>music.JUMP_UP</code>, <code>music.ENTERTAINER</code>.',
        'Otros sonidos: <code>Sound.GIGGLE</code>, <code>Sound.HELLO</code>, <code>Sound.SAD</code>, <code>Sound.TWINKLE</code>, <code>Sound.YAWN</code>.',
        'Para silenciar el altavoz de la placa (por ejemplo, si usas auriculares en P0): <code>speaker.off()</code>.']) +

    sec(9, 'Números al azar') +
    code('''from microbit import *
import random

while True:
    if accelerometer.was_gesture("shake"):
        display.show(random.randint(1, 6))     # dado: de 1 a 6, ambos incluidos
    if button_a.was_pressed():
        display.show(random.choice([Image.HAPPY, Image.SAD, Image.HEART]))''') +

    sec(10, 'Listas') +
    P('Una <b>lista</b> guarda varios valores en orden. El primero está en la posición 0.') +
    code('''from microbit import *

colores = ["rojo", "verde", "azul"]
display.scroll(colores[0])        # rojo
colores.append("amarillo")        # añade al final
display.scroll(len(colores))      # 4

medidas = []
for i in range(5):
    medidas.append(temperature())
    sleep(1000)
display.scroll(max(medidas))      # la más alta (min() da la más baja)''') +

    sec(11, 'Funciones') +
    P('Una <b>función</b> es un trozo de programa con nombre que puedes usar muchas veces. Se crea con <code>def</code> y puede devolver un resultado con <code>return</code>.') +
    code('''from microbit import *

def parpadear(imagen, veces):
    for i in range(veces):
        display.show(imagen)
        sleep(300)
        display.clear()
        sleep(300)

def doble(n):
    return n * 2

parpadear(Image.HEART, 3)
display.scroll(doble(21))''') +

    sec(12, 'Radio') +
    P('Las micro:bits se envían mensajes de texto por radio. Todas las que quieran hablar entre sí deben estar en el mismo <b>grupo</b> (de 0 a 255).') +
    code('''from microbit import *
import radio

radio.on()
radio.config(group=7)

while True:
    if button_a.was_pressed():
        radio.send("hola")
    mensaje = radio.receive()      # None si no ha llegado nada
    if mensaje:
        display.scroll(mensaje)''') +
    ul(['Los mensajes son texto: para enviar un número, conviértelo con <code>str(n)</code> y, al recibirlo, vuelve a número con <code>int(mensaje)</code>.',
        'Una placa no recibe sus propios mensajes.']) +

    sec(13, 'Pines') +
    tabla(['Para…', 'Python'], [
        ['Encender o apagar algo (LED, zumbador)', '<code>pin0.write_digital(1)</code> / <code>pin0.write_digital(0)</code>'],
        ['Leer si hay contacto (pulsador, interruptor)', '<code>pin1.read_digital()</code> → 0 o 1'],
        ['Leer un valor que varía (potenciómetro, sensor)', '<code>pin1.read_analog()</code> → de 0 a 1023'],
        ['Dar más o menos potencia (brillo de un LED)', '<code>pin0.write_analog(512)</code> → de 0 a 1023'],
        ['Tocar un pin con la mano', '<code>pin0.is_touched()</code>'],
        ['Activar la resistencia interna (interruptores a GND)', '<code>pin1.set_pull(pin1.PULL_UP)</code>'],
    ]) +
    code('''from microbit import *

while True:
    valor = pin1.read_analog()      # potenciómetro en P1
    pin0.write_analog(valor)        # LED en P0: más o menos brillo
    sleep(20)''') +
    box('ojo', 'Antes de conectar nada', P('Repasa la página <a href="precauciones.html">Precauciones y cuidados</a>: cada pin da muy poca corriente y los motores necesitan una placa de expansión.')) +

    sec(14, 'Errores y cómo leerlos') +
    P('Muchos errores de escritura los marca el propio editor en la línea donde están. Si el fallo aparece al ejecutarse, la pantalla de la placa '
      '(o del simulador) desplaza un mensaje con el <b>número de línea</b> y el tipo de error.') +
    tabla(['Mensaje', 'Qué suele significar'], [
        ['<code>SyntaxError</code>', 'Algo está mal escrito: faltan los dos puntos <code>:</code>, un paréntesis o unas comillas.'],
        ['<code>IndentationError</code>', 'La sangría está descolocada: revisa los espacios al principio de la línea.'],
        ['<code>NameError</code>', 'Usas un nombre que no existe: una variable sin crear, una errata (<code>Display</code> en vez de <code>display</code>) o un módulo sin importar.'],
        ['<code>TypeError</code>', 'Mezclas tipos que no encajan, como sumar texto y número sin <code>str()</code>.'],
        ['<code>ValueError</code>', 'El valor no sirve, como <code>int("hola")</code> o un brillo de 12.'],
    ]) +
    box('idea', 'Truco para depurar', P('Muestra en la pantalla el valor de una variable en el punto que falla (<code>display.scroll(x)</code>) o usa '
        '<code>print(x)</code> y mira la consola serie del editor, debajo del simulador. Así ves qué está pasando de verdad.')) +

    sec(15, 'Tres programas completos') +
    ej('Dado con sonido', 'Agita la placa: suena, muestra un número del 1 al 6 y cuenta cuántas tiradas llevas.',
       '''from microbit import *
import random
import music

tiradas = 0
while True:
    if accelerometer.was_gesture("shake"):
        tiradas += 1
        music.pitch(880, 80)
        display.show(random.randint(1, 6))
    if button_a.was_pressed():
        display.scroll("Tiradas: " + str(tiradas))''') +
    ej('Vigilante del frío', 'Muestra la temperatura al pulsar A y avisa con una alarma si baja de 15 °C.',
       '''from microbit import *
import music

LIMITE = 15
while True:
    t = temperature()
    if button_a.was_pressed():
        display.scroll(str(t) + " C")
    if t < LIMITE:
        display.show(Image.NO)
        music.pitch(1000, 200)
    else:
        display.show(Image.YES)
    sleep(500)''') +
    ej('Barra de sonido', 'Una barra que sube con el ruido de la clase, usando una función y un bucle.',
       '''from microbit import *

def barra(filas):
    display.clear()
    for y in range(filas):
        for x in range(5):
            display.set_pixel(x, 4 - y, 9)

while True:
    nivel = microphone.sound_level()     # de 0 a 255
    barra(nivel * 6 // 256)              # de 0 a 5 filas
    sleep(100)''') +
    box('docente', 'Para el profesorado', P('Todas las prácticas del material tienen su versión en Python en la pestaña correspondiente. '
        'Una buena forma de empezar es resolver una práctica con bloques y, después, comparar su solución en Python línea a línea.'))
)
