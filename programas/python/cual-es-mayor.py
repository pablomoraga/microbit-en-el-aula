from microbit import *
import random

a = b = 0
while True:
    if pin_logo.is_touched():
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        display.scroll(str(a) + "-" + str(b))
    if button_a.was_pressed():
        display.show(Image.YES if a > b else Image.NO)
    if button_b.was_pressed():
        display.show(Image.YES if b > a else Image.NO)
