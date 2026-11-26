# -*- coding: utf-8 -*-
from common import page, P, ul, ol, box, tabla, h2, e
from iconos import icon

S = 'saber'

def enlaces(items):
    return '<div class="enlaces">%s</div>' % ''.join(
        '<a href="%s" target="_blank" rel="noopener"><b>%s %s</b><span>%s</span></a>' % (u, icon('enlace', 16), e(t), d) for t, u, d in items)

page(S, 'problemas-frecuentes', 'Problemas frecuentes', tabla(['Problema', 'Qué hacer'], [
    ['No aparece la unidad MICROBIT', 'Prueba otro cable: muchos cables solo cargan y no transmiten datos. Prueba otro puerto USB.'],
    ['La pantalla muestra una cara triste y un número', 'Es un error del programa (por ejemplo, 020 = falta de memoria). Revisa el programa y vuelve a cargarlo.'],
    ['El programa no hace nada', 'Comprueba que los bloques están dentro de un evento (al iniciar, para siempre…). Un bloque suelto no se ejecuta.'],
    ['MakeCode no conecta por USB', 'Usa Chrome o Edge y pulsa «Conectar dispositivo». Si no aparece la placa, actualiza su firmware siguiendo las instrucciones de microbit.org.'],
    ['MicroBlocks no conecta', 'Instala su firmware en la placa (engranaje › actualiza firmware de la placa). Cierra otras pestañas que usen la placa.'],
    ['Después de usar MicroBlocks, MakeCode «no va»', 'Simplemente carga un .hex de MakeCode: sustituye el firmware de MicroBlocks.'],
    ['No suena nada', 'Comprueba que es una V2 y que el volumen no está a 0. En MakeCode, revisa «configurar altavoz interno».'],
    ['La radio no funciona', 'Las dos placas deben estar en el mismo grupo y programadas con el mismo editor. Una placa no recibe sus propios mensajes.'],
    ['La brújula pide «inclinar»', 'Es la calibración: inclina la placa hasta llenar la pantalla de LED.'],
    ['Las tildes y la ñ no salen', 'La pantalla solo tiene letras sin acento. Escribe sin tildes ni eñes.'],
]), icono='salvavidas')

page(S, 'glosario', 'Glosario', tabla(['Término', 'Significado'], [
    ['Algoritmo', 'Lista ordenada de pasos para resolver un problema.'],
    ['Bucle', 'Instrucciones que se repiten un número de veces o para siempre.'],
    ['Condicional', 'Instrucción que elige qué hacer según se cumpla o no una condición (si… entonces… si no).'],
    ['Depurar', 'Buscar y corregir errores de un programa.'],
    ['Evento', 'Algo que ocurre (pulsar un botón, agitar la placa) y que pone en marcha un trozo de programa.'],
    ['Variable', 'Espacio con nombre donde se guarda un dato que puede cambiar.'],
    ['Lista', 'Variable que guarda varios datos ordenados.'],
    ['Sensor', 'Componente que mide algo del entorno: luz, temperatura, movimiento, sonido…'],
    ['Actuador', 'Componente que actúa sobre el entorno: LED, altavoz, motor, servo…'],
    ['Digital / analógico', 'Digital: solo dos valores (0 o 1). Analógico: muchos valores intermedios (0 a 1023 en la micro:bit).'],
    ['Umbral', 'Valor límite a partir del cual el programa toma una decisión.'],
    ['Calibrar', 'Ajustar un sensor o un umbral comparando con medidas reales.'],
    ['Firmware', 'Programa interno de la placa que le permite entender a un editor.'],
    ['.hex / .ubp / .py', 'Archivos de programa de MakeCode y Python (.hex), de MicroBlocks (.ubp) y de Python (.py).'],
    ['Extensión / biblioteca', 'Conjunto de bloques nuevos que se añade al editor para usar un componente o un kit.'],
    ['GND', 'Tierra, 0 voltios: el punto al que vuelve la corriente de todo circuito.'],
]), icono='lista')

