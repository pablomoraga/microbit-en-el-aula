from microbit import *

numero = 0
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        numero = 0
        display.scroll(numero)
    elif button_a.was_pressed():
        numero += 10
        display.show("D")
    elif button_b.was_pressed():
        numero += 1
        display.show("U")
    if pin_logo.is_touched():
        display.scroll(numero)
