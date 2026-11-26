from microbit import *
import random

metros = 0
while True:
    if button_a.was_pressed():
        metros = random.randint(1, 9)
        display.scroll(str(metros) + "m")
    if button_b.was_pressed():
        display.scroll(str(metros * 100) + "cm")
