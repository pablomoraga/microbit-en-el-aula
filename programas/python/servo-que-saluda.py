from microbit import *

pin0.set_analog_period(20)

def angulo(grados):
    # de 0-180 grados a impulsos de 0,5-2,5 ms (valores de 26 a 128)
    pin0.write_analog(26 + grados * 102 // 180)

while True:
    if button_a.was_pressed():
        angulo(0)
    if button_b.was_pressed():
        angulo(180)
    if pin_logo.is_touched():
        for i in range(3):
            angulo(45)
            sleep(300)
            angulo(135)
            sleep(300)
