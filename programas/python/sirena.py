from microbit import *
import music

while True:
    if button_a.is_pressed():
        display.show(Image.DIAMOND)
        music.pitch(600, 300)
        display.show(Image.DIAMOND_SMALL)
        music.pitch(900, 300)
    else:
        display.clear()
