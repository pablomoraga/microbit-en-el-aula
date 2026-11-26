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
    '<b>Kits y robots</b>: datos, puertos y funciones tomados del wiki de ELECFREAKS, del wiki de DFRobot y del código de sus extensiones oficiales de MakeCode. Las ilustraciones son esquemas propios.',
    '<b>Inteligencia artificial</b>: según la guía de usuario oficial de micro:bit CreateAI.',
    '<b>Recursos recomendados</b>: los recursos de Pedro Ruiz (pedroruizf) y de TecnoJajulca (jajulca.eu, Eufrasio Cabrera) se citan como referencia y enlace. Este material no reproduce sus contenidos; si en el futuro se adapta alguno, se indicará en la propia actividad.',
    'Ilustraciones, iconos, prácticas, programas y textos: elaboración propia de Pablo Moraga (CC BY-NC-ND 4.0).',
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
page(S, 'enlaces', 'Enlaces y recursos', h2('Oficiales') + enlaces(OFICIAL) + h2('Guías y comunidad') + enlaces(GUIAS) +
    h2('Recursos de TecnoJajulca (Eufrasio Cabrera)') + enlaces(JAJULCA) + h2('Recursos de Pedro Ruiz') + enlaces(PEDRO) + h2('Mis recursos') + enlaces(PROPIOS), icono='enlace')
page(S, 'creditos', 'Créditos y licencias', P('Este material es de elaboración propia. Estas son las fuentes y herramientas utilizadas:') + CREDITOS, icono='libro')
