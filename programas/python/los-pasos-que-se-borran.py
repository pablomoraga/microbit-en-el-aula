from microbit import *

pasos = 0
while True:
    if accelerometer.was_gesture("shake"):
        pasos += 1
        display.scroll(pasos)
