from microbit import *
import radio

radio.on()
radio.config(group=3)
ultimo_envio = 0
while True:
    if running_time() - ultimo_envio > 2000:
        radio.send(str(temperature()))
        ultimo_envio = running_time()
    dato = radio.receive()
    if dato:
        display.scroll(dato)
