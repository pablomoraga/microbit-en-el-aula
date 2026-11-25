from microbit import *
import radio

radio.on()
radio.config(group=20)
si = no = 0
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        si = no = 0
    elif button_a.was_pressed():
        radio.send("1")
        display.show(Image.YES)
    elif button_b.was_pressed():
        radio.send("0")
        display.show(Image.NO)
    voto = radio.receive()
    if voto == "1":
        si += 1
    elif voto == "0":
        no += 1
    if pin_logo.is_touched():
        display.scroll("SI " + str(si) + " NO " + str(no))
