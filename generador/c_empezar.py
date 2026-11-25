# -*- coding: utf-8 -*-
from common import page, P, ul, ol, box, tabla, h2, h3, kbd, panel_python, py_html, e
import makecode, mbk
from iconos import icon

S = 'empezar'

page(S, 'que-es-programar', '¿Qué es programar?', P(
    'Programar es <b>dar instrucciones a una máquina</b> para que haga lo que queremos. Las instrucciones tienen que estar '
    'en el orden correcto y ser tan claras que no admitan dudas: la máquina no adivina, hace exactamente lo que le decimos.',
    'Una lista ordenada de pasos para resolver un problema se llama <b>algoritmo</b>. Una receta de cocina, las instrucciones para montar '
    'un mueble o el camino de casa al colegio son algoritmos. Cuando escribimos un algoritmo en un lenguaje que entiende un ordenador, '
    'tenemos un <b>programa</b>.') +
    h2('Entrada, proceso y salida') +
    P('Casi todos los programas siguen el mismo esquema: recogen información (<b>entrada</b>), la procesan siguiendo unas reglas (<b>proceso</b>) '
      'y producen un resultado (<b>salida</b>). Con la micro:bit lo vemos enseguida:') +
    tabla(['', 'En la micro:bit', 'Ejemplo'], [
        ['%s <b>Entrada</b>' % icon('pulsador', 18), 'Botones, logotipo táctil, sensores de luz, temperatura, movimiento y sonido, radio, pines', 'Pulso el botón A'],
        ['%s <b>Proceso</b>' % icon('chip', 18), 'El procesador sigue el programa: decide, cuenta, compara, repite…', 'Sumo 1 al contador'],
        ['%s <b>Salida</b>' % icon('led', 18), 'Pantalla de LED, altavoz, radio, pines (luces, motores, servos…)', 'Muestro el número'],
    ]) +
    h2('Tres ideas que aparecen en todos los programas') +
    ul(['<b>Secuencia</b>: las instrucciones se ejecutan una detrás de otra, en orden.',
        '<b>Repetición (bucles)</b>: repetir instrucciones un número de veces o para siempre.',
        '<b>Decisión (condicionales)</b>: hacer una cosa u otra según se cumpla una condición.']) +
    P('A estas tres se suman los <b>eventos</b> (reaccionar cuando pasa algo, como pulsar un botón) y las <b>variables</b> '
      '(guardar datos que cambian, como una puntuación). Con estas cinco piezas se construyen desde un dado electrónico hasta un robot.') +
    box('docente', 'Actividad desenchufada: el robot de clase', P(
        'Antes de usar la placa, una alumna hace de «robot» y solo puede obedecer órdenes como <i>avanza 1 paso</i>, <i>gira a la derecha</i> o '
        '<i>repite 3 veces</i>. El resto escribe en la pizarra el programa para llevarla hasta la puerta. Cuando el robot choca, el grupo '
        'busca el error y lo corrige: acaban de <b>depurar</b> su primer programa.')),
    icono='lista')

page(S, 'por-que-microbit', '¿Por qué micro:bit?', P(
    'La <b>micro:bit</b> es un ordenador muy pequeño, del tamaño de una tarjeta, creado para aprender a programar. Fue diseñada por la BBC '
    'y hoy la desarrolla la Micro:bit Educational Foundation, una organización sin ánimo de lucro. Usamos la <b>versión 2 (V2)</b>, que añade '
    'altavoz, micrófono y logotipo táctil a la primera versión.') +
    h2('Lo que la hace especial para el aula') +
    '<div class="tres">' + ''.join('<div>%s<h3>%s</h3><p>%s</p></div>' % (icon(i, 28), t, d) for i, t, d in [
        ('led', 'Resultado inmediato', 'Lo que programas se ve, se oye o se mueve en la placa en segundos. El error también se ve, y eso ayuda a aprender.'),
        ('sensor', 'Todo incluido', 'Pantalla, botones, sensores de luz, temperatura, movimiento y sonido, altavoz, brújula y radio sin conectar nada.'),
        ('bloques', 'Varios lenguajes', 'Se programa con bloques (MakeCode, MicroBlocks) y con texto (Python, JavaScript). Se crece sin cambiar de placa.'),
        ('antena', 'Trabajo en grupo', 'Las placas se comunican por radio: juegos multijugador, votaciones o mensajes entre equipos.'),
        ('cocodrilo', 'Abierta al mundo real', 'Con cables de cocodrilo y kits se conectan luces, motores, sensores y robots.'),
        ('rayo', 'Sin instalar nada', 'Los editores funcionan en el navegador. MakeCode tiene simulador: se puede empezar incluso sin placa.'),
    ]) + '</div>' +
    h2('Computación física') +
    P('Con la micro:bit el programa sale de la pantalla y actúa sobre objetos reales. A esto se le llama <b>computación física</b>: el alumnado '
      'diseña, construye, prueba y mejora, y conecta la programación con la ciencia, la tecnología, las matemáticas, el arte o la música.') +
    box('sabias', '¿V1 o V2?', P('Se distinguen por el borde inferior: la V2 tiene unas <b>muescas</b> entre los contactos dorados y la V1 lo tiene recto. '
        'La V2 tiene además el logotipo dorado táctil y el LED del micrófono. Casi todas las prácticas funcionan en las dos, '
        'salvo las que usan altavoz, micrófono o logotipo.')),
    icono='placa')

