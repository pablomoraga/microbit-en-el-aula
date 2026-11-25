from microbit import *
import music

GOTA = Image("00900:09990:99999:99999:09990")
pin0.set_analog_period(20)

def ventana(grados):
    pin0.write_analog(26 + grados * 102 // 180)

ultimo = 0
while True:
    if running_time() - ultimo > 2000:
        ultimo = running_time()
        if pin1.read_analog() < 300:
            display.show(GOTA)
            music.pitch(440, 120)
        else:
            display.show(Image.HAPPY)
        if temperature() > 28:
            ventana(90)
        elif temperature() < 24:
            ventana(0)
    if button_a.was_pressed():
        display.scroll(temperature())
    if button_b.was_pressed():
        display.scroll(pin1.read_analog())
