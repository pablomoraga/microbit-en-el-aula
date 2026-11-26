from microbit import *

while True:
    mv = pin1.read_analog() * 3300 // 1023
    if button_a.was_pressed():
        display.scroll(mv)
    if mv > 1400:
        display.show(Image.YES)
    elif mv > 1200:
        display.show(Image.ASLEEP)
    else:
        display.show(Image.NO)
    sleep(200)
