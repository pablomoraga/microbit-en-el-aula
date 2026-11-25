from microbit import *

while True:
    if temperature() > 30 or display.read_light_level() > 240:
        display.scroll("Sombra")
    else:
        display.show(Image.HAPPY)
    sleep(1000)
