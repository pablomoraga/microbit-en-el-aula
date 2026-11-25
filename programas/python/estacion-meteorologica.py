from microbit import *
import radio

radio.on()
radio.config(group=10)
while True:
    radio.send("t=" + str(temperature()))
    radio.send("luz=" + str(display.read_light_level()))
    radio.send("ruido=" + str(microphone.sound_level()))
    display.show(Image.UMBRELLA)
    sleep(5000)
