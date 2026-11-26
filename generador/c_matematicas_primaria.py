# -*- coding: utf-8 -*-
"""Más retos de matemáticas para Primaria (se añaden al apartado Matemáticas)."""
from common import practica
from c_comenzamos import bm

S = 'matematicas'

practica(S, 'M9', 'sumas-con-dados', 'Sumas con dados', 1, 'P1', '15 min', ['suma', 'cálculo mental'],
    'Al agitar la placa salen dos números como si fueran dos dados. Haz la suma de cabeza y comprueba con B.',
    ['En [[agitar]], [[fijar]] <i>a</i> a [[azar]] del 1 al 6 y <i>b</i> a otro [[azar]] del 1 al 6.',
     'Muestra la operación con [[mostrar_texto]], por ejemplo «3+5».',
     'En [[boton]] (B), [[mostrar_numero]] con a [[sumar]] b.',
     'Jugad por parejas: ¿quién lo dice antes de pulsar B?'],
    ['La suma más pequeña es 2 y la más grande, 12.', 'Si quieres restas, cambia [[sumar]] por [[restar]] y pon primero el número mayor.'],
    '''let a = 0
let b = 0
input.onGesture(Gesture.Shake, function () {
    a = randint(1, 6)
    b = randint(1, 6)
    basic.showString("" + a + "+" + b)
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(a + b)
})''',
    "whenStarted\na = 0\nb = 0\n---\nwhenCondition (('[sensors:acceleration]') > 200)\na = (random 1 6)\nb = (random 1 6)\nscroll_text ('[data:join]' a '+' b)\n---\nwhenButtonPressed 'B'\nscroll_text (a + b)",
    '''from microbit import *
import random

a = b = 0
while True:
    if accelerometer.was_gesture("shake"):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        display.scroll(str(a) + "+" + str(b))
    if button_b.was_pressed():
        display.scroll(a + b)''',
    ['Usa tres dados.', 'Cambia la suma por una multiplicación para las tablas del 1 al 6.'],
    icono='dado')

practica(S, 'M10', 'cual-es-mayor', '¿Cuál es mayor?', 1, 'P1', '20 min', ['comparar números', 'condicionales'],
    'La placa muestra dos números del 1 al 20. Pulsa A si el primero es mayor y B si lo es el segundo. La placa te dice si has acertado.',
    ['En [[logo]], [[fijar]] <i>a</i> y <i>b</i> a [[azar]] del 1 al 20 y muéstralos con [[mostrar_texto]] separados por un guion.',
     'En [[boton]] (A), usa [[si_no]]: si a [[mayor]] b, muestra el sí; si no, el no.',
     'En [[boton]] (B), lo mismo con b [[mayor]] a.'],
    ['Si salen dos números iguales, ninguno es mayor: vuelve a tocar el logotipo.', 'Para niveles más altos, usa números hasta el 1000.'],
    '''let a = 0
let b = 0
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    a = randint(1, 20)
    b = randint(1, 20)
    basic.showString("" + a + "-" + b)
})
input.onButtonPressed(Button.A, function () {
    if (a > b) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
})
input.onButtonPressed(Button.B, function () {
    if (b > a) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
})''',
    "whenStarted\na = 0\nb = 0\n---\nwhenCondition (touchPin_logoTouched)\na = (random 1 20)\nb = (random 1 20)\nscroll_text ('[data:join]' a '-' b)\n---\nwhenButtonPressed 'A'\nif (a > b) {\n  led_displayImage 'yes'\n} else {\n  led_displayImage 'no'\n}\n---\nwhenButtonPressed 'B'\nif (b > a) {\n  led_displayImage 'yes'\n} else {\n  led_displayImage 'no'\n}",
    '''from microbit import *
import random

a = b = 0
while True:
    if pin_logo.is_touched():
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        display.scroll(str(a) + "-" + str(b))
    if button_a.was_pressed():
        display.show(Image.YES if a > b else Image.NO)
    if button_b.was_pressed():
        display.show(Image.YES if b > a else Image.NO)''',
    ['Lleva la cuenta de los aciertos.', 'Cambia a «¿cuál es menor?».'],
    icono='lupa')

