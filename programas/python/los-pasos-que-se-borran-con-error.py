from microbit import *

while True:
    if accelerometer.was_gesture("shake"):
        pasos = 0
        pasos += 1
        display.scroll(pasos)
