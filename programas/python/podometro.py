from microbit import *

pasos = 0
while True:
    if accelerometer.was_gesture("shake"):
        pasos += 1
        display.set_pixel(2, 2, 9)
        sleep(100)
        display.set_pixel(2, 2, 0)
    if button_a.was_pressed():
        display.scroll(pasos)
