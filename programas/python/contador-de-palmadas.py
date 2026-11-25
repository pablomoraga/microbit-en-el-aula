from microbit import *

palmadas = 0
while True:
    if microphone.was_event(SoundEvent.LOUD):
        palmadas += 1
        display.scroll(palmadas)
    if button_a.was_pressed():
        palmadas = 0
        display.scroll(palmadas)
