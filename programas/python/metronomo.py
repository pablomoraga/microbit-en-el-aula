from microbit import *
import music

pulsos = 60
while True:
    if button_a.was_pressed() and pulsos > 40:
        pulsos -= 10
        display.scroll(pulsos)
    if button_b.was_pressed() and pulsos < 200:
        pulsos += 10
        display.scroll(pulsos)
    display.set_pixel(2, 2, 9)
    music.pitch(1000, 50)
    display.set_pixel(2, 2, 0)
    sleep(60000 // pulsos - 50)
