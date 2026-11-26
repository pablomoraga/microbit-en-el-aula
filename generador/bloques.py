# -*- coding: utf-8 -*-
"""Bloques en línea para el paso a paso: en el texto se escribe [[clave]] y se muestra el bloque
con su color y su categoría en el editor que haya elegido el alumnado (MakeCode, MicroBlocks o Python).
Los nombres de MakeCode salen del propio editor en español; los de MicroBlocks, de su traducción oficial."""
import re, html
e = html.escape

MC = {'Básico': '#1E90FF', 'Entrada': '#D400D4', 'Música': '#E63022', 'LED': '#5C2D91', 'Radio': '#E3008C', 'Bucles': '#00AA00',
      'Lógica': '#00A4A6', 'Variables': '#DC143C', 'Matemática': '#9400D3', 'Pines': '#B22222', 'Arreglos': '#E65722', 'Juego': '#007A4B'}
MB = {'Control': '#D18C25', 'Salida': '#4852BF', 'Entrada': '#9F42A5', 'Pines': '#548799', 'Operadores': '#479D1D',
      'Variables': '#D3732A', 'Datos': '#C44E6B', 'Radio': '#1E997A', 'Tonos': '#4852BF', 'Pantalla LED': '#4852BF',
      'Sensores básicos': '#9F42A5', 'TouchPin': '#9F42A5', 'Micrófono': '#9F42A5', 'Servo': '#4852BF'}

