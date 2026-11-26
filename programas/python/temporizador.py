from microbit import *
import music

minutos = 0
while True:
    if button_a.was_pressed():
        minutos += 1
        display.scroll(minutos)
    if button_b.was_pressed():
        while minutos > 0:
            display.scroll(minutos)
            sleep(60000)
            minutos -= 1
        display.show(Image.YES)
        music.play(music.POWER_UP)
