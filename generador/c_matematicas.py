# -*- coding: utf-8 -*-
"""Matemáticas con micro:bit: actividades organizadas por los sentidos matemáticos del currículo."""
from common import page, practica, P, ul, box, tabla, kbd

S = 'matematicas'
GRUPOS = {}

page(S, 'matematicas-con-microbit', 'Matemáticas con micro:bit', P(
    'La micro:bit es una calculadora que se mueve, mide y cuenta. Con ella las matemáticas dejan de estar solo en el papel: se generan números al azar, se miden tiempos, '
    'se dibuja en una cuadrícula de coordenadas y se recogen datos reales para analizarlos.') +
    P('Las actividades de este apartado se organizan según los <b>sentidos matemáticos</b> del currículo de Matemáticas (LOMLOE) y se pueden usar como rincón de cálculo, '
      'como reto al terminar una tarea o como proyecto de clase.') +
    tabla(['Sentido', 'Actividad', 'Etapa'], [
        ['Numérico', '<a href="sumas-con-dados.html">M9 · Sumas con dados</a>, <a href="cual-es-mayor.html">M10 · ¿Cuál es mayor?</a>, <a href="decenas-y-unidades.html">M11 · Decenas y unidades</a>', 'Primaria 6-9'],
        ['Numérico', '<a href="tablas-de-multiplicar.html">M1 · Tablas de multiplicar</a>, <a href="par-o-impar.html">M2 · ¿Par o impar?</a>', 'Primaria'],
        ['Espacial', '<a href="figuras-geometricas.html">M12 · Figuras geométricas</a>', 'Primaria 6-9'],
        ['Medida', '<a href="metros-y-centimetros.html">M13 · Metros y centímetros</a>', 'Primaria 10-12'],
        ['Algebraico', '<a href="series-numericas.html">M14 · Series numéricas</a>', 'Primaria 10-12'],
        ['Numérico', '<a href="fracciones-de-luz.html">M3 · Fracciones de luz</a>', 'Primaria 10-12'],
        ['Espacial', '<a href="coordenadas.html">M4 · Caza de coordenadas</a>', 'Primaria 10-12 · ESO'],
        ['Medida', '<a href="velocidad.html">M5 · ¿A qué velocidad vas?</a>', 'ESO'],
        ['Algebraico', '<a href="numeros-binarios.html">M6 · Números binarios</a>', 'Primaria 10-12 · ESO'],
        ['Estocástico', '<a href="probabilidad-del-dado.html">M7 · La probabilidad del dado</a>', 'ESO'],
        ['Estocástico', '<a href="media-de-temperaturas.html">M8 · Media de temperaturas</a>', 'ESO'],
    ]) +
    box('docente', 'Ideas para el aula', ul([
        'Antes de ejecutar un programa, pide una <b>predicción</b>: ¿qué número saldrá?, ¿cuántas veces aparecerá el 6? Después, compara.',
        'Muchas actividades generan datos: anótalos en una tabla y haz gráficas en papel o en la hoja de cálculo.',
        'Las prácticas de Comenzamos también tienen mucha matemática: el dado (azar), el cronómetro (medida del tiempo), el barrido de LED (coordenadas) o la brújula (ángulos).'])),
    icono='calculadora')

# ------------------------------------------------------------------ M1
practica(S, 'M1', 'tablas-de-multiplicar', 'Tablas de multiplicar', 1, 'P2', '20 min', ['sentido numérico', 'azar'],
    'Practicar las tablas: con A la placa propone una multiplicación al azar y con B muestra el resultado para comprobarlo.',
    ['En [[boton]] (A), [[fijar]] <i>a</i> y <i>b</i> a [[azar]] del 1 al 10.',
     'Muestra la operación con [[mostrar_texto]], por ejemplo «7x8».',
     'Piensa la respuesta (o escríbela en un papel).',
     'En [[boton]] (B), [[mostrar_numero]] con a [[multiplicar]] b y comprueba si has acertado.'],
    ['Para escribir la operación une textos y números: «a», « x », «b».',
     'En MakeCode, la multiplicación está en <b>Matemática</b>; en MicroBlocks, en <b>Operadores</b>.',
     'Si solo quieres practicar una tabla, fija <i>a</i> a ese número en lugar de elegirlo al azar.'],
    '''let a = 0
let b = 0
input.onButtonPressed(Button.A, function () {
    a = randint(1, 10)
    b = randint(1, 10)
    basic.showString("" + a + "x" + b)
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(a * b)
})''',
    "whenButtonPressed 'A'\na = (random 1 10)\nb = (random 1 10)\nscroll_text ('[data:join]' a 'x' b)\n---\nwhenButtonPressed 'B'\nscroll_text (a * b)",
    '''from microbit import *
import random

a = b = 0
while True:
    if button_a.was_pressed():
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        display.scroll(str(a) + "x" + str(b))
    if button_b.was_pressed():
        display.scroll(a * b)''',
    ['Haz que solo pregunte la tabla del 7.', 'Cambia a sumas o restas para Primaria 6-9.', 'Cuenta los aciertos: el alumno pulsa el logotipo si acertó.'],
    icono='calculadora')

