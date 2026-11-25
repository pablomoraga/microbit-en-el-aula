from microbit import *

contador = 0
while True:
    if button_a.was_pressed():
        contador += 1
        display.scroll(contador)
