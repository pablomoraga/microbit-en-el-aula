from microbit import *
import random

while True:
    if accelerometer.was_gesture("shake"):
        mano = random.randint(0, 2)
        if mano == 0:
            display.show(Image.SQUARE_SMALL)
        elif mano == 1:
            display.show(Image.SQUARE)
        else:
            display.show(Image.SCISSORS)
