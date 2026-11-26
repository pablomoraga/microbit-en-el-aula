# -*- coding: utf-8 -*-
"""Inteligencia artificial con micro:bit CreateAI (según la guía oficial de microbit.org)."""
from common import page, P, ul, ol, box, tabla, h2, h3, e
from iconos import icon

S = 'ia'

def enlaces(items):
    return '<div class="enlaces">%s</div>' % ''.join(
        '<a href="%s" target="_blank" rel="noopener"><b>%s %s</b><span>%s</span></a>' % (u, icon('enlace', 16), e(t), d) for t, u, d in items)

page(S, 'que-es-createai', 'IA y aprendizaje automático', P(
    'La <b>inteligencia artificial</b> (IA) hace que las máquinas realicen tareas que parecen inteligentes, como reconocer una cara o entender una frase. '
    'Una de sus formas más usadas es el <b>aprendizaje automático</b>: en lugar de escribir las reglas, le damos a la máquina muchos <b>ejemplos</b> y ella aprende a reconocer patrones.') +
    P('<a href="https://createai.microbit.org" target="_blank" rel="noopener">micro:bit CreateAI</a> es la herramienta gratuita y oficial de la Micro:bit Educational Foundation para entrenar un modelo '
      'con los movimientos que mide el acelerómetro de la placa y usarlo después en un programa de MakeCode. Está en español.') +
    h2('Las palabras clave') +
    tabla(['Palabra', 'Qué significa', 'En CreateAI'], [
        ['Datos', 'Los ejemplos con los que aprende la máquina.', 'Muestras de movimiento de 1 segundo grabadas con el acelerómetro.'],
        ['Acción', 'Cada cosa distinta que queremos reconocer.', 'Aplaudir, saludar, saltar, estar quieto…'],
        ['Entrenar', 'Hacer que el modelo aprenda de los datos.', 'El botón «Entrenar modelo».'],
        ['Modelo', 'Lo que ha aprendido la máquina: un «filtro» que clasifica movimientos nuevos.', 'Se descarga a la micro:bit V2 junto al programa.'],
        ['Certeza', 'Lo segura que está la máquina de su respuesta, en %.', 'Se ve al probar el modelo.'],
        ['Punto de reconocimiento', 'Certeza mínima para dar por buena una acción.', 'Se puede ajustar al probar.'],
    ]) +
    h2('Qué necesitas') +
    ul(['Un ordenador con Chrome o Edge, o una tableta Android o iPad con la aplicación CreateAI.',
        'Una micro:bit <b>V2</b>, cable USB de datos y portapilas.',
        'Una forma de sujetar la placa a la muñeca, al tobillo o a un objeto (una cinta o un soporte impreso en 3D).',
        'Si el ordenador no tiene Bluetooth, <b>una segunda micro:bit V2</b> que hace de enlace de radio conectada por USB.']) +
    box('sabias', 'Por qué la V2', P('Con cualquier micro:bit se pueden recoger datos y entrenar, pero para ejecutar el modelo dentro de la placa hace falta el procesador más rápido de la V2.')),
    icono='cerebro')

