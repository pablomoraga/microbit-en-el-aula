# -*- coding: utf-8 -*-
from common import page, P, ul, ol, box, tabla, h2, h3, py_html, e, anatomia
import makecode, mbk, placa
from iconos import icon

S = 'conoce'
G1, G2 = 'La placa micro:bit V2', 'Los editores'
GRUPOS = {
    G1: P('La placa por delante y por detrás, sus pines, su ficha técnica y cómo cargar un programa.'),
    G2: P('MakeCode, MicroBlocks y Python: cómo es cada editor, cómo se organizan sus bloques o instrucciones y cómo ampliarlos con extensiones y bibliotecas.'),
}

def leyenda(items, start):
    return '<ol class="leyenda">%s</ol>' % ''.join('<li><span class="n">%d</span><b>%s</b>%s</li>' % (start + i, e(t), e(d)) for i, (t, d) in enumerate(items))

page(S, 'la-placa', 'La placa por delante y por detrás', P(
    'La micro:bit V2 mide unos 5 × 4 cm. En una cara están los elementos con los que interactuamos (pantalla, botones, logotipo) '
    'y en la otra, los componentes electrónicos.') +
    '<figure class="anat-fig">%s</figure>' % placa.anatomia() +
    P('Ahora, con la placa en la mano, busca cada parte numerada por delante y por detrás.') +
    '<div class="placa-dos"><div>%s</div><div>%s</div></div>' % (placa.frente(), placa.reves()) +
    h2('Anverso') + leyenda(placa.LEYENDA_FRENTE, 1) +
    h2('Reverso') + leyenda(placa.LEYENDA_REVES, 7) +
    h2('Entradas y salidas') +
    tabla(['Entradas (la placa recibe información)', 'Salidas (la placa actúa)'], [[
        ul(['Botones A y B', 'Logotipo táctil', 'Sensor de luz (los propios LED)', 'Sensor de temperatura', 'Acelerómetro (movimiento y gestos)', 'Brújula (magnetómetro)', 'Micrófono', 'Radio (recibir)', 'Pines de entrada']),
        ul(['Pantalla de 25 LED', 'Altavoz', 'Radio (enviar)', 'Pines de salida: luces, zumbadores, motores, servos…'])]]) +
    box('sabias', 'La pantalla también mide la luz', P('Los LED de la pantalla pueden funcionar al revés: en lugar de dar luz, detectan la que les llega. '
        'Por eso la micro:bit mide la luz ambiente sin tener un sensor de luz aparte.')),
    group=G1, icono='placa')

page(S, 'pines', 'Pines y conector de borde', P(
    'El borde dorado inferior es el <b>conector de borde</b>: tiene 25 contactos. Cinco de ellos son anillos grandes con agujero, pensados para '
    'conectar cables de cocodrilo o clavijas de 4 mm sin herramientas.') +
    placa.pines() +
    tabla(['Anillo', 'Para qué sirve', 'Ejemplo'], [
        ['<b>P0, P1, P2</b>', 'Entradas y salidas de uso general: digitales (0/1), analógicas (0-1023) y táctiles.', 'Encender un LED, leer un potenciómetro, hacer un piano de frutas'],
        ['<b>3V</b>', 'Salida de alimentación de unos 3 voltios para pequeños componentes.', 'Alimentar un sensor sencillo'],
        ['<b>GND</b>', 'Tierra (0 voltios). Todo circuito tiene que volver a GND.', 'La pata corta del LED, el cable de referencia del piano'],
    ]) +
    h2('Digital, analógico y táctil') +
    ul(['<b>Digital</b>: solo dos valores, 0 (apagado) o 1 (encendido). Sirve para LED, zumbadores y pulsadores.',
        '<b>Analógico</b>: un número de 0 a 1023. Al leer, mide cuánta tensión llega (por ejemplo, de un potenciómetro o un sensor de humedad). '
        'Al escribir, simula valores intermedios: un LED con más o menos brillo o un motor más o menos rápido.',
        '<b>Táctil</b>: detecta si tocas el pin con el dedo mientras sujetas GND con la otra mano. Así funcionan los pianos de frutas.']) +
    box('ojo', 'Para no estropear nada', ul([
        'No conectes 3V directamente con GND: es un cortocircuito.',
        'Pon siempre una resistencia (por ejemplo, de 220 Ω) en serie con un LED externo.',
        'La placa da poca corriente por sus pines. Los motores, las tiras de LED largas o varios servos necesitan una placa de expansión con alimentación propia.',
        'Los pines pequeños (P3 a P20) se usan con placas de expansión. Algunos están compartidos con la pantalla (P3, P4, P6, P7, P10) o con los botones (P5 y P11).'])),
    group=G1, icono='cocodrilo')

