from microbit import *

CALABAZA = Image("09990:99999:90909:99999:09090")
while True:
    if display.read_light_level() < 30:
        display.show(CALABAZA)
        audio.play(Sound.GIGGLE)
    else:
        display.show(Image.ASLEEP)
    sleep(300)
