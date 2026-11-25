from microbit import *
import random

cientificas = ["Ada Lovelace", "Marie Curie", "Hedy Lamarr", "Margarita Salas", "Katherine Johnson"]
i = 0
while True:
    if button_a.was_pressed():
        display.scroll(cientificas[i])
        i = (i + 1) % len(cientificas)
    if button_b.was_pressed():
        display.scroll(random.choice(cientificas))
