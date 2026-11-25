from microbit import *

encendido = Image("99999:99999:99999:99999:99999")

while True:
    if display.read_light_level() < 30:
        display.show(encendido)
    else:
        display.clear()
    sleep(200)
