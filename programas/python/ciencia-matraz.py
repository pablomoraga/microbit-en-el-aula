from microbit import *

M1 = Image("09990:00900:09090:90009:99999")
M2 = Image("00900:00900:09090:99099:99999")
while True:
    if pin_logo.is_touched():
        display.scroll("La ciencia es cosa de todas")
    display.show(M1)
    sleep(400)
    display.show(M2)
    sleep(400)
