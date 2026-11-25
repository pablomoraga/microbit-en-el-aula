from microbit import *
import music

while True:
    if accelerometer.was_gesture("shake"):
        display.clear()
        for y in range(5):
            for x in range(5):
                display.set_pixel(x, y, 9)
                sleep(1000)
        music.play(music.ENTERTAINER)
