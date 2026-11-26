from microbit import *
import music

pin0.set_pull(pin0.PULL_UP)
while True:
    if pin0.read_digital() == 0:
        display.show(Image.YES)
        music.pitch(988, 120)
    else:
        display.show(Image.NO)
