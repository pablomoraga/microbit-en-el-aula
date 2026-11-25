from microbit import *
import random

while True:
    if button_b.was_pressed():
        display.clear()
        sleep(random.randint(1000, 4000))
        display.show(Image.TARGET)
        salida = running_time()
        while not button_a.is_pressed():
            sleep(1)
        display.scroll(running_time() - salida)
