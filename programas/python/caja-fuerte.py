from microbit import *
import music

a = 0
b = 0
while True:
    if button_a.was_pressed():
        a += 1
    if button_b.was_pressed():
        b += 1
    if pin_logo.is_touched():
        if a == 3 and b == 2:
            display.show(Image.YES)
            music.pitch(988, 500)
        else:
            display.show(Image.NO)
        a = 0
        b = 0
        sleep(500)
