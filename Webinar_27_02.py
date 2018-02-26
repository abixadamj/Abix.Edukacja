#!/usr/bin/env python3
#
# Kod gry, którą będziemy tworzyć w oparciu o bibliotekę pyGame ZERO : https://pypi.python.org/pypi/pgzero/
# dokumentacja biblioteki: https://pygame-zero.readthedocs.io/en/stable/
# System, w którym już wszystko mamy: https://free-desktop.pl
#
#
alien = Actor('robot')
alien.pos = 100, 156

WIDTH = 800
HEIGHT = 600 

def draw():
	screen.blit('tlo',(0,0))
	screen.draw.text('Halo, tu nasza gra.',  (10, 10),  fontsize=40)
	alien1.draw()

def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        x , y = pos
        alien1.left = x - 50
        alien1.top  = y - 50
#
# powyżej kod, który pozwala zrobić prosty program - przykład do obejrzenia: https://youtu.be/1PdeXRAVUv0
# na webinarze wyjaśnię znaczenie linijek: 8-9, 15-17 oraz 21-23 
# pliki tlo i robot znajdują się w :  https://www.dropbox.com/sh/d861squ89dsi41p/AAB1FFWiR9VxwpVxZQGMDMVNa
