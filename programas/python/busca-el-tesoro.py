from microbit import *
import radio

radio.on()
radio.config(group=4)
tesoro = False
while True:
    if button_a.was_pressed():
        tesoro = True
        display.show(Image.DIAMOND)
    if tesoro:
        radio.send("0")
        sleep(200)
    paquete = radio.receive_full()
    if paquete:
        senal = paquete[1]
        if senal > -60:
            display.show(Image.HEART)
        elif senal > -75:
            display.show(Image.HEART_SMALL)
        else:
            display.show(Image("00000:00000:00900:00000:00000"))
