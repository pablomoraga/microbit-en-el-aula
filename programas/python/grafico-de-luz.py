from microbit import *

while True:
    filas = display.read_light_level() * 6 // 256
    display.clear()
    for i in range(filas):
        for x in range(5):
            display.set_pixel(x, 4 - i, 9)
    sleep(200)
