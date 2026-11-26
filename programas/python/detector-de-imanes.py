from microbit import *
import music

normal = compass.get_field_strength()
while True:
    campo = compass.get_field_strength()
    if button_a.was_pressed():
        normal = campo
    if button_b.was_pressed():
        display.scroll(campo)
    if campo > normal * 2:
        display.show(Image.YES)
    else:
        display.show(Image.NO)
        music.pitch(880, 250)
