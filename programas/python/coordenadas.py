from microbit import *
import random

x = y = 0
while True:
    if button_b.was_pressed():
        display.clear()
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        display.set_pixel(x, y, 9)
    if button_a.was_pressed():
        display.scroll(str(x) + "," + str(y))
        display.set_pixel(x, y, 9)
