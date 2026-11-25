from microbit import *
import random

while True:
    if button_a.was_pressed():
        veces = [0, 0, 0, 0, 0, 0]
        for i in range(600):
            cara = random.randint(1, 6)
            veces[cara - 1] += 1
        for j in range(6):
            display.scroll(str(j + 1) + ":" + str(veces[j]))
