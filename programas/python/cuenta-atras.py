from microbit import *
import music

while True:
    if button_a.was_pressed():
        display.show(3)
        music.pitch(440, 250)
        display.show(2)
        music.pitch(440, 250)
        display.show(1)
        music.pitch(440, 250)
        display.show(Image.ARROW_N)
        music.pitch(880, 1000)
        display.clear()
