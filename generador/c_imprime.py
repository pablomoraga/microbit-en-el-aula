# -*- coding: utf-8 -*-
from common import page, P, ul, box, tabla, h2, e
from iconos import icon

S = 'imprime'

def enlaces(items):
    return '<div class="enlaces">%s</div>' % ''.join(
        '<a href="%s" target="_blank" rel="noopener"><b>%s %s</b><span>%s</span></a>' % (u, icon('enlace', 16), e(t), d) for t, u, d in items)

page(S, 'disenos-3d', 'Diseños 3D para micro:bit', P(
    'La impresión 3D completa muy bien los proyectos con micro:bit: carcasas que protegen la placa, soportes para el portapilas, piezas compatibles con LEGO o cajas para estaciones meteorológicas.') +
    h2('Mis diseños') + enlaces([
        ('Repositorio de diseños 3D', 'https://github.com/pablomoraga/impresion3d', 'Carcasas, soportes y accesorios para micro:bit y otras placas, con archivos STL y consejos de impresión (en construcción).'),
        ('Impresión 3D Código 4.0', 'https://pablomoraga.github.io/impresion-3d-codigo-4.0/', 'Manual para diseñar e imprimir en el aula: impresora, laminador, Tinkercad y retos.'),
    ]) +
    h2('Ideas de piezas para estos proyectos') +
    tabla(['Pieza', 'Para qué', 'Proyecto'], [
        ['Carcasa con hueco para los botones y el logotipo', 'Proteger la placa en el aula', 'Todas las prácticas'],
        ['Soporte para la placa y el portapilas', 'Llevar la micro:bit en la muñeca o el tobillo', 'Podómetro, contador de palmadas'],
        ['Caja ventilada', 'Proteger la estación del sol directo', 'Estación meteorológica'],
        ['Marco de semáforo', 'Sujetar los tres LED', 'Semáforo de LED y cruce inteligente'],
        ['Brazo para servo', 'Ventana, barrera o brazo que saluda', 'Servo que saluda, invernadero'],
        ['Base para el juego del pulso', 'Sujetar el alambre', 'El juego del pulso'],
    ]) +
    h2('Buscar más diseños') + enlaces([
        ('Printables: micro:bit', 'https://www.printables.com/search/models?q=microbit', 'Buscador de modelos de la comunidad de Prusa.'),
        ('Thingiverse: micro:bit', 'https://www.thingiverse.com/search?q=microbit', 'Buscador de modelos de Thingiverse.'),
    ]) +
    box('ojo', 'Antes de imprimir', ul(['Comprueba la licencia de cada diseño y cita a su autor.', 'Mide tu placa y tu portapilas: hay pequeñas diferencias entre versiones.',
        'Deja los agujeros del micrófono y el altavoz despejados en la V2.'])),
    icono='caja')
