from microbit import *
import music

while True:
    if pin0.is_touched():
        display.show("C")
        music.pitch(262, 300)
    if pin1.is_touched():
        display.show("E")
        music.pitch(330, 300)
    if pin2.is_touched():
        display.show("G")
        music.pitch(392, 300)
