from microbit import *
import music

pin1.set_pull(pin1.PULL_UP)
vigilando = True
while True:
    if button_a.was_pressed():
        vigilando = not vigilando
        display.show(Image.YES if vigilando else Image.NO)
    if vigilando and pin1.read_digital() == 1:
        display.show(Image.SURPRISED)
        music.pitch(880, 250)
        music.pitch(660, 250)
