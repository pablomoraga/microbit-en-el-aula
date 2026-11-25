from microbit import *
import random
import music

while True:
    if pin_logo.is_touched():
        for n in (3, 2, 1):
            display.show(n)
            sleep(700)
        display.clear()
        sleep(random.randint(1000, 5000))
        display.show(Image.HEART)
        while not (button_a.is_pressed() or button_b.is_pressed()):
            sleep(1)
        if button_a.is_pressed():
            display.show("A")
        else:
            display.show("B")
        music.play(music.POWER_UP)