page(S, 'evaluacion', 'Evaluación', P('Rúbrica orientativa para evaluar prácticas y proyectos. Puede usarse también como autoevaluación.') +
    tabla(['Criterio', 'Inicial', 'En desarrollo', 'Conseguido', 'Excelente'], [
        ['Funcionamiento', 'No funciona', 'Funciona en parte', 'Cumple el objetivo', 'Cumple el objetivo y una ampliación'],
        ['Programación', 'Bloques sueltos o desordenados', 'Usa eventos y secuencias', 'Usa bucles, condicionales y variables', 'Código claro, sin repeticiones, con nombres significativos'],
        ['Depuración', 'No localiza los errores', 'Localiza errores con ayuda', 'Localiza y corrige sus errores', 'Ayuda a otros a depurar'],
        ['Montaje (si lo hay)', 'Conexiones incorrectas', 'Funciona con ayuda', 'Montaje correcto y seguro', 'Montaje cuidado, con explicación del circuito'],
        ['Comunicación', 'No explica su trabajo', 'Explica qué hace', 'Explica cómo funciona', 'Explica decisiones y mejoras posibles'],
        ['Trabajo en pareja', 'No colabora', 'Colabora a ratos', 'Alterna roles y colabora', 'Lidera y facilita el trabajo del equipo'],
    ]), icono='check')

