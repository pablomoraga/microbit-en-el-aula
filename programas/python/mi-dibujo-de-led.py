from microbit import *

normal = Image("09090:09090:00000:90009:09990")
guino = Image("00090:99090:00000:90009:09990")

while True:
    display.show(normal)
    sleep(2000)
    display.show(guino)
    sleep(300)
