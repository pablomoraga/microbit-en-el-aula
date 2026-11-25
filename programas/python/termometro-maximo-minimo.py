from microbit import *

maxima = minima = temperature()
ultimo = 0
while True:
    if running_time() - ultimo > 1000:
        t = temperature()
        maxima = max(maxima, t)
        minima = min(minima, t)
        ultimo = running_time()
    if button_a.is_pressed() and button_b.is_pressed():
        maxima = minima = temperature()
        display.show(Image.YES)
    elif button_a.was_pressed():
        display.scroll(maxima)
    elif button_b.was_pressed():
        display.scroll(minima)
