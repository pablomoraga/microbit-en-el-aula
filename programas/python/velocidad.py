from microbit import *

salida = 0
while True:
    if button_a.was_pressed():
        salida = running_time()
        display.show(Image.YES)
    if button_b.was_pressed():
        segundos = (running_time() - salida) / 1000
        display.scroll("t=" + str(round(segundos, 1)) + "s")
        display.scroll("v=" + str(round(10 / segundos, 1)) + "m/s")