# ------------------------------------------------------------------ M2
practica(S, 'M2', 'par-o-impar', '¿Par o impar?', 1, 'P1', '20 min', ['sentido numérico', 'condicionales'],
    'Un juego de rapidez: al agitar aparece un número del 1 al 20; pulsa A si es par y B si es impar. La placa te dice si has acertado.',
    ['En [[agitar]], [[fijar]] <i>n</i> a [[azar]] del 1 al 20 y muéstralo con [[mostrar_numero]].',
     'En [[boton]] (A, par): con [[si_no]], si el [[resto]] de n entre 2 [[igual]] 0, muestra el sí; si no, el no.',
     'Al pulsar B (impar): al revés.',
     'Jugad por parejas: ¿quién acierta más de diez seguidos?'],
    ['Un número es <b>par</b> si al dividirlo entre 2 el resto es 0.',
     'En MakeCode el resto está en %s (Matemática); en MicroBlocks es %s; en Python, el operador <code>%%</code>.' % (kbd('resto de'), kbd('módulo'))],
    '''let n = 0
input.onGesture(Gesture.Shake, function () {
    n = randint(1, 20)
    basic.showNumber(n)
})
input.onButtonPressed(Button.A, function () {
    if (n % 2 == 0) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
})
input.onButtonPressed(Button.B, function () {
    if (n % 2 == 1) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
})''',
    "whenStarted\nn = 0\n---\nwhenCondition (('[sensors:acceleration]') > 200)\nn = (random 1 20)\nscroll_text n\n---\nwhenButtonPressed 'A'\nif ((n % 2) == 0) {\n  led_displayImage 'yes'\n} else {\n  led_displayImage 'no'\n}\n---\nwhenButtonPressed 'B'\nif ((n % 2) == 1) {\n  led_displayImage 'yes'\n} else {\n  led_displayImage 'no'\n}",
    '''from microbit import *
import random

n = 0
while True:
    if accelerometer.was_gesture("shake"):
        n = random.randint(1, 20)
        display.scroll(n)
    if button_a.was_pressed():
        if n % 2 == 0:
            display.show(Image.YES)
        else:
            display.show(Image.NO)
    if button_b.was_pressed():
        if n % 2 == 1:
            display.show(Image.YES)
        else:
            display.show(Image.NO)''',
    ['Cambia el juego a «¿múltiplo de 3?».', 'Amplía hasta el 100 para 5.º y 6.º.'],
    icono='dado')

# ------------------------------------------------------------------ M3
practica(S, 'M3', 'fracciones-de-luz', 'Fracciones de luz', 2, 'P2', '25 min', ['fracciones', 'porcentajes', 'bucles'],
    'La pantalla tiene 25 LED: con A encendemos uno más y vemos la fracción de pantalla iluminada; con B, su porcentaje.',
    ['Crea la variable <i>encendidos</i> con [[crear_variable]] y, en [[al_iniciar]], [[fijar]] a 0.',
     'En [[boton]] (A), [[cambiar]] encendidos por 1 (si pasa de 25, vuelve a 0), [[borrar]] y con [[para_indice]] y [[graficar]] enciende tantos LED como diga la variable.',
     'En [[boton]] (B), muestra el porcentaje: encendidos [[multiplicar]] 4 (porque 25 × 4 = 100).',
     'Busca fracciones equivalentes: ¿cuántos LED son 1/5 de la pantalla? ¿Y 2/5?'],
    ['Para recorrer los LED en orden: columna = i mod 5 y fila = i ÷ 5 (división entera).',
     'En MicroBlocks las coordenadas empiezan en 1: suma 1 a la columna y a la fila.'],
    '''let encendidos = 0
input.onButtonPressed(Button.A, function () {
    encendidos += 1
    if (encendidos > 25) {
        encendidos = 0
    }
    basic.clearScreen()
    for (let i = 0; i < encendidos; i++) {
        led.plot(i % 5, Math.idiv(i, 5))
    }
})
input.onButtonPressed(Button.B, function () {
    basic.showString("" + encendidos * 4 + "%")
})''',
    "whenStarted\nencendidos = 0\n---\nwhenButtonPressed 'A'\nencendidos += 1\nif (encendidos > 25) {\n  encendidos = 0\n}\n'[display:mbDisplayOff]'\nfor i encendidos {\n  '[display:mbPlot]' (((i - 1) % 5) + 1) (((i - 1) / 5) + 1)\n}\n---\nwhenButtonPressed 'B'\nscroll_text ('[data:join]' (encendidos * 4) '%')",
    '''from microbit import *

encendidos = 0
while True:
    if button_a.was_pressed():
        encendidos += 1
        if encendidos > 25:
            encendidos = 0
        display.clear()
        for i in range(encendidos):
            display.set_pixel(i % 5, i // 5, 9)
    if button_b.was_pressed():
        display.scroll(str(encendidos * 4) + "%")''',
    ['Muestra también la fracción simplificada (por ejemplo, 5/25 = 1/5).', 'Haz un juego: la placa propone un porcentaje y hay que encender los LED correctos.'],
    icono='matriz')