page(S, 'ficha-tecnica', 'Ficha técnica', P('Datos de la micro:bit V2 según la documentación técnica oficial (tech.microbit.org).') +
    tabla(['Elemento', 'Característica'], [
        ['Procesador', 'Nordic nRF52833, Arm Cortex-M4 de 32 bits a 64 MHz, 512 KB de memoria flash y 128 KB de RAM'],
        ['Pantalla', '25 LED rojos en matriz de 5 × 5 con brillo regulable; también miden la luz ambiente'],
        ['Botones', 'A y B programables en el anverso; botón de reinicio y reposo en el reverso'],
        ['Táctil', 'Logotipo táctil en el anverso y pines P0, P1 y P2'],
        ['Movimiento', 'Acelerómetro y magnetómetro (brújula) de 3 ejes en un mismo chip'],
        ['Sonido', 'Altavoz integrado y micrófono MEMS con LED indicador'],
        ['Temperatura', 'Sensor dentro del procesador: da una aproximación de la temperatura del aire'],
        ['Comunicación', 'Radio propia de 2,4 GHz entre micro:bits y Bluetooth 5.1 de baja energía'],
        ['Conexiones', 'Micro USB, conector de pilas (portapilas de 2 × AAA) y conector de borde de 25 contactos (5 anillos)'],
        ['Entradas analógicas', '6 pines con conversor de 10 bits (valores de 0 a 1023)'],
    ]) +
    box('sabias', 'Modo reposo', P('Si mantienes pulsado el botón del reverso, el LED rojo se apaga y la placa queda en reposo, gastando muy poca energía. '
        'Una pulsación corta la despierta y el programa vuelve a empezar.')),
    group=G1, icono='chip')

page(S, 'cargar-un-programa', 'Cargar un programa en la placa', P(
    'El programa se escribe en el ordenador, pero tiene que llegar a la placa para funcionar sin él. Cada editor lo hace a su manera.') +
    h2('MakeCode y Python: el archivo .hex') +
    ol(['Conecta la micro:bit con el cable USB. En el ordenador aparece una unidad llamada <b>MICROBIT</b>, como si fuera un pendrive.',
        'En MakeCode pulsa <b>Descargar</b>; en el editor de Python, <b>Guardar</b>. Se descarga un archivo con extensión <b>.hex</b>.',
        'Arrastra el archivo .hex a la unidad MICROBIT. El LED amarillo parpadea mientras se copia y el programa empieza solo.']) +
    P('Con <b>Chrome o Edge</b> es más rápido: conecta la placa al editor (en MakeCode, el botón de los tres puntos junto a Descargar › <b>Conectar dispositivo</b>; '
      'en Python, <b>Enviar a micro:bit</b>). A partir de ahí cada descarga se envía directamente a la placa.') +
    h2('MicroBlocks: programación en vivo') +
    ol(['Abre <a href="https://microblocks.fun/run/microblocks.html" target="_blank" rel="noopener">el editor de MicroBlocks</a> en Chrome o Edge, o instala la aplicación.',
        'La primera vez hay que instalar el firmware de MicroBlocks en la placa: menú del <b>engranaje</b> › <b>actualiza firmware de la placa</b>, elige micro:bit y sigue las instrucciones.',
        'Pulsa <b>Conecta</b>, elige <b>USB</b> y selecciona la placa. Cuando el botón se pone verde, ya estás en vivo.',
        'Haz clic en un bloque y se ejecuta al momento en la placa. Los programas se guardan en la micro:bit y siguen funcionando al desconectarla.']) +
    box('ojo', 'Si cambias de editor', P('El firmware de MicroBlocks y los programas de MakeCode o Python no conviven: al cargar un .hex de MakeCode se borra MicroBlocks, '
        'y para volver a MicroBlocks hay que reinstalar su firmware. Es un paso de un minuto, pero conviene saberlo antes de la clase.')) +
    box('idea', 'Sin placa', P('MakeCode y el editor de Python tienen <b>simulador</b>: una micro:bit en pantalla que responde a los botones, al movimiento y a los sensores. '
        'Es perfecto para empezar o para trabajar en casa.')),
    group=G1, icono='usb')

