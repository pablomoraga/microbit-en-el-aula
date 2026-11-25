# Guía para editar «micro:bit en el aula»

## Estructura
| Archivo | Contiene |
|---|---|
| `generador/c_empezar.py` | Para empezar |
| `generador/c_conoce.py` | Conoce micro:bit (placa, editores, extensiones) |
| `generador/c_comenzamos.py` | Las 30 prácticas |
| `generador/c_experto.py` | Modo experto |
| `generador/c_talleres.py` | Talleres (proyectos tipo y kits) |
| `generador/c_celebrar.py` | Para celebrar (efemérides) |
| `generador/c_imprime.py` | Imprime en 3D |
| `generador/c_saber.py` | Para saber más |

Cada práctica lleva el programa en tres formatos: JavaScript de MakeCode, texto de MicroBlocks (el mismo de los .ubp) y Python.

## Construir en local
```
python generador/build.py
```
La web queda en `_salida/web`.

## Imágenes de los bloques de MakeCode
Si cambias o añades un programa de MakeCode, hay que generar su imagen:
1. `python generador/build.py`
2. `python herramientas/renderizar_makecode.py` y abre http://localhost:8791/ en Chrome o Edge.
3. Cuando termine, vuelve a construir y sube las imágenes nuevas de `generador/estaticos/img/makecode/`.

## Publicar
Al subir cambios a `main`, la Action **Construir y publicar la web** reconstruye y publica en GitHub Pages (Settings › Pages › Source: GitHub Actions).
