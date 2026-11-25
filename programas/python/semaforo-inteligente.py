from microbit import *
import music

pin2.write_digital(1)
while True:
    if button_a.was_pressed():
        pin2.write_digital(0)
        pin1.write_digital(1)
        sleep(2000)
        pin1.write_digital(0)
        pin0.write_digital(1)
        display.show(Image.STICKFIGURE)
        sleep(2000)
        for i in range(5, 0, -1):
            display.show(i)
            music.pitch(880, 60)
            sleep(700)
        display.clear()
        pin0.write_digital(0)
        pin2.write_digital(1)
