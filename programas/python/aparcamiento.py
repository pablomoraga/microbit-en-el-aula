from microbit import *
import music

pin0.set_analog_period(20)

def angulo(grados):
    # de 0-180 grados a impulsos de 0,5-2,5 ms (valores de 26 a 128)
    pin0.write_analog(26 + grados * 102 // 180)

def abrir_barrera():
    angulo(90)
    sleep(2000)
    angulo(0)

plazas = 3
angulo(0)
display.show(plazas)
while True:
    if button_a.was_pressed():
        if plazas > 0:
            plazas -= 1
            abrir_barrera()
        else:
            display.show(Image.NO)
            music.pitch(196, 500)
        display.show(plazas)
    if button_b.was_pressed():
        if plazas < 3:
            plazas += 1
            abrir_barrera()
        display.show(plazas)
