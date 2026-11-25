from microbit import *
import music

GOTA = Image("00900:09990:99999:99999:09990")
while True:
    if button_a.was_pressed():
        display.show(Image.YES)
        sleep(60000)
        for i in range(5):
            display.show(GOTA)
            music.pitch(988, 250)
            display.clear()
            sleep(300)
