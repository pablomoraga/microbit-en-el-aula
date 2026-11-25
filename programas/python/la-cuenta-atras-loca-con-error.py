from microbit import *

while True:
    if button_a.was_pressed():
        display.show(1)
        sleep(700)
        display.show(2)
        sleep(700)
        display.show(3)
        sleep(700)
        display.show(Image.ARROW_N)
