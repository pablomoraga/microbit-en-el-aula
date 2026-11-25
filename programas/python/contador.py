from microbit import *

contador = 0
display.scroll(contador)
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        contador = 0
        display.scroll(contador)
    elif button_a.was_pressed():
        contador += 1
        display.scroll(contador)
    elif button_b.was_pressed():
        contador -= 1
        display.scroll(contador)
