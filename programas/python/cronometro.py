from microbit import *

inicio = 0
while True:
    if button_a.was_pressed():
        inicio = running_time()
        display.show(Image.YES)
    if button_b.was_pressed():
        display.scroll((running_time() - inicio) // 1000)