# ------------------------------------------------------------------ MakeCode
MC_CATS = [
    ('Básico', '#1E90FF', 'Mostrar números, textos, iconos y LED; pausas; <b>al iniciar</b> y <b>para siempre</b>.'),
    ('Entrada', '#D400D4', 'Botones, logotipo, gestos (agitar, inclinar…), luz, temperatura, sonido, brújula y aceleración.'),
    ('Música', '#E63022', 'Tonos, melodías y efectos de sonido por el altavoz.'),
    ('LED', '#5C2D91', 'Encender y apagar LED concretos con coordenadas x, y; gráficos de barras; brillo.'),
    ('Radio', '#E3008C', 'Enviar y recibir números, textos y pares nombre-valor entre placas del mismo grupo.'),
    ('Bucles', '#00AA00', 'Repetir, mientras, para… y cada cierto tiempo.'),
    ('Lógica', '#00A4A6', 'Si… entonces… si no; comparaciones; y, o, no; verdadero y falso.'),
    ('Variables', '#DC143C', 'Crear variables, fijar su valor y cambiarlo.'),
    ('Matemática', '#9400D3', 'Operaciones, números al azar, redondeo, valor absoluto, mínimo y máximo…'),
    ('Funciones', '#3455DB', '(Avanzado) Agrupar bloques con un nombre para reutilizarlos.'),
    ('Arreglos', '#E65722', '(Avanzado) Listas de valores.'),
    ('Texto', '#B8860B', '(Avanzado) Unir, cortar y comparar textos.'),
    ('Juego', '#007A4B', '(Avanzado) Sprites de un LED, puntuación, vidas y fin del juego.'),
    ('Imágenes', '#7600A8', '(Avanzado) Crear y desplazar imágenes y flechas.'),
    ('Pines', '#B22222', '(Avanzado) Escritura y lectura digital y analógica, servos y mapear valores.'),
    ('Serial', '#002050', '(Avanzado) Enviar datos al ordenador.'),
    ('Control', '#333333', '(Avanzado) Reiniciar, esperar, ejecutar en segundo plano.'),
]
_MC_EJ = '''let pulsaciones = 0
basic.showIcon(IconNames.Happy)
input.onButtonPressed(Button.A, function () {
    pulsaciones += 1
    basic.showNumber(pulsaciones)
})
basic.forever(function () {
    if (input.lightLevel() < 50) {
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    }
})'''

page(S, 'makecode', 'MakeCode', P(
    '<a href="https://makecode.microbit.org" target="_blank" rel="noopener">MakeCode</a> es el editor oficial de Microsoft para la micro:bit. Funciona en el navegador, '
    'no necesita cuenta y guarda los proyectos en el propio navegador. Para ponerlo en español: rueda dentada › <b>Idioma</b>.') +
    h2('Las partes del editor') +
    anatomia('makecode.jpg', 'Editor MakeCode para micro:bit en español', [
        (16, 30, 'Simulador', 'Una micro:bit virtual que ejecuta el programa al momento. Puedes pulsar sus botones y tocar su logotipo.'),
        (16, 57, 'Controles del simulador', 'Parar, reiniciar, depurar paso a paso, silenciar, captura y pantalla completa.'),
        (41, 11, 'Buscador', 'Escribe el nombre de un bloque para encontrarlo sin recorrer las categorías.'),
        (40, 45, 'Categorías', 'Los bloques ordenados por colores. Al pulsar una se abre su paleta.'),
        (42, 64, 'Extensiones', 'Añade bloques nuevos para robots, sensores y tiras de LED.'),
        (75, 50, 'Área de programación', 'Aquí se arrastran y encajan los bloques. Ya trae «al iniciar» y «para siempre».'),
        (44, 4, 'Bloques / JavaScript / Python', 'Cambia entre bloques y texto: el mismo programa en tres formas.'),
        (17, 95, 'Descargar', 'Crea el archivo .hex o lo envía directamente a la placa conectada.'),
        (45, 95, 'Nombre y guardar', 'Ponle nombre al proyecto antes de descargarlo.'),
        (92, 95, 'Deshacer y zoom', 'Deshacer, rehacer y cambiar el tamaño de los bloques.'),
    ], 'Captura del editor MakeCode (makecode.microbit.org) en español.') +
    h2('Los bloques que mueven el programa') +
    P('Todo programa empieza por un bloque con forma de «boca»: <b>al iniciar</b> se ejecuta una vez al encender la placa; <b>para siempre</b> se repite sin parar; '
      'y los eventos, como <b>al presionarse el botón A</b>, se ejecutan cada vez que pasa algo. Este ejemplo usa los tres:') +
    makecode.blocks(_MC_EJ) +
    h2('Categorías') +
    tabla(['Categoría', '¿Qué contiene?'], [['<span class="cat" style="--c:%s">%s</span>' % (c, n), d] for n, c, d in MC_CATS]) +
    box('idea', 'Truco', P('Haz clic derecho sobre un bloque y elige <b>Ayuda</b> para ver su explicación. Con <b>Duplicar</b> copias un bloque con todo lo que lleva dentro.')),
    group=G2, icono='bloques')

