from microbit import *

while True:
    x = accelerometer.get_x()
    if x < -150:
        display.show(Image.ARROW_W)
    elif x > 150:
        display.show(Image.ARROW_E)
    else:
        display.show(Image.YES)
