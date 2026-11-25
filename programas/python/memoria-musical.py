from microbit import *
import random
import music

secuencia = []
ok = True
while ok:
    secuencia.append(random.randint(1, 2))
    for nota in secuencia:
        if nota == 1:
            display.show(Image.ARROW_W)
            music.pitch(262, 400)
        else:
            display.show(Image.ARROW_E)
            music.pitch(523, 400)
        display.clear()
        sleep(200)
    for nota in secuencia:
        while not (button_a.is_pressed() or button_b.is_pressed()):
            sleep(1)
        respuesta = 1 if button_a.is_pressed() else 2
        while button_a.is_pressed() or button_b.is_pressed():
            sleep(1)
        if respuesta != nota:
            ok = False
            break
    if ok:
        display.show(Image.YES)
        sleep(500)
display.show(Image.NO)
sleep(1000)
display.scroll(len(secuencia) - 1)
