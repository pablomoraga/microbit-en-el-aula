from microbit import *

while True:
    nivel = microphone.sound_level()
    if nivel > 50:
        display.show(Image.MEH)
    elif nivel > 120:
        display.show(Image.ANGRY)
    else:
        display.show(Image.HAPPY)
    sleep(100)
