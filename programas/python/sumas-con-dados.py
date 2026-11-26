from microbit import *
import random

a = b = 0
while True:
    if accelerometer.was_gesture("shake"):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        display.scroll(str(a) + "+" + str(b))
    if button_b.was_pressed():
        display.scroll(a + b)
