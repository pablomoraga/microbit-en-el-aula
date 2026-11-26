from microbit import *

pala, x, y, dx, dy, puntos = 2, 2, 0, 1, 1, 0
while True:
    if button_a.was_pressed() and pala > 0:
        pala -= 1
    if button_b.was_pressed() and pala < 3:
        pala += 1
    display.clear()
    display.set_pixel(pala, 4, 9)
    display.set_pixel(pala + 1, 4, 9)
    display.set_pixel(x, y, 9)
    sleep(max(100, 400 - puntos * 20))
    if x + dx < 0 or x + dx > 4:
        dx = -dx
    if y + dy < 0:
        dy = 1
    if y + dy == 4:
        if x + dx == pala or x + dx == pala + 1:
            dy = -1
            puntos += 1
        else:
            break
    x += dx
    y += dy
display.scroll("Puntos " + str(puntos))