# ------------------------------------------------------------------ M4
practica(S, 'M4', 'coordenadas', 'Caza de coordenadas', 2, 'P2', '25 min', ['sentido espacial', 'coordenadas'],
    'La placa enciende un punto al azar y hay que decir sus coordenadas. Con A se comprueba la respuesta y con B aparece un punto nuevo.',
    ['Recuerda: en la micro:bit, x es la columna (de izquierda a derecha) e y es la fila (de arriba abajo). En MakeCode y Python empiezan en 0.',
     'En [[boton]] (B), [[borrar]], [[fijar]] x e y a [[azar]] y enciende el punto con [[graficar]].',
     'Di en voz alta sus coordenadas.',
     'En [[boton]] (A), [[mostrar_texto]] con las coordenadas en el formato «x,y».'],
    ['Compara con el plano cartesiano de clase: allí el eje y sube hacia arriba, en la pantalla de la micro:bit baja. ¿Por qué crees que es así?',
     'En MicroBlocks las coordenadas van de 1 a 5.'],
    '''let x = 0
let y = 0
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    x = randint(0, 4)
    y = randint(0, 4)
    led.plot(x, y)
})
input.onButtonPressed(Button.A, function () {
    basic.showString("" + x + "," + y)
    led.plot(x, y)
})''',
    "whenButtonPressed 'B'\n'[display:mbDisplayOff]'\nx = (random 1 5)\ny = (random 1 5)\n'[display:mbPlot]' x y\n---\nwhenButtonPressed 'A'\nscroll_text ('[data:join]' x ',' y)\n'[display:mbPlot]' x y",
    '''from microbit import *
import random

x = y = 0
while True:
    if button_b.was_pressed():
        display.clear()
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        display.set_pixel(x, y, 9)
    if button_a.was_pressed():
        display.scroll(str(x) + "," + str(y))
        display.set_pixel(x, y, 9)''',
    ['Enciende dos puntos y calcula cuántos pasos hay entre ellos (en horizontal y vertical).', 'Dibuja figuras dando solo las coordenadas a un compañero.'],
    icono='matriz')

