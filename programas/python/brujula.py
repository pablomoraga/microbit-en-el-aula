from microbit import *

while True:
    grados = compass.heading()
    if grados < 45 or grados >= 315:
        display.show("N")
    elif grados < 135:
        display.show("E")
    elif grados < 225:
        display.show("S")
    else:
        display.show("O")
