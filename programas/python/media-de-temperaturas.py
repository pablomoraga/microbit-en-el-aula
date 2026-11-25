from microbit import *

while True:
    if button_a.was_pressed():
        medidas = []
        for i in range(6):
            medidas.append(temperature())
            display.set_pixel(2, 2, 9 * (i % 2))
            sleep(10000)
        media = sum(medidas) / len(medidas)
        display.scroll("Media " + str(round(media, 1)))
        display.scroll("Max " + str(max(medidas)))
        display.scroll("Min " + str(min(medidas)))