page(S, 'primer-modelo', 'Mi primer modelo: aplaudir o saludar', P(
    'Entrenamos un modelo que distinga tres acciones (<b>aplaudir</b>, <b>saludar</b> y <b>quieto</b>) y lo usamos para que la micro:bit reaccione a cada una.') +
    '<div class="ficha"><span class="chip">%s 2 sesiones</span><span class="chip">Primaria · ESO</span><span class="chip chip-c">datos</span><span class="chip chip-c">entrenamiento</span><span class="chip chip-c">eventos</span></div>' % icon('reloj', 14) +
    h2('1. Conectar la placa') +
    ol(['Abre <a href="https://createai.microbit.org" target="_blank" rel="noopener">createai.microbit.org</a> en Chrome o Edge y pulsa <b>Nuevo proyecto</b>.',
        'Sigue las instrucciones de la pantalla: CreateAI elige la conexión adecuada (Bluetooth o enlace de radio con una segunda placa).',
        'Sujeta la placa a la muñeca con una cinta. Cuando muevas la mano, verás la gráfica de movimiento en directo.']) +
    h2('2. Recoger datos') +
    ol(['Crea la primera acción, <b>aplaudir</b>, y elige su icono.',
        'Pulsa <b>Grabar</b> (o el botón B de la placa) y aplaude justo al empezar. Cada muestra dura 1 segundo.',
        'Graba al menos 10 muestras: el mínimo son 3, pero con más datos el modelo funciona mejor.',
        'Añade las acciones <b>saludar</b> y <b>quieto</b> y graba sus muestras.',
        'Revisa las muestras y borra las que estén mal (por ejemplo, si empezaste tarde): eso es <b>limpiar los datos</b>.']) +
    h2('3. Entrenar y probar') +
    ol(['Pulsa <b>Entrenar modelo</b>.', 'Haz cada movimiento y mira la <b>acción estimada</b> y su <b>certeza</b>.',
        'Si se equivoca, mejóralo: graba más muestras, pide a otras personas que graben las suyas o elige movimientos más diferentes. Vuelve a entrenar.']) +
    h2('4. Programar con el modelo') +
    ol(['Pulsa <b>Editar en MakeCode</b>. Aparece la categoría de aprendizaje automático, arriba del todo, con bloques para tus acciones.',
        'Usa el evento <b>al empezar</b> de cada acción: con aplaudir, muestra un corazón y toca un sonido; con saludar, muestra una cara sonriente; con quieto, borra la pantalla.',
        'Pulsa <b>Descargar</b> y sigue las instrucciones para pasar el programa y el modelo a una micro:bit V2.',
        'Pon pilas a la placa y pruébala sin ordenador.']) +
    box('idea', 'Los bloques de aprendizaje automático', ul([
        '<b>al empezar</b> una acción: se ejecuta cuando el modelo cambia a esa acción.',
        '<b>al terminar</b> una acción: se ejecuta cuando deja de detectarla; una versión del bloque da también su <b>duración</b> en milisegundos.',
        '<b>¿se detecta</b> una acción?: verdadero o falso, para usar dentro de un «si».',
        '<b>certeza (%)</b> de una acción: un número de 0 a 100.'])) +
    box('docente', 'Para el profesorado', P('El paso más importante es el de <b>mejorar el modelo</b>: el alumnado comprueba que la IA solo es tan buena como sus datos, y que esos datos los recogen, '
        'etiquetan y revisan personas. Es el momento de hablar de <b>sesgos</b>: si solo graba una persona, ¿funcionará igual con las demás?')),
    icono='cerebro')

page(S, 'ideas-y-recursos', 'Ideas y recursos de IA', P('Proyectos para seguir, todos con CreateAI y MakeCode:') +
    tabla(['Idea', 'Acciones a entrenar', 'Qué hace la placa'], [
        ['Contador de ejercicios', 'Sentadilla, salto, quieto', 'Cuenta repeticiones de cada ejercicio y las muestra.'],
        ['Interruptor por gestos', 'Girar la muñeca, quieto', 'Envía por radio una orden para encender o apagar una luz.'],
        ['Mando de juego', 'Inclinar a izquierda, a derecha, agitar', 'Controla un juego de otra placa por radio.'],
        ['Detector de baile', 'Tres pasos de baile', 'Pone una nota distinta con cada paso.'],
        ['Avisador de postura', 'Espalda recta, encorvado', 'Pita si estás encorvado durante mucho tiempo.'],
    ]) +
    h2('Hablar de IA en clase') +
    ul(['¿Qué datos personales recoge un reloj inteligente? ¿Quién los ve?', '¿Por qué el modelo falla con movimientos que no ha visto nunca?',
        '¿Es justa una IA entrenada solo por una parte de la clase?', '¿Qué decisiones nunca debería tomar una máquina sola?']) +
    h2('Recursos oficiales') + enlaces([
        ('micro:bit CreateAI', 'https://createai.microbit.org', 'La herramienta, con ideas de proyectos y recursos para docentes.'),
        ('Guía del usuario de CreateAI', 'https://microbit.org/get-started/user-guide/microbit-createai/', 'Explicación completa de cada paso y de los bloques de MakeCode.'),
        ('Primeras lecciones con CreateAI', 'https://microbit.org/teach/lessons/first-lessons-with-microbit-createai/', 'Unidad didáctica oficial.'),
        ('Clases de prueba', 'https://microbit.org/teach/lessons/createai-taster-lessons/', 'Sesiones cortas para empezar.'),
        ('Alfabetización en IA', 'https://microbit.org/teach/lessons/developing-ai-literacy-with-the-microbit/', 'Lecciones para entender cómo funciona la IA.'),
    ]), icono='cerebro')
