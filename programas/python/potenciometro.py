from microbit import *
import music

while True:
    valor = pin2.read_analog()
    filas = valor * 6 // 1024
    display.clear()
    for i in range(filas):
        for x in range(5):
            display.set_pixel(x, 4 - i, 9)
    if button_a.was_pressed():
        music.pitch(200 + valor * 800 // 1023, 300)
    sleep(100)