# ------------------------------------------------------------------ M5
practica(S, 'M5', 'velocidad', '¿A qué velocidad vas?', 2, 'ESO', '40 min', ['sentido de la medida', 'tiempo', 'división'],
    'Medir cuánto tardas en recorrer 10 metros y calcular tu velocidad: A inicia el cronómetro, B lo para y muestra el tiempo y la velocidad.',
    ['Marca en el patio una salida y una meta a 10 metros.',
     'En [[boton]] (A), guarda el momento de salida con [[reiniciar_tiempo]].',
     'En [[boton]] (B), calcula el tiempo con [[tiempo]] [[dividir]] 1000 y la velocidad: v = 10 [[dividir]] tiempo.',
     'Muestra la velocidad. Compara andando, corriendo y a la pata coja.'],
    ['La velocidad se mide en metros por segundo (m/s). Para pasarla a km/h, multiplica por 3,6.',
     'MicroBlocks trabaja con números enteros: calcula la velocidad en centímetros por segundo (1 000 000 ÷ milisegundos).'],
    '''let salida = 0
let segundos = 0
input.onButtonPressed(Button.A, function () {
    salida = input.runningTime()
    basic.showIcon(IconNames.Yes)
})
input.onButtonPressed(Button.B, function () {
    segundos = (input.runningTime() - salida) / 1000
    basic.showString("t=" + Math.round(segundos * 10) / 10 + "s")
    basic.showString("v=" + Math.round(10 / segundos * 10) / 10 + "m/s")
})''',
    "whenButtonPressed 'A'\nresetTimer\nled_displayImage 'yes'\n---\nwhenButtonPressed 'B'\nms = (timer)\nscroll_text ('[data:join]' 't=' ms 'ms')\nscroll_text ('[data:join]' 'v=' (1000000 / ms) 'cm/s')",
    '''from microbit import *

salida = 0
while True:
    if button_a.was_pressed():
        salida = running_time()
        display.show(Image.YES)
    if button_b.was_pressed():
        segundos = (running_time() - salida) / 1000
        display.scroll("t=" + str(round(segundos, 1)) + "s")
        display.scroll("v=" + str(round(10 / segundos, 1)) + "m/s")''',
    ['Muestra también la velocidad en km/h.', 'Haced una tabla con las velocidades de toda la clase y calculad la media.'],
    icono='reloj')

# ------------------------------------------------------------------ M6
practica(S, 'M6', 'numeros-binarios', 'Números binarios', 3, 'ESO', '35 min', ['sistema binario', 'potencias de 2', 'bucles'],
    'Ver cómo cuentan los ordenadores: con A el número sube de 0 a 31 y la fila central muestra sus 5 cifras binarias (LED encendido = 1).',
    ['Los LED de la fila central representan, de derecha a izquierda, 1, 2, 4, 8 y 16.',
     'En [[boton]] (A), [[cambiar]] número por 1 (después de 31 vuelve a 0).',
     'Con [[para_indice]], calcula si cada cifra es 1 con el [[resto]] entre 2. Si es 1, [[graficar]]; si no, [[ocultar]].',
     'Con B, muestra el número en decimal para comprobarlo.'],
    ['La potencia empieza en 1 y se multiplica por 2 en cada vuelta del bucle.',
     'Prueba primero con números fáciles: 1 = 00001, 2 = 00010, 3 = 00011, 16 = 10000.'],
    '''let numero = 0
let potencia = 1
input.onButtonPressed(Button.A, function () {
    numero += 1
    if (numero > 31) {
        numero = 0
    }
    potencia = 1
    for (let i = 0; i <= 4; i++) {
        if (Math.idiv(numero, potencia) % 2 == 1) {
            led.plot(4 - i, 2)
        } else {
            led.unplot(4 - i, 2)
        }
        potencia = potencia * 2
    }
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(numero)
})''',
    "whenStarted\nnumero = 0\n---\nwhenButtonPressed 'A'\nnumero += 1\nif (numero > 31) {\n  numero = 0\n}\npotencia = 1\nfor i 5 {\n  if (((numero / potencia) % 2) == 1) {\n    '[display:mbPlot]' (6 - i) 3\n  } else {\n    '[display:mbUnplot]' (6 - i) 3\n  }\n  potencia = (potencia * 2)\n}\n---\nwhenButtonPressed 'B'\nscroll_text numero",
    '''from microbit import *

numero = 0
while True:
    if button_a.was_pressed():
        numero += 1
        if numero > 31:
            numero = 0
        potencia = 1
        for i in range(5):
            if (numero // potencia) % 2 == 1:
                display.set_pixel(4 - i, 2, 9)
            else:
                display.set_pixel(4 - i, 2, 0)
            potencia *= 2
    if button_b.was_pressed():
        display.scroll(numero)''',
    ['Usa dos filas para llegar hasta 1023 (10 bits).', 'Reto inverso: la placa muestra un número binario y hay que adivinar el decimal.'],
    icono='chip')

