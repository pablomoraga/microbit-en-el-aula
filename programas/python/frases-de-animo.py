from microbit import *
import random

frases = ["Tu puedes", "Sigue asi", "Genial", "Paso a paso", "Animo"]
while True:
    if button_a.was_pressed():
        display.scroll(random.choice(frases))
