from microbit import *
import random

nave, ax, ay, puntos = 2, random.randint(0, 4), 0, 0
while True:
    if button_a.was_pressed() and nave > 0:
        nave -= 1
    if button_b.was_pressed() and nave < 4:
        nave += 1
    display.clear()
    display.set_pixel(nave, 4, 9)
    display.set_pixel(ax, ay, 5)
    sleep(max(150, 500 - puntos * 20))
    if ay == 4 and ax == nave:
        break
    elif ay == 4:
        puntos += 1
        ay = 0
        ax = random.randint(0, 4)
    else:
        ay += 1
display.show(Image.SKULL)
sleep(1000)
display.scroll("Puntos " + str(puntos))