practica(S, 'M11', 'decenas-y-unidades', 'Decenas y unidades', 1, 'P1', '20 min', ['valor posicional', 'variables'],
    'Construir números con «bloques»: A suma una decena (10) y B una unidad (1). El logotipo muestra el número formado.',
    ['Crea la variable <i>numero</i> con [[crear_variable]] y, en [[al_iniciar]], [[fijar]] numero a 0.',
     'En [[boton]] (A), [[cambiar]] numero por 10 y muestra una «D» con [[mostrar_caracter]].',
     'En [[boton]] (B), [[cambiar]] numero por 1 y muestra una «U».',
     'En [[logo]], [[mostrar_numero]] con numero. Con A+B, vuelve a 0.',
     'Reto: forma el 34 con el menor número de pulsaciones.'],
    ['Para formar el 34: 3 decenas (A, A, A) y 4 unidades (B, B, B, B).', 'Puedes usar regletas o bloques de base 10 de verdad para comprobarlo.'],
    '''let numero = 0
input.onButtonPressed(Button.A, function () {
    numero += 10
    basic.showString("D")
})
input.onButtonPressed(Button.B, function () {
    numero += 1
    basic.showString("U")
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showNumber(numero)
})
input.onButtonPressed(Button.AB, function () {
    numero = 0
    basic.showNumber(numero)
})''',
    "whenStarted\nnumero = 0\n---\nwhenButtonPressed 'A'\nnumero += 10\ndisplayCharacter 'D'\n---\nwhenButtonPressed 'B'\nnumero += 1\ndisplayCharacter 'U'\n---\nwhenCondition (touchPin_logoTouched)\nscroll_text numero\n---\nwhenButtonPressed 'A+B'\nnumero = 0\nscroll_text numero",
    '''from microbit import *

numero = 0
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        numero = 0
        display.scroll(numero)
    elif button_a.was_pressed():
        numero += 10
        display.show("D")
    elif button_b.was_pressed():
        numero += 1
        display.show("U")
    if pin_logo.is_touched():
        display.scroll(numero)''',
    ['Añade centenas (100) agitando la placa.', 'La placa propone un número al azar y hay que formarlo.'],
    icono='calculadora')

TRI = ('00100', '01010', '10001', '11111', '00000')
RECT = ('00000', '11111', '10001', '11111', '00000')
practica(S, 'M12', 'figuras-geometricas', 'Figuras geométricas', 1, 'P1', '20 min', ['geometría', 'figuras planas'],
    'Con A la placa muestra una figura (cuadrado, triángulo, rectángulo o rombo). Con B dice cuántos lados tiene.',
    ['Dibuja en papel cuadriculado de 5 × 5 un triángulo y un rectángulo.',
     'Crea la variable <i>figura</i> y, en [[boton]] (A), [[cambiar]] figura por 1 (después de 4, vuelve a 1).',
     'Con [[si_no]] y [[igual]], muestra la figura que toca: 1 cuadrado, 2 triángulo, 3 rectángulo y 4 rombo, con [[mostrar_icono]] o [[mostrar_leds]].',
     'En [[boton]] (B), [[mostrar_numero]] con el número de lados (todas tienen 4 salvo el triángulo, que tiene 3).'],
    ['El cuadrado y el rombo ya están en los iconos; el triángulo y el rectángulo los dibujas tú.', '¿Qué diferencia hay entre un cuadrado y un rombo?'],
    '''let figura = 0
input.onButtonPressed(Button.A, function () {
    figura += 1
    if (figura > 4) {
        figura = 1
    }
    if (figura == 1) {
        basic.showIcon(IconNames.Square)
    } else if (figura == 2) {
        basic.showLeds(`
            . . # . .
            . # . # .
            # . . . #
            # # # # #
            . . . . .
            `)
    } else if (figura == 3) {
        basic.showLeds(`
            . . . . .
            # # # # #
            # . . . #
            # # # # #
            . . . . .
            `)
    } else {
        basic.showIcon(IconNames.Diamond)
    }
})
input.onButtonPressed(Button.B, function () {
    if (figura == 2) {
        basic.showNumber(3)
    } else {
        basic.showNumber(4)
    }
})''',
    "whenStarted\nfigura = 0\n---\nwhenButtonPressed 'A'\nfigura += 1\nif (figura > 4) {\n  figura = 1\n}\nif (figura == 1) {\n  led_displayImage 'square'\n} (figura == 2) {\n  '[display:mbDisplay]' %d\n} (figura == 3) {\n  '[display:mbDisplay]' %d\n} else {\n  led_displayImage 'diamond'\n}\n---\nwhenButtonPressed 'B'\nif (figura == 2) {\n  scroll_text 3\n} else {\n  scroll_text 4\n}" % (bm(*TRI), bm(*RECT)),
    '''from microbit import *

TRIANGULO = Image("00900:09090:90009:99999:00000")
RECTANGULO = Image("00000:99999:90009:99999:00000")
figuras = [Image.SQUARE, TRIANGULO, RECTANGULO, Image.DIAMOND]
lados = [4, 3, 4, 4]
figura = 0
while True:
    if button_a.was_pressed():
        figura = (figura + 1) % 4
        display.show(figuras[figura])
    if button_b.was_pressed():
        display.scroll(lados[figura])''',
    ['Añade un pentágono dibujado por ti.', 'Cuenta también los vértices.'],
    icono='matriz')

