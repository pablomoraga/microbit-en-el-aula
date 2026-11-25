from microbit import *

while True:
    nivel = microphone.sound_level()
    if nivel > 120:
        display.show(Image.ANGRY)
    elif nivel > 50:
        display.show(Image.MEH)
    else:
        display.show(Image.HAPPY)
    sleep(100)