# ------------------------------------------------------------------ MicroBlocks
MB_CATS = [
    ('Salida', 'Output', 'Pantalla de LED, texto en movimiento, LED integrado.', "'[display:mbDisplay]' 4685802"),
    ('Entrada', 'Input', 'Botones, cronómetro, sensores de la placa (inclinación, luz, temperatura…).', "sayIt (buttonA)"),
    ('Pines', 'Pins', 'Leer y escribir pines digitales y analógicos.', "digitalWriteOp 0 true"),
    ('Control', 'Control', 'Eventos (al empezar, cuando se pulse el botón…), bucles, esperas, si…', "whenStarted"),
    ('Operadores', 'Operators', 'Operaciones, comparaciones, azar, y/o/no.', "sayIt (random 1 10)"),
    ('Variables', 'Variables', 'Crear variables, asignarles valor y aumentarlas.', "puntos += 1"),
    ('Datos', 'Data', 'Listas y textos.', "sayIt ('[data:join]' 'micro' 'bit')"),
    ('Mis bloques', 'My Blocks', 'Bloques propios hechos por ti.', None),
]
_MB_EJ = '''whenStarted
forever {
  '[display:mbDisplay]' 4685802
  waitMillis 500
  '[display:mbDisplayOff]'
  waitMillis 500
}
---
whenButtonPressed 'A'
scroll_text 'Hola'
---
whenCondition (('[display:lightLevel]') < 10)
'play tone' 'nt;c' 1 200'''

page(S, 'microblocks', 'MicroBlocks', P(
    '<a href="https://microblocks.fun" target="_blank" rel="noopener">MicroBlocks</a> es un lenguaje de bloques libre y gratuito, parecido a Scratch, que funciona con la micro:bit '
    'y con muchas otras placas. Se usa en el navegador (Chrome o Edge) o como aplicación para Windows, macOS, Linux y Chromebook.') +
    anatomia('microblocks.jpg', 'Editor de MicroBlocks en español con el programa de la sirena', [
        (5, 22, 'Categorías', 'Salida, Entrada, Pines, Control, Operadores, Variables, Datos y Mis bloques, cada una con su color.'),
        (8, 51, 'Bibliotecas', 'Las bibliotecas cargadas (aquí Pantalla LED y Tonos) y el botón «Añadir biblioteca».'),
        (26, 30, 'Paleta', 'Los bloques de la categoría elegida. Se arrastran al área de guiones.'),
        (62, 42, 'Área de guiones', 'Aquí se montan los programas. Haz clic en un guion para ejecutarlo en la placa.'),
        (17, 3, 'Idioma, ajustes y archivo', 'El globo cambia el idioma; el engranaje tiene la actualización de firmware; la hoja abre y guarda proyectos.'),
        (76, 3, 'Gráfica', 'Muestra en directo los valores enviados con el bloque «añade al gráfico».'),
        (85, 3, 'Conecta', 'Conecta la placa por USB o Bluetooth. Se pone verde al conectar.'),
        (96, 3, 'Iniciar y parar', 'Pone en marcha todos los guiones «al empezar» o los detiene.'),
    ], 'Captura de MicroBlocks (microblocks.fun) con el proyecto de la práctica «La sirena» abierto desde este material.') +
    h2('Sus cuatro ideas clave') +
    '<div class="tres">' + ''.join('<div>%s<h3>%s</h3><p>%s</p></div>' % (icon(i, 26), t, d) for i, t, d in [
        ('rayo', 'En vivo', 'No hay que descargar nada: cada cambio se envía a la placa al instante. Haz clic en un bloque y se ejecuta.'),
        ('engranaje', 'Multitarea', 'Varios guiones funcionan a la vez sin estorbarse: uno anima la pantalla mientras otro vigila un botón.'),
        ('bateria', 'Autónomo', 'El programa queda guardado en la placa y sigue funcionando al desconectarla del ordenador.'),
        ('caja', 'Portátil', 'Los mismos bloques sirven para otras placas, como Calliope mini o ESP32.'),
    ]) + '</div>' +
    h2('Un ejemplo con tres guiones a la vez') +
    P('El primero hace latir un corazón, el segundo escribe «Hola» al pulsar A y el tercero pita cuando tapas la pantalla. Funcionan a la vez:') +
    mbk.render(_MB_EJ) +
    h2('Categorías') +
    tabla(['Categoría', '¿Qué contiene?', 'Ejemplo'], [
        ['<span class="cat" style="--c:%s">%s</span>' % (mbk.COLOR[k], n), d, mbk.render(ex) if ex else ''] for n, k, d, ex in MB_CATS]) +
    h2('Bibliotecas') +
    P('Muchos bloques están en <b>bibliotecas</b>. Con la micro:bit se cargan solas las básicas (como <b>Pantalla LED</b>), y el resto se añade con '
      '<b>Añadir biblioteca</b>, bajo la lista de categorías. Las más útiles con la micro:bit son <b>Tone</b> (notas musicales), <b>Radio</b>, <b>Microphone</b> (sonido y palmadas), '
      '<b>TouchPin</b> (logotipo y pines táctiles), <b>Servo</b> y <b>NeoPixel</b>. Los proyectos de este material ya llevan dentro las bibliotecas que necesitan.') +
    box('idea', 'Ver los valores en directo', P('El bloque <b>di</b> muestra un globo con el valor que le pongas, y <b>gráfica</b> dibuja los datos de un sensor en tiempo real. '
        'Son perfectos para explorar sensores antes de programar.')),
    group=G2, icono='bloques2')

