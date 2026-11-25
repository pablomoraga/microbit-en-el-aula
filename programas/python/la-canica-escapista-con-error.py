from microbit import *

x = 2
while True:
    ax = accelerometer.get_x()
    if ax > 200:
        x += 1
    elif ax < -200 and x > 0:
        x -= 1
    display.clear()
    if 0 <= x <= 4:
        display.set_pixel(x, 2, 9)
    sleep(150)
