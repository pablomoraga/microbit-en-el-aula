from microbit import *
import random

cesta, x, y = 2, random.randint(0, 4), 0
puntos, vidas = 0, 3
while vidas > 0:
    if button_a.was_pressed() and cesta > 0:
        cesta -= 1
    if button_b.was_pressed() and cesta < 4:
        cesta += 1
    display.clear()
    display.set_pixel(cesta, 4, 9)
    display.set_pixel(x, y, 5)
    sleep(400)
    y += 1
    if y == 4:
        if x == cesta:
            puntos += 1
        else:
            vidas -= 1
        y, x = 0, random.randint(0, 4)
display.scroll("Puntos " + str(puntos))
