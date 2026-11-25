from microbit import *
import music

pin1.set_pull(pin1.PULL_UP)
activa = True
clave = ""
while True:
    if button_a.was_pressed():
        clave += "A"
    if button_b.was_pressed():
        clave += "B"
        if clave == "AAB":
            activa = False
            display.show(Image.NO)
        clave = ""
    if pin_logo.is_touched():
        activa = True
        display.show(Image.YES)
    if activa and pin1.read_digital() == 1:
        display.show(Image.SKULL)
        music.pitch(988, 250)
        music.pitch(784, 250)