practica(S, 'M13', 'metros-y-centimetros', 'Metros y centímetros', 2, 'P2', '20 min', ['medida', 'cambio de unidades'],
    'Practicar el cambio de unidades: con A sale una longitud en metros y con B su equivalencia en centímetros.',
    ['En [[boton]] (A), [[fijar]] <i>metros</i> a [[azar]] del 1 al 9 y muéstralo con [[mostrar_texto]] seguido de «m».',
     'Piensa: ¿cuántos centímetros son?',
     'En [[boton]] (B), [[mostrar_numero]] con metros [[multiplicar]] 100 y después «cm».'],
    ['1 metro = 100 centímetros.', 'Para kilómetros y metros, multiplica por 1000.'],
    '''let metros = 0
input.onButtonPressed(Button.A, function () {
    metros = randint(1, 9)
    basic.showString("" + metros + "m")
})
input.onButtonPressed(Button.B, function () {
    basic.showString("" + metros * 100 + "cm")
})''',
    "whenStarted\nmetros = 0\n---\nwhenButtonPressed 'A'\nmetros = (random 1 9)\nscroll_text ('[data:join]' metros 'm')\n---\nwhenButtonPressed 'B'\nscroll_text ('[data:join]' (metros * 100) 'cm')",
    '''from microbit import *
import random

metros = 0
while True:
    if button_a.was_pressed():
        metros = random.randint(1, 9)
        display.scroll(str(metros) + "m")
    if button_b.was_pressed():
        display.scroll(str(metros * 100) + "cm")''',
    ['Cambia a kilos y gramos, o a horas y minutos.', 'Mide objetos de clase con una cinta métrica y comprueba.'],
    icono='reloj')

practica(S, 'M14', 'series-numericas', 'Series numéricas', 2, 'P2', '25 min', ['patrones', 'sentido algebraico'],
    'La placa muestra el principio de una serie (por ejemplo, 3, 6, 9) y hay que adivinar el número siguiente.',
    ['En [[boton]] (A), [[fijar]] <i>salto</i> a [[azar]] del 2 al 9 y <i>inicio</i> a otro [[azar]] del 1 al 10.',
     'Muestra los tres primeros términos: inicio, inicio + salto e inicio + 2 × salto.',
     'Piensa el cuarto término.',
     'En [[boton]] (B), [[mostrar_numero]] con inicio [[sumar]] 3 [[multiplicar]] salto.'],
    ['Cada número se obtiene sumando siempre la misma cantidad: el <b>salto</b>.', 'Reto: haz series que resten o que multipliquen por 2.'],
    '''let salto = 0
let inicio = 0
input.onButtonPressed(Button.A, function () {
    salto = randint(2, 9)
    inicio = randint(1, 10)
    basic.showString("" + inicio + "," + (inicio + salto) + "," + (inicio + 2 * salto) + ",?")
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(inicio + 3 * salto)
})''',
    "whenStarted\nsalto = 0\ninicio = 0\n---\nwhenButtonPressed 'A'\nsalto = (random 2 9)\ninicio = (random 1 10)\nscroll_text ('[data:join]' inicio ',' (inicio + salto) ',' (inicio + (2 * salto)) ',?')\n---\nwhenButtonPressed 'B'\nscroll_text (inicio + (3 * salto))",
    '''from microbit import *
import random

salto = inicio = 0
while True:
    if button_a.was_pressed():
        salto = random.randint(2, 9)
        inicio = random.randint(1, 10)
        display.scroll("%d,%d,%d,?" % (inicio, inicio + salto, inicio + 2 * salto))
    if button_b.was_pressed():
        display.scroll(inicio + 3 * salto)''',
    ['Muestra también el salto con el logotipo.', 'Inventa series con números pares o con múltiplos de 5.'],
    icono='lista')