OFICIAL = [
    ('micro:bit (español)', 'https://microbit.org/es-es/', 'Web oficial: guía de inicio, características de la placa y proyectos.'),
    ('Proyectos «Make it: code it»', 'https://microbit.org/es-es/projects/make-it-code-it/', 'Proyectos rápidos para todas las edades, filtrables por nivel, editor y sensor.'),
    ('Lecciones para docentes', 'https://microbit.org/teach/lessons/', 'Unidades didácticas por edades (7-16 años) y retos de diseño.'),
    ('Destacados para docentes', 'https://microbit.org/teach/featured/', 'Novedades, cursos y webinarios para el profesorado.'),
    ('MakeCode para micro:bit', 'https://makecode.microbit.org', 'Editor de bloques con simulador, tutoriales y extensiones.'),
    ('Editor de Python', 'https://python.microbit.org', 'MicroPython con simulador, referencia, ideas y API.'),
    ('MicroBlocks', 'https://microblocks.fun', 'Editor de bloques en vivo. Su sección «Get started» explica la instalación.'),
    ('Documentación técnica', 'https://tech.microbit.org', 'Hardware, pines y especificaciones de la placa.'),
]
GUIAS = [
    ('Guía de trabajo para micro:bit (F. Coca)', 'https://fgcoca.github.io/Guia-de-trabajo-para-microbit/guias/mblocks/', 'Guía en español de MicroBlocks, MakeCode y Python, con actividades.'),
    ('Guía de micro:bit paso a paso (BricoGeek)', 'https://lab.bricogeek.com/tutorial/guia-de-microbit-paso-a-paso-para-principiantes', 'Tutorial para principiantes con las funciones de la placa y la robótica con Maqueen.'),
    ('Proyectos en Instructables', 'https://www.instructables.com/search/?q=microbit&projects=all', 'Miles de proyectos de la comunidad (en inglés) para inspirarse.'),
    ('Wiki de ELECFREAKS', 'https://wiki.elecfreaks.com/en/microbit/', 'Guías y casos de Cutebot, Wonder Building Kit, Smart Agriculture Kit y más.'),
    ('Wiki de DFRobot', 'https://wiki.dfrobot.com', 'Documentación de Maqueen, Maqueen Plus y sus sensores.'),
]
JAJULCA = [
    ('TecnoJajulca', 'https://jajulca.eu', 'Portal de recursos de tecnología, robótica y programación de Eufrasio Cabrera.'),
    ('Programamos la microbit', 'https://jajulca.eu/microbit/', 'Retos del IES Aricel: gráficos, sensores, juegos, radio, estación meteorológica…'),
    ('Retos con Maqueen', 'http://jajulca.net/maqueen/index.html', 'Motores, neopíxeles, ultrasonidos, mando IR, seguidor de línea y más.'),
    ('Robótica y programación', 'http://jajulca.net/computacionyrobotica/index.html', 'Ejercicios y manuales de micro:bit, Maqueen con MicroBlocks, Scratch y Arduino.'),
    ('Artículos sobre micro:bit', 'https://jajulca.eu/category/microbit/', 'Entradas del blog con proyectos de micro:bit.'),
]
PEDRO = [
    ('Retos de micro:bit con MicroBlocks', 'https://pedroruizf.github.io/retos_microbit_microblocks/index.html', 'Retos con animaciones, pulsadores, sensores, servos y radio, con sus ficheros de programa.'),
    ('Retos con robot Maqueen', 'https://pedroruizf.github.io/maqueen_retos/', 'Motores, neopíxeles, ultrasonidos, mando IR, seguidor de línea, evita-obstáculos y control por radio.'),
    ('Programación y robótica', 'https://github.com/pedroruizf/programacionyrobotica', 'Repositorio con materiales de programación y robótica.'),
    ('GitHub de Pedro Ruiz', 'https://github.com/pedroruizf', 'Todos sus recursos educativos publicados.'),
]
CREDITOS = ul([
    '<b>Bloques de MakeCode</b>: las imágenes las dibuja el propio editor MakeCode de Microsoft (makecode.microbit.org) a partir del código de cada práctica.',
    '<b>MicroBlocks</b>: los nombres de los bloques salen de su traducción oficial al español y los proyectos incluyen sus bibliotecas oficiales, distribuidas con licencia MPL 2.0.',
    '<b>Capturas de los editores</b>: MakeCode, MicroBlocks y el editor de Python de la Micro:bit Educational Foundation, hechas con fines educativos para explicar su uso.',
    '<b>Datos técnicos de la placa</b>: documentación oficial de micro:bit (microbit.org y tech.microbit.org).',
    '<b>Kits y robots</b>: datos, puertos y funciones tomados del wiki de ELECFREAKS, del wiki de DFRobot y del código de sus extensiones oficiales de MakeCode.',
    '<b>Inteligencia artificial</b>: según la guía de usuario oficial de micro:bit CreateAI.',
    '<b>Recursos recomendados</b>: los recursos de Pedro Ruiz (pedroruizf) y de TecnoJajulca (jajulca.eu, Eufrasio Cabrera) se citan como referencia y enlace.',
    '<b>Ideas de otros materiales</b>: algunas actividades parten de ideas de los retos de Pedro Ruiz, del <i>Manual de Programación micro:bit</i> de José Francisco Muñoz (Almeribot · Microes.org), del <i>Cuaderno de proyectos micro:bit</i> de Plan Ceibal y de las tarjetas de MicroBlocks. Cada una lo indica al final con «Idea inspirada en…».',
])
PROPIOS = [
    ('Conoce micro:bit', 'https://pablomoraga.github.io/conocemicrobit/', 'La placa V2 y misiones con MakeCode (eXeLearning).'),
    ('Taller micro:bit', 'https://pablomoraga.github.io/tallermicrobit/', 'Taller con misiones y un proyecto simulado.'),
    ('Un hogar inteligente', 'https://pablomoraga.github.io/microbitcasainteligente/', 'REA para 5.º de Primaria: casa inteligente con micro:bit.'),
    ('ESEROver', 'https://pablomoraga.github.io/eserover/', 'Rover Cutebot con retos «Destino Marte» e IoT.'),
    ('Moon Camp', 'https://pablomoraga.github.io/mooncamp/', 'Proyecto STEAM con ESEROver y Moon Garden.'),
    ('Robótica con kidsIOT', 'https://pablomoraga.github.io/roboticakidsiot/', 'Robótica con MicroBlocks y el kit Kidsbits.'),
    ('Scratch en el aula', 'https://pablomoraga.github.io/scratch-en-el-aula/', 'Manual de Scratch 3.0 para Primaria y ESO, con retos de micro:bit.'),
    ('Impresión 3D Código 4.0', 'https://pablomoraga.github.io/impresion-3d-codigo-4.0/', 'Manual de diseño e impresión 3D en el aula.'),
]
ZIP = 'https://github.com/pablomoraga/microbit-en-el-aula/archive/refs/heads/gh-pages.zip'
page(S, 'descargas', 'Descargas y uso sin conexión',
    P('Todo el material se puede descargar para usarlo en aulas con mala conexión o en ordenadores sin internet.') +
    '<div class="descargas">' +
    '<a class="card" href="%s"><span class="card-ico">%s</span><span class="card-tag">ZIP · unos 30 MB</span><span class="card-t">La web completa</span>'
    '<span class="card-d">Todas las páginas, imágenes y programas. Se genera con la última versión publicada.</span></a>' % (ZIP, icon('descarga', 26)) +
    '<a class="card" href="../recursos/tarjetas-comenzamos.pdf" download><span class="card-ico">%s</span><span class="card-tag">PDF</span><span class="card-t">Tarjetas de Comenzamos</span>'
    '<span class="card-d">Las 34 prácticas en tarjetas A5 para imprimir a doble cara.</span></a>' % icon('descarga', 26) +
    '</div>' +
    h2('Cómo usar la web sin conexión') +
    ol(['Descarga el ZIP y descomprímelo (botón derecho › <b>Extraer todo</b>).',
        'Abre la carpeta <b>microbit-en-el-aula-gh-pages</b> y haz doble clic en <b>index.html</b>.',
        'Para el aula, cópiala en una carpeta compartida o en un pendrive: no hace falta instalar nada.']) +
    box('ojo', 'Lo que necesita internet', ul([
        'El <b>simulador</b> de las prácticas y los editores (MakeCode, MicroBlocks y Python) se cargan desde sus webs oficiales.',
        'Los visores de montaje y las fotos de DFRobot de los kits se muestran desde las webs de los fabricantes.',
        'Sin conexión puedes leer todo, copiar el código y descargar los programas (.ubp y .py). Para trabajar sin internet, instala '
        '<a href="https://microblocks.fun/download" target="_blank" rel="noopener">MicroBlocks</a> o la '
        '<a href="https://makecode.microbit.org/offline-app" target="_blank" rel="noopener">aplicación de MakeCode sin conexión</a> en el ordenador.'])),
    icono='descarga')
