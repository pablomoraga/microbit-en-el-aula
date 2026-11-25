from microbit import *
import music

fallos = 0
display.show(Image.HAPPY)
pin0.set_pull(pin0.PULL_UP)
while True:
    if pin0.read_digital() == 0:
        fallos += 1
        music.pitch(196, 250)
        display.scroll(fallos)
    if button_a.was_pressed():
        fallos = 0
        display.show(Image.HAPPY)
