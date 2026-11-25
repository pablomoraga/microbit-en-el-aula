from microbit import *
import radio
import music

radio.on()
radio.config(group=30)
notas = [262, 330, 392]
mia = 0
tocando = False
tiempo = 1
ultimo = 0
while True:
    if button_a.was_pressed():
        tocando = not tocando
    if button_b.was_pressed():
        mia = (mia + 1) % 3
        display.show(mia + 1)
    if tocando and running_time() - ultimo > 500:
        ultimo = running_time()
        radio.send(str(tiempo))
        display.show(tiempo)
        tiempo = tiempo % 4 + 1
    golpe = radio.receive()
    if golpe in ("1", "3"):
        music.pitch(notas[mia], 250, wait=False)