page(S, 'enlaces', 'Enlaces y recursos', h2('Oficiales') + enlaces(OFICIAL) + h2('Guías y comunidad') + enlaces(GUIAS) +
    h2('Recursos de TecnoJajulca (Eufrasio Cabrera)') + enlaces(JAJULCA) + h2('Recursos de Pedro Ruiz') + enlaces(PEDRO) + h2('Mis recursos') + enlaces(PROPIOS), icono='enlace')
LIC = ('<a href="https://creativecommons.org/licenses/by-nc/4.0/deed.es" target="_blank" rel="noopener">CC BY-NC 4.0</a>')
IMAGENES = tabla(['Imagen', 'Dónde aparece', 'Fuente'], [
    ['Foto del Cutebot', 'Talleres › Cutebot', 'Captura del wiki de ELECFREAKS (wiki.elecfreaks.com)'],
    ['Diagrama de pines de Maqueen Lite', 'Talleres › Maqueen Lite', 'Captura del wiki de DFRobot (wiki.dfrobot.com/rob0148-en)'],
    ['Foto de Maqueen Plus V2', 'Talleres › Maqueen Plus V2', 'Captura del wiki de DFRobot (wiki.dfrobot.com/mbt0021-en)'],
    ['Foto de la placa IoT:bit', 'Talleres › Smart Agriculture Kit', 'Captura del wiki de ELECFREAKS'],
    ['Foto de la placa WuKong', 'Talleres › Wonder Building Kit', 'Repositorio github.com/elecfreaks/pxt-wukong (licencia MIT)'],
    ['Carruseles de montaje de Maqueen', 'Talleres › Maqueen Lite y Plus V2', 'Enlazadas desde el servidor de imágenes de DFRobot, sin copiarlas'],
    ['Montajes del Wonder Building Kit y del Smart Agriculture Kit', 'Actividades de esos kits', 'Página oficial del wiki de ELECFREAKS mostrada en un visor, sin copiarla'],
    ['Capturas de MakeCode, MicroBlocks y del editor de Python', 'Conoce micro:bit y Comenzamos', 'Hechas por el autor en los editores oficiales'],
])
page(S, 'creditos', 'Créditos y licencias',
    h2('Licencia de este material') +
    P('Este material se comparte con licencia %s:' % LIC) +
    ul(['<b>Puedes</b> copiarlos, compartirlos, adaptarlos y usarlos en tus clases.',
        '<b>Siempre citando al autor</b>: «micro:bit en el aula, Pablo Moraga» con el enlace a la web.',
        '<b>Sin uso comercial</b>: no se pueden vender ni incluir en productos de pago.']) +
    P('Las imágenes de terceros de la tabla de abajo <b>no</b> forman parte de esa licencia: pertenecen a sus autores y se muestran citando la fuente.') +
    h2('Fuentes y herramientas') + CREDITOS + h2('Imágenes de terceros') + IMAGENES, icono='libro')
