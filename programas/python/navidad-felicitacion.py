from microbit import *
import radio

radio.on()
radio.config(group=25)
while True:
    if button_a.was_pressed():
        radio.send("Felices fiestas")
    mensaje = radio.receive()
    if mensaje:
        audio.play(Sound.TWINKLE, wait=False)
        display.scroll(mensaje)
