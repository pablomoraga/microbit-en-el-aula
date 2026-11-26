from microbit import *
import music
import math

armada = False
sonando = False
while True:
    if button_a.was_pressed():
        display.show(Image.YES)
        sleep(1000)
        display.clear()
        armada = True
    if button_b.was_pressed():
        armada = False
        sonando = False
        display.clear()
    x, y, z = accelerometer.get_values()
    if armada and math.sqrt(x * x + y * y + z * z) > 1500:
        sonando = True
    if sonando:
        display.show(Image.NO)
        music.pitch(880, 150)
        music.pitch(440, 150)