# ------------------------------------------------------------------ M7
practica(S, 'M7', 'probabilidad-del-dado', 'La probabilidad del dado', 3, 'ESO', '40 min', ['sentido estocástico', 'listas', 'frecuencias'],
    'Lanzar un dado 600 veces en un segundo y contar cuántas veces sale cada cara, para comparar la frecuencia con la probabilidad teórica (1/6).',
    ['Predice: si lanzas un dado 600 veces, ¿cuántas veces saldrá cada número?',
     '[[fijar]] <i>veces</i> a una [[lista]] de seis ceros.',
     'Con [[repetir]] 600 veces: elige una cara con [[azar]] del 1 al 6 y suma 1 a su contador.',
     'Muestra los seis resultados uno tras otro. Anótalos y calcula la frecuencia relativa de cada cara.'],
    ['En MakeCode y Python la cara 1 está en la posición 0 de la lista; en MicroBlocks, en la posición 1.',
     'Cuantos más lanzamientos, más se acercan los resultados a 100 por cara: es la <b>ley de los grandes números</b>.'],
    '''let veces: number[] = []
input.onButtonPressed(Button.A, function () {
    veces = [0, 0, 0, 0, 0, 0]
    for (let index = 0; index < 600; index++) {
        let cara = randint(1, 6)
        veces[cara - 1] = veces[cara - 1] + 1
    }
    for (let j = 0; j <= 5; j++) {
        basic.showString("" + (j + 1) + ":" + veces[j])
    }
})''',
    "whenButtonPressed 'A'\nveces = ('[data:makeList]' 0 0 0 0 0 0)\nrepeat 600 {\n  cara = (random 1 6)\n  atPut cara veces ((at cara veces) + 1)\n}\nfor j 6 {\n  scroll_text ('[data:join]' j ':' (at j veces))\n}",
    '''from microbit import *
import random

while True:
    if button_a.was_pressed():
        veces = [0, 0, 0, 0, 0, 0]
        for i in range(600):
            cara = random.randint(1, 6)
            veces[cara - 1] += 1
        for j in range(6):
            display.scroll(str(j + 1) + ":" + str(veces[j]))''',
    ['Repite con 60 y con 6000 lanzamientos: ¿qué observas?', 'Simula dos dados y cuenta las sumas del 2 al 12: ¿son todas igual de probables?'],
    icono='dado')

# ------------------------------------------------------------------ M8
practica(S, 'M8', 'media-de-temperaturas', 'Media de temperaturas', 3, 'ESO', '35 min', ['estadística', 'listas', 'media'],
    'Tomar 6 medidas de temperatura (una cada 10 segundos), guardarlas en una lista y calcular la media, la máxima y la mínima.',
    ['En [[boton]] (A), vacía la [[lista]] y, con [[repetir]] 6 veces, añade [[temperatura]] y haz una [[pausa]] de 10 000 ms.',
     'Suma todas las medidas y divide entre el número de medidas: esa es la <b>media</b>.',
     'Recorre la lista con [[para_elemento]] para encontrar la máxima y la mínima.',
     'Muestra los tres resultados.'],
    ['La media de 6 números es su suma dividida entre 6.',
     'En MicroBlocks la división es entera: la media saldrá sin decimales.'],
    '''let medidas: number[] = []
input.onButtonPressed(Button.A, function () {
    medidas = []
    for (let index = 0; index < 6; index++) {
        medidas.push(input.temperature())
        led.toggle(2, 2)
        basic.pause(10000)
    }
    let suma = 0
    let maxima = medidas[0]
    let minima = medidas[0]
    for (let valor of medidas) {
        suma += valor
        maxima = Math.max(maxima, valor)
        minima = Math.min(minima, valor)
    }
    basic.showString("Media " + suma / medidas.length)
    basic.showString("Max " + maxima)
    basic.showString("Min " + minima)
})''',
    "whenButtonPressed 'A'\nmedidas = ('[data:makeList]')\nrepeat 6 {\n  '[data:addLast]' ('[sensors:temperature]') medidas\n  '[display:mbPlot]' 3 3\n  waitMillis 10000\n  '[display:mbUnplot]' 3 3\n}\nsuma = 0\nmaxima = (at 1 medidas)\nminima = (at 1 medidas)\nfor valor medidas {\n  suma += valor\n  maxima = (maximum maxima valor)\n  minima = (minimum minima valor)\n}\nscroll_text ('[data:join]' 'Media ' (suma / (size medidas)))\nscroll_text ('[data:join]' 'Max ' maxima)\nscroll_text ('[data:join]' 'Min ' minima)",
    '''from microbit import *

while True:
    if button_a.was_pressed():
        medidas = []
        for i in range(6):
            medidas.append(temperature())
            display.set_pixel(2, 2, 9 * (i % 2))
            sleep(10000)
        media = sum(medidas) / len(medidas)
        display.scroll("Media " + str(round(media, 1)))
        display.scroll("Max " + str(max(medidas)))
        display.scroll("Min " + str(min(medidas)))''',
    ['Calcula también el rango (máxima − mínima).', 'Toma una medida cada hora durante la jornada y dibuja la gráfica.'],
    icono='termometro')
