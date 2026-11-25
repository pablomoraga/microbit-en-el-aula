from microbit import *
import random
import music

while True:
    if button_a.was_pressed():
        limite = running_time() + random.randint(5000, 15000)
        while running_time() < limite:
            display.show(Image.GHOST)
            music.pitch(523, 60)
            sleep(400)
        display.show(Image.SKULL)
        music.pitch(131, 1200)
