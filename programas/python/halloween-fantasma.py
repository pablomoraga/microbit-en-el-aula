from microbit import *

while True:
    if accelerometer.was_gesture("shake"):
        display.show(Image.GHOST)
        audio.play(Sound.MYSTERIOUS)
        display.clear()
