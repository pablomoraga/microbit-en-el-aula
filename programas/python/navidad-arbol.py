from microbit import *
import random
import music

ARBOL = Image("00900:09990:99999:09990:99999")
while True:
    luces = ARBOL.copy()
    luces.set_pixel(random.randint(0, 4), random.randint(1, 4), 0)
    display.show(luces)
    if button_a.was_pressed():
        music.play(["E5:2", "E5:2", "E5:4", "E5:2", "E5:2", "E5:4"], wait=False)
    sleep(300)
