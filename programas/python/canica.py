from microbit import *

x, y = 2, 2
while True:
    ax, ay = accelerometer.get_x(), accelerometer.get_y()
    if ax > 200:
        x += 1
    elif ax < -200:
        x -= 1
    if ay > 200:
        y += 1
    elif ay < -200:
        y -= 1
    x = min(4, max(0, x))
    y = min(4, max(0, y))
    display.clear()
    display.set_pixel(x, y, 9)
    sleep(150)