# ------------------------------------------------------------------ Python
_PY_EJ = '''# Las importaciones van arriba
from microbit import *

pulsaciones = 0
display.show(Image.HAPPY)

# Lo que va dentro de while True se repite para siempre
while True:
    if button_a.was_pressed():
        pulsaciones += 1
        display.scroll(pulsaciones)
    if display.read_light_level() < 50:
        display.show(Image.ASLEEP)'''

page(S, 'python', 'Python', P(
    'El <a href="https://python.microbit.org" target="_blank" rel="noopener">editor de Python</a> de la Micro:bit Educational Foundation usa <b>MicroPython</b>, '
    'una versión de Python para placas pequeñas. Está en español, tiene <b>simulador</b> y, en el panel izquierdo, tres ayudas: <b>Referencia</b> (explicaciones con ejemplos que se '
    'pueden arrastrar al código), <b>Ideas</b> (proyectos de ejemplo) y <b>API</b> (todas las instrucciones).') +
    anatomia('python.jpg', 'Editor de Python para micro:bit en español', [
        (3.5, 40, 'Referencia, Ideas y API', 'Ayudas con ejemplos que se arrastran al código, proyectos de ejemplo y todas las instrucciones.'),
        (20, 4, 'Nombre del proyecto', 'Haz clic para cambiarlo.'),
        (38, 30, 'Editor de código', 'Aquí se escribe el programa. Los números de la izquierda son las líneas.'),
        (86, 18, 'Simulador', 'Ejecuta el programa en una micro:bit virtual.'),
        (86, 70, 'Sensores del simulador', 'Gestos, luz, temperatura, brújula, sonido, botones, pines y radio para probar sin placa.'),
        (19, 95, 'Enviar a micro:bit', 'Envía el programa a la placa conectada por USB (Chrome o Edge).'),
        (60, 95, 'Guardar y Abrir…', 'Guarda el programa como .hex o .py y abre archivos guardados.'),
    ], 'Captura del editor de Python (python.microbit.org) en español.') +
    h2('Cómo es un programa') +
    '<pre class="code py"><code>%s</code></pre>' % py_html(_PY_EJ) +
    ul(['<code>from microbit import *</code> carga las instrucciones de la placa. Va siempre al principio.',
        'Lo que está fuera del bucle se ejecuta una vez, como <b>al iniciar</b>.',
        '<code>while True:</code> repite para siempre lo que tiene debajo, como <b>para siempre</b>.',
        'La <b>sangría</b> (los espacios al principio de la línea) indica qué instrucciones van dentro de un bucle o de un <code>if</code>. Si se descoloca, el programa falla.']) +
    h2('Instrucciones más usadas') +
    tabla(['Para…', 'Python', 'Bloque equivalente en MakeCode'], [
        ['Mostrar un número o texto', '<code>display.scroll(7)</code>', 'mostrar número / mostrar cadena'],
        ['Mostrar un icono', '<code>display.show(Image.HEART)</code>', 'mostrar ícono'],
        ['Esperar', '<code>sleep(1000)</code>', 'pausa (ms)'],
        ['Botón pulsado', '<code>button_a.was_pressed()</code>', 'al presionarse el botón A'],
        ['Logotipo tocado', '<code>pin_logo.is_touched()</code>', 'el logotipo está pulsado'],
        ['Gesto', '<code>accelerometer.was_gesture("shake")</code>', 'si agitar'],
        ['Luz y temperatura', '<code>display.read_light_level()</code>, <code>temperature()</code>', 'nivel de luz, temperatura (°C)'],
        ['Nivel de sonido', '<code>microphone.sound_level()</code>', 'nivel de sonido'],
        ['Número al azar', '<code>random.randint(1, 6)</code> (con <code>import random</code>)', 'escoger al azar de 1 a 6'],
        ['Sonido', '<code>music.play(music.BA_DING)</code> (con <code>import music</code>)', 'reproduce…'],
        ['Radio', '<code>radio.send("hola")</code>, <code>radio.receive()</code> (con <code>import radio</code>)', 'radio enviar cadena, al recibir radio'],
        ['Pines', '<code>pin0.write_digital(1)</code>, <code>pin1.read_analog()</code>', 'escritura digital, lectura analógica'],
    ]) +
    box('ojo', 'Errores típicos en Python', ul(['Olvidar los dos puntos <code>:</code> al final de <code>while</code>, <code>if</code>, <code>for</code> o <code>def</code>.',
        'Mezclar espacios y tabuladores en la sangría.', 'Escribir <code>Button_a</code> en lugar de <code>button_a</code>: Python distingue mayúsculas y minúsculas.',
        'Usar <code>random</code>, <code>music</code> o <code>radio</code> sin importarlos antes.'])),
    group=G2, icono='codigo')

