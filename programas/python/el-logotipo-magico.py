from microbit import *

display.show("?")
while True:
    if pin_logo.is_touched():
        display.scroll("Eres genial")
        display.show("?")
