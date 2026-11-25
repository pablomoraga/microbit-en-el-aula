from microbit import *
import music

while True:
    if button_a.was_pressed():
        display.show(Image.HOUSE)
        music.pitch(988, 100)
        sleep(50)
        music.pitch(988, 100)
    if button_b.was_pressed():
        display.show(Image.MUSIC_CROTCHET)
        music.play(["C4:4", "E4:4", "G4:4", "C5:4"])
