from microbit import *

TRIANGULO = Image("00900:09090:90009:99999:00000")
RECTANGULO = Image("00000:99999:90009:99999:00000")
figuras = [Image.SQUARE, TRIANGULO, RECTANGULO, Image.DIAMOND]
lados = [4, 3, 4, 4]
figura = 0
while True:
    if button_a.was_pressed():
        figura = (figura + 1) % 4
        display.show(figuras[figura])
    if button_b.was_pressed():
        display.scroll(lados[figura])
