from microbit import *
import music

while True:
    humedad = pin1.read_analog()
    if humedad < 300:
        display.show(Image.SAD)
        music.pitch(440, 250)
    else:
        display.show(Image.HAPPY)
    sleep(2000)