# ------------------------------------------------------------------ bloques y texto
_MC = '''input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Heart)
    basic.pause(1000)
    basic.clearScreen()
})'''
_MB = '''whenButtonPressed 'A'
'[display:mbDisplay]' 4685802
waitMillis 1000
'[display:mbDisplayOff]\''''
_PY = '''from microbit import *

while True:
    if button_a.was_pressed():
        display.show(Image.HEART)
        sleep(1000)
        display.clear()'''

page(S, 'bloques-y-texto', 'Bloques y texto', P(
    'Hay dos grandes formas de programar: <b>con bloques</b>, encajando piezas como en un puzle, y <b>con texto</b>, escribiendo las instrucciones. '
    'Las dos sirven para lo mismo; cambia la forma de escribir. Este es el mismo programa (al pulsar A aparece un corazón durante un segundo) en los tres editores:') +
    '<div class="comparar"><div><h4>MakeCode · bloques</h4>%s</div><div><h4>MicroBlocks · bloques</h4>%s</div><div><h4>Python · texto</h4><pre class="code py"><code>%s</code></pre></div></div>' % (
        makecode.blocks(_MC), mbk.render(_MB), py_html(_PY)) +
    h2('Ventajas de cada forma') +
    tabla(['', 'Bloques', 'Texto'], [
        ['Errores de escritura', 'No hay: los bloques solo encajan si tienen sentido.', 'Una coma o una sangría mal puesta impiden que funcione.'],
        ['Qué recordar', 'Nada: todos los bloques están a la vista en la paleta.', 'Hay que conocer las instrucciones (o consultarlas).'],
        ['Programas largos', 'Ocupan mucho espacio en pantalla.', 'Son compactos, fáciles de copiar, buscar y compartir.'],
        ['Edad recomendada', 'Desde 6-7 años.', 'Desde 11-12 años, mejor tras pasar por los bloques.'],
    ]) +
    h2('Los tres editores de este material') +
    tabla(['', 'MakeCode', 'MicroBlocks', 'Python'], [
        ['Lenguaje', 'Bloques, con paso a JavaScript y Python de MakeCode', 'Bloques', 'Texto (MicroPython)'],
        ['Dónde', '<a href="https://makecode.microbit.org" target="_blank" rel="noopener">makecode.microbit.org</a>', '<a href="https://microblocks.fun" target="_blank" rel="noopener">microblocks.fun</a> (web o aplicación)', '<a href="https://python.microbit.org" target="_blank" rel="noopener">python.microbit.org</a>'],
        ['Cómo llega el programa a la placa', 'Se descarga un archivo .hex y se pasa a la placa (o se envía directamente desde Chrome o Edge)', 'En vivo por USB o Bluetooth: cada cambio se envía al momento', 'Se descarga un archivo .hex o se envía desde Chrome o Edge'],
        ['Simulador', 'Sí, integrado', 'No para la micro:bit (tiene una placa virtual de práctica, Boardie)', 'Sí, integrado'],
        ['Punto fuerte', 'Muy completo, con tutoriales y cientos de extensiones', 'Programación en vivo y varias tareas a la vez; sirve para muchas placas', 'Lenguaje real y muy usado; ideal para dar el salto en ESO'],
        ['Recomendado', 'Primaria y ESO', 'Primaria y ESO', 'ESO'],
    ]) +
    box('idea', 'Nuestra propuesta', P('Empezar con bloques y, cuando el grupo domine secuencias, bucles, condicionales y variables, mirar el código en Python de las mismas prácticas. '
        'En MakeCode puedes pasar de bloques a texto con la pestaña <b>JavaScript</b> o <b>Python</b> de la parte superior, y ver cómo cada bloque se convierte en una línea.')),
    icono='bloques')

