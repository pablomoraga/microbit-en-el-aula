from microbit import *

numero = 0
while True:
    if button_a.was_pressed():
        numero += 1
        if numero > 31:
            numero = 0
        potencia = 1
        for i in range(5):
            if (numero // potencia) % 2 == 1:
                display.set_pixel(4 - i, 2, 9)
            else:
                display.set_pixel(4 - i, 2, 0)
            potencia *= 2
    if button_b.was_pressed():
        display.scroll(numero)