page(S, 'extensiones', 'Extensiones y bibliotecas', P(
    'Los editores traen los bloques de la placa, pero cuando conectamos un robot, una tira de luces o un kit hacen falta bloques nuevos. '
    'En MakeCode se llaman <b>extensiones</b>; en MicroBlocks, <b>bibliotecas</b>; en Python, <b>módulos</b>.') +
    h2('Añadir una extensión en MakeCode') +
    ol(['Pulsa <b>Extensiones</b>, al final de la lista de categorías.',
        'Escribe el nombre en el buscador (por ejemplo, <i>neopixel</i>, <i>servo</i> o <i>cutebot</i>) o pega la dirección de GitHub que indique el fabricante.',
        'Elige la extensión. Aparece una categoría nueva con sus bloques. La extensión se guarda dentro del proyecto.']) +
    tabla(['Extensión', 'Para qué', 'Dónde se usa en este material'], [
        ['neopixel', 'Tiras y anillos de LED de colores', 'Talleres y Para celebrar'],
        ['servo', 'Servomotores', 'Talleres'],
        ['cutebot', 'Robot Cutebot de ELECFREAKS', 'Taller Cutebot'],
        ['maqueen / MaqueenPlusV2', 'Robots Maqueen de DFRobot', 'Talleres Maqueen'],
        ['wukong', 'Placa WuKong (Wonder Building Kit)', 'Taller Wonder Building Kit'],
        ['iot-environment-kit', 'Sensores de los kits de ELECFREAKS (humedad del suelo, DHT11…)', 'Taller Smart Agriculture Kit'],
    ]) +
    box('ojo', 'Solo extensiones de confianza', P('Usa las extensiones que aparecen en el buscador o las que indica el fabricante de tu kit en su documentación. '
        'Si una extensión no funciona, revisa que es la de tu modelo: hay robots con varias versiones y cada una tiene la suya.')) +
    h2('Añadir una biblioteca en MicroBlocks') +
    P('Pulsa <b>Añadir biblioteca</b> bajo las categorías y elige una de las carpetas (Sensores, Robots, Kits y placas…). Las bibliotecas también se pueden arrastrar desde un archivo .ubl. '
      'Hay bibliotecas para Cutebot y Maqueen, entre otras.') +
    h2('Módulos de Python') +
    P('En Python se escribe <code>import</code> al principio: <code>import music</code>, <code>import radio</code>, <code>import neopixel</code>, <code>import random</code>. '
      'La pestaña <b>API</b> del editor lista todos los módulos disponibles.'),
    group=G2, icono='pieza')
