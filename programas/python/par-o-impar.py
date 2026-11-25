from microbit import *
import random

n = 0
while True:
    if accelerometer.was_gesture("shake"):
        n = random.randint(1, 20)
        display.scroll(n)
    if button_a.was_pressed():
        if n % 2 == 0:
            display.show(Image.YES)
        else:
            display.show(Image.NO)
    if button_b.was_pressed():
        if n % 2 == 1:
            display.show(Image.YES)
        else:
            display.show(Image.NO)
