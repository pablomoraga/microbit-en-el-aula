from microbit import *
import radio

radio.on()
radio.config(group=1)
while True:
    if button_a.was_pressed():
        radio.send("Hola")
    mensaje = radio.receive()
    if mensaje == 1:
        display.scroll(mensaje)
