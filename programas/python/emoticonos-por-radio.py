from microbit import *
import radio

radio.on()
radio.config(group=2)
while True:
    if button_a.was_pressed():
        radio.send("1")
    if button_b.was_pressed():
        radio.send("2")
    if pin_logo.is_touched():
        radio.send("3")
        sleep(300)
    codigo = radio.receive()
    if codigo == "1":
        display.show(Image.HAPPY)
    elif codigo == "2":
        display.show(Image.SAD)
    elif codigo == "3":
        display.show(Image.HEART)
