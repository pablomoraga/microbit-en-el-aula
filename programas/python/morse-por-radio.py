from microbit import *
import radio
import music

radio.on()
radio.config(group=5)
while True:
    if button_a.was_pressed():
        radio.send(".")
    if button_b.was_pressed():
        radio.send("-")
    senal = radio.receive()
    if senal == ".":
        display.show(Image("00000:00000:00900:00000:00000"))
        music.pitch(698, 200)
        display.clear()
    elif senal == "-":
        display.show(Image("00000:00000:99999:00000:00000"))
        music.pitch(698, 600)
        display.clear()
