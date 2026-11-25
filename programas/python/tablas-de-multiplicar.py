from microbit import *
import random

a = b = 0
while True:
    if button_a.was_pressed():
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        display.scroll(str(a) + "x" + str(b))
    if button_b.was_pressed():
        display.scroll(a * b)
