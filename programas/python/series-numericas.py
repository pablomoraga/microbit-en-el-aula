from microbit import *
import random

salto = inicio = 0
while True:
    if button_a.was_pressed():
        salto = random.randint(2, 9)
        inicio = random.randint(1, 10)
        display.scroll("%d,%d,%d,?" % (inicio, inicio + salto, inicio + 2 * salto))
    if button_b.was_pressed():
        display.scroll(inicio + 3 * salto)
