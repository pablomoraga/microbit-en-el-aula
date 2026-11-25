from microbit import *

display.show(Image.MEH)
while True:
    if button_a.was_pressed():
        display.show(Image.HAPPY)
        audio.play(Sound.HAPPY)
        display.show(Image.MEH)
    if button_b.was_pressed():
        display.show(Image.SAD)
        audio.play(Sound.SAD)
        display.show(Image.MEH)
    if pin_logo.is_touched():
        display.show(Image.SILLY)
        audio.play(Sound.GIGGLE)
        display.show(Image.MEH)
