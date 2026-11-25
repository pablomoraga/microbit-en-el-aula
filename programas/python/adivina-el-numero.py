from microbit import *
import random
import music

secreto = random.randint(1, 9)
respuesta = 1
display.show(respuesta)
while True:
    if button_a.was_pressed():
        respuesta += 1
        if respuesta > 9:
            respuesta = 1
        display.show(respuesta)
    if button_b.was_pressed():
        if respuesta == secreto:
            display.show(Image.YES)
            music.play(music.POWER_UP)
            secreto = random.randint(1, 9)
        elif respuesta < secreto:
            display.show(Image.ARROW_N)
        else:
            display.show(Image.ARROW_S)
