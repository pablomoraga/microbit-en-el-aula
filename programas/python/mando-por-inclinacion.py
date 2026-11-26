from microbit import *
import radio

radio.on()
radio.config(group=7)
flechas = {"1": Image.ARROW_N, "2": Image.ARROW_S, "3": Image.ARROW_W, "4": Image.ARROW_E}
while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    if y < -300:
        radio.send("1")
    elif y > 300:
        radio.send("2")
    elif x < -300:
        radio.send("3")
    elif x > 300:
        radio.send("4")
    else:
        radio.send("0")
    codigo = radio.receive()
    if codigo in flechas:
        display.show(flechas[codigo])
    elif codigo == "0":
        display.clear()
    sleep(200)
