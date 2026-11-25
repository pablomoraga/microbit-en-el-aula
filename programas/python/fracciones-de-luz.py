from microbit import *

encendidos = 0
while True:
    if button_a.was_pressed():
        encendidos += 1
        if encendidos > 25:
            encendidos = 0
        display.clear()
        for i in range(encendidos):
            display.set_pixel(i % 5, i // 5, 9)
    if button_b.was_pressed():
        display.scroll(str(encendidos * 4) + "%")