page(S, 'pensamiento-computacional', 'Pensamiento computacional', P(
    'El <b>pensamiento computacional</b> es una forma de resolver problemas que usan los programadores pero que sirve para cualquier materia: '
    'partir el problema, buscar lo que se repite, quedarse con lo importante y escribir los pasos de la solución. '
    'En España, la LOMLOE lo incluye en Matemáticas de Primaria y en Tecnología y Digitalización de ESO.') +
    tabla(['Habilidad', 'En qué consiste', 'Con la micro:bit'], [
        ['%s <b>Descomposición</b>' % icon('puzle', 18), 'Dividir un problema grande en partes pequeñas.', 'Un podómetro: detectar el paso, contar, mostrar el número, reiniciar.'],
        ['%s <b>Patrones</b>' % icon('matriz', 18), 'Encontrar lo que se repite para no hacerlo dos veces.', 'Las cuatro flechas de una brújula se programan igual: solo cambia el ángulo.'],
        ['%s <b>Abstracción</b>' % icon('lupa', 18), 'Quedarse con lo importante e ignorar los detalles.', 'Para un termómetro no importa cómo mide el chip, sino qué número da.'],
        ['%s <b>Algoritmos</b>' % icon('lista', 18), 'Escribir los pasos ordenados de la solución.', 'Si la luz baja de 50, enciende el LED; si no, apágalo.'],
        ['%s <b>Depuración</b>' % icon('salvavidas', 18), 'Encontrar y corregir errores probando.', 'El dado siempre saca 6: revisamos el bloque de número al azar.'],
        ['%s <b>Evaluación</b>' % icon('check', 18), 'Comprobar si la solución funciona y se puede mejorar.', '¿El juego es justo? ¿Va demasiado rápido para Primaria?'],
    ]) +
    h2('Una forma de trabajar: usar, modificar, crear') +
    ol(['<b>Usar</b>: probar un programa que ya funciona y explicar qué hace.',
        '<b>Modificar</b>: cambiar números, iconos o sonidos y predecir qué pasará antes de probarlo.',
        '<b>Crear</b>: diseñar un programa propio a partir de lo aprendido.']) +
    P('Las prácticas de este material siguen ese camino: cada una tiene un objetivo, pasos guiados, pistas, una solución para comparar y un <b>¿Y si…?</b> para crear algo nuevo.') +
    box('docente', 'Programación en parejas', P('Funciona muy bien que trabajen de dos en dos con roles que se cambian cada 10 minutos: el <b>piloto</b> maneja el ratón y el '
        '<b>copiloto</b> lee el paso a paso, propone ideas y revisa. Así todo el grupo piensa y nadie se queda mirando.')),
    icono='cerebro')

page(S, 'como-usar', 'Cómo usar este material', P(
    'El material está organizado de menos a más. No hace falta seguirlo entero: cada docente puede elegir las prácticas que encajen con su grupo.') +
    tabla(['Apartado', 'Para qué', 'Etapa'], [
        ['<a href="../conoce/index.html">Conoce micro:bit</a>', 'Conocer la placa y los editores', 'Todas'],
        ['<a href="../comenzamos/index.html">Comenzamos</a>', '30 prácticas guiadas en 6 bloques', 'Primaria (bloques 1-4) y ESO (todas)'],
        ['<a href="../experto/index.html">Modo experto</a>', 'Juegos, retos, cables de cocodrilo y sensores', '5.º-6.º de Primaria y ESO'],
        ['<a href="../talleres/index.html">Talleres</a>', 'Proyectos tipo y kits de robótica', '5.º-6.º de Primaria y ESO'],
        ['<a href="../celebrar/index.html">Para celebrar</a>', 'Actividades cortas para fechas especiales', 'Todas'],
    ]) +
    h2('Qué significa cada marca') +
    ul(['<b>Dificultad</b> ★☆☆ a ★★★: lo exigente que es la práctica dentro de su bloque.',
        '<b>Etapa</b>: Primaria 6-9, Primaria 10-12 o ESO. Es orientativa: una práctica de Primaria sirve como calentamiento en ESO.',
        '<b>Conceptos</b>: las ideas de programación que se trabajan (bucles, variables, eventos…).']) +
    h2('Material necesario') +
    ul(['Una micro:bit V2 por pareja, con su cable USB (mejor si es de datos, no solo de carga).',
        'Un portapilas con dos pilas AAA para usarla lejos del ordenador.',
        'Un ordenador con Chrome o Edge. MakeCode y Python también funcionan en tabletas con su aplicación o navegador.',
        'Para el modo experto: cables de cocodrilo, algunos LED, un zumbador y sensores sencillos (se indica en cada proyecto).']) +
    box('ojo', 'Cuidado con la placa', ul(['Cógela por los bordes y evita tocar los componentes con los dedos mojados.',
        'No la pongas sobre superficies metálicas: puede hacer cortocircuito por detrás.',
        'No conectes los pines 3V y GND entre sí con un cable.'])),
    icono='libro')