# clave: (MakeCode: texto, categoría) · (MicroBlocks: texto, categoría) · Python
B = {
    'al_iniciar': (('al iniciar', 'Básico'), ('al empezar', 'Control'), 'arriba, fuera de while True'),
    'para_siempre': (('para siempre', 'Básico'), ('por siempre', 'Control'), 'while True:'),
    'mostrar_texto': (('mostrar cadena', 'Básico'), ('anima el texto', 'Pantalla LED'), 'display.scroll("…")'),
    'mostrar_numero': (('mostrar número', 'Básico'), ('anima el texto', 'Pantalla LED'), 'display.scroll(n)'),
    'mostrar_icono': (('mostrar ícono', 'Básico'), ('muestra imagen', 'Pantalla LED'), 'display.show(Image.…)'),
    'mostrar_leds': (('mostrar LEDs', 'Básico'), ('pantalla', 'Pantalla LED'), 'display.show(Image("…"))'),
    'mostrar_caracter': (('mostrar cadena', 'Básico'), ('muestra carácter', 'Pantalla LED'), 'display.show("A")'),
    'borrar': (('borrar la pantalla', 'Básico'), ('limpia pantalla', 'Pantalla LED'), 'display.clear()'),
    'pausa': (('pausa (ms)', 'Básico'), ('espera … milisegundos', 'Control'), 'sleep(ms)'),
    'flecha': (('mostrar flecha', 'Básico'), ('pantalla', 'Pantalla LED'), 'Image.ARROW_N'),
    'boton': (('al presionarse el botón A', 'Entrada'), ('cuando se pulse el botón A', 'Control'), 'button_a.was_pressed()'),
    'boton_pulsado': (('botón A presionado', 'Entrada'), ('botón A', 'Entrada'), 'button_a.is_pressed()'),
    'logo': (('al pulsar el logotipo', 'Entrada'), ('cuando · logo touched', 'Control'), 'pin_logo.is_touched()'),
    'agitar': (('si agitar', 'Entrada'), ('cuando · aceleración > 200', 'Control'), 'accelerometer.was_gesture("shake")'),
    'luz': (('nivel de luz', 'Entrada'), ('nivel de luz', 'Sensores básicos'), 'display.read_light_level()'),
    'temperatura': (('temperatura (°C)', 'Entrada'), ('temperatura (°C)', 'Sensores básicos'), 'temperature()'),
    'inclinacion': (('aceleración (mg) x', 'Entrada'), ('inclinación x', 'Sensores básicos'), 'accelerometer.get_x()'),
    'aceleracion': (('si agitar', 'Entrada'), ('aceleración', 'Sensores básicos'), 'accelerometer.was_gesture("shake")'),
    'sonido_nivel': (('nivel de sonido', 'Entrada'), ('volumen', 'Micrófono'), 'microphone.sound_level()'),
    'sonido_alto': (('al detectar el sonido alto', 'Entrada'), ('recuento de palmadas', 'Micrófono'), 'microphone.was_event(SoundEvent.LOUD)'),
    'brujula': (('dirección de la brújula (°)', 'Entrada'), None, 'compass.heading()'),
    'tiempo': (('tiempo de ejecución (ms)', 'Entrada'), ('cronómetro', 'Entrada'), 'running_time()'),
    'reiniciar_tiempo': (('fijar inicio a tiempo de ejecución', 'Variables'), ('reinicia cronómetro', 'Entrada'), 'inicio = running_time()'),
    'tono': (('reproduce tono', 'Música'), ('toca la frecuencia', 'Tonos'), 'music.pitch(Hz, ms)'),
    'nota': (('reproduce tono', 'Música'), ('toca la nota', 'Tonos'), 'music.pitch(Hz, ms)'),
    'melodia': (('reproduce melodía', 'Música'), ('toca la nota', 'Tonos'), 'music.play([…])'),
    'efecto': (('reproduce (risa, feliz…)', 'Música'), ('toca la nota', 'Tonos'), 'audio.play(Sound.…)'),
    'si': (('si … entonces', 'Lógica'), ('si', 'Control'), 'if …:'),
    'si_no': (('si … entonces … si no', 'Lógica'), ('si … si no', 'Control'), 'if …: … else:'),
    'menor': (('0 < 0', 'Lógica'), ('_ < _', 'Operadores'), '<'),
    'mayor': (('0 > 0', 'Lógica'), ('_ > _', 'Operadores'), '>'),
    'igual': (('0 = 0', 'Lógica'), ('_ = _', 'Operadores'), '=='),
    'y': (('… y …', 'Lógica'), ('_ y _', 'Operadores'), 'and'),
    'o': (('… o …', 'Lógica'), ('_ o _', 'Operadores'), 'or'),
    'azar': (('escoger al azar de 1 a 10', 'Matemática'), ('número al azar entre 1 y 10', 'Operadores'), 'random.randint(1, 10)'),
    'sumar': (('0 + 0', 'Matemática'), ('_ + _', 'Operadores'), '+'),
    'restar': (('0 − 0', 'Matemática'), ('_ − _', 'Operadores'), '-'),
    'multiplicar': (('0 × 0', 'Matemática'), ('_ × _', 'Operadores'), '*'),
    'dividir': (('0 ÷ 0', 'Matemática'), ('_ / _', 'Operadores'), '/'),
    'resto': (('resto de … ÷ …', 'Matemática'), ('_ módulo _', 'Operadores'), '%'),
    'crear_variable': (('Crear una variable…', 'Variables'), ('Crea una variable', 'Variables'), 'nombre = 0'),
    'fijar': (('fijar … a', 'Variables'), ('asigna a … el valor', 'Variables'), 'x = 0'),
    'cambiar': (('cambiar … por 1', 'Variables'), ('aumenta … en 1', 'Variables'), 'x += 1'),
    'repetir': (('repetir 4 veces', 'Bucles'), ('repite 10 veces', 'Control'), 'for i in range(4):'),
    'para_indice': (('para índice de 0 a 4', 'Bucles'), ('por cada i en 5', 'Control'), 'for i in range(5):'),
    'para_elemento': (('para el elemento valor de lista', 'Bucles'), ('por cada … en lista', 'Control'), 'for valor in lista:'),
    'mientras': (('mientras', 'Bucles'), ('repite hasta que', 'Control'), 'while …:'),
    'esperar_hasta': (('mientras … pausa', 'Bucles'), ('espera hasta que', 'Control'), 'while not …: sleep(1)'),
    'graficar': (('graficar x y', 'LED'), ('enciende x y', 'Pantalla LED'), 'display.set_pixel(x, y, 9)'),
    'ocultar': (('ocultar x y', 'LED'), ('apaga x y', 'Pantalla LED'), 'display.set_pixel(x, y, 0)'),
    'barras': (('trazar gráfico de barras', 'LED'), ('enciende x y', 'Pantalla LED'), 'display.set_pixel(…)'),
    'radio_grupo': (('radio establecer grupo', 'Radio'), ('fija el grupo de radio a', 'Radio'), 'radio.config(group=1)'),
    'radio_enviar_numero': (('radio enviar número', 'Radio'), ('envía número por radio', 'Radio'), 'radio.send("1")'),
    'radio_enviar_texto': (('radio enviar cadena', 'Radio'), ('envía texto por radio', 'Radio'), 'radio.send("Hola")'),
    'radio_recibir_numero': (('al recibir radio recibirNúmero', 'Radio'), ('¿mensaje de radio recibido?', 'Radio'), 'radio.receive()'),
    'radio_recibir_texto': (('al recibir radio recibirCadena', 'Radio'), ('¿mensaje de radio recibido?', 'Radio'), 'radio.receive()'),
    'pin_escribir': (('escritura digital pin P0 a 1', 'Pines'), ('pon pin digital 0 a', 'Pines'), 'pin0.write_digital(1)'),
    'pin_leer': (('lectura analógica pin P1', 'Pines'), ('lectura analógica 1', 'Pines'), 'pin1.read_analog()'),
    'pin_digital': (('lectura digital pin P1', 'Pines'), ('lectura digital 1', 'Pines'), 'pin1.read_digital()'),
    'pin_tocado': (('al presionarse pin P0', 'Entrada'), ('cuando · pin 0 touched', 'Control'), 'pin0.is_touched()'),
    'servo': (('escribir servo pin P0 a 90', 'Pines'), ('pon el servo 0 a … grados', 'Servo'), 'pin0.write_analog(…)'),
    'lista': (('matriz de', 'Arreglos'), ('lista', 'Datos'), '[…]'),
    'elemento': (('obtener el valor en', 'Arreglos'), ('elemento … de', 'Datos'), 'lista[i]'),
    'unir': (('unir', 'Básico'), ('une', 'Datos'), 'str(a) + "…"'),
    'di': (('mostrar número', 'Básico'), ('di', 'Salida'), 'print(…)'),
}

def chip(key):
    mc, mb, py = B[key]
    out = '<span class="bq-g">'
    out += '<span class="bq e-mc" style="--c:%s" title="MakeCode · %s">%s</span>' % (MC[mc[1]], mc[1], e(mc[0]))
    if mb:
        out += '<span class="bq e-mb" style="--c:%s" title="MicroBlocks · %s">%s</span>' % (MB[mb[1]], mb[1], e(mb[0]))
    else:
        out += '<span class="bq e-mb bq-no" title="No existe en MicroBlocks para la micro:bit">sin bloque en MicroBlocks</span>'
    out += '<code class="e-py" title="Python">%s</code>' % e(py)
    return out + '</span>'

def expand(text):
    """Sustituye cada [[clave]] por su bloque."""
    return re.sub(r'\[\[(\w+)\]\]', lambda m: chip(m.group(1)), text)

SELECTOR = ('<div class="ed-sel" role="group" aria-label="Editor"><span>Trabajo con:</span>'
            '<button type="button" data-t="makecode">MakeCode</button><button type="button" data-t="microblocks">MicroBlocks</button>'
            '<button type="button" data-t="python">Python</button></div>')
