from microbit import *
import music

while True:
    if button_a.was_pressed():
        display.show("C")
        music.pitch(262, 300)
    if button_b.was_pressed():
        display.show("D")
        music.pitch(294, 300)
    if pin_logo.is_touched():
        display.show("E")
        music.pitch(330, 300)
