from microbit import *
import music

while True:
    luz = display.read_light_level()
    if luz > 10:
        music.pitch(200 + luz * 4, 100)
    else:
        sleep(100)
