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
        alien.left = x - 50
        alien.top  = y - 50
#
# powyżej kod, który pozwala zrobić prosty program - przykład do obejrzenia: https://youtu.be/1PdeXRAVUv0
# na webinarze wyjaśnię znaczenie linijek: 8-9, 15-17 oraz 21-23 
# pliki tlo i robot znajdują się w :  https://www.dropbox.com/sh/d861squ89dsi41p/AAB1FFWiR9VxwpVxZQGMDMVNa


# gra00.py
alien = Actor('robot')
alien.pos = 100, 156

WIDTH = 800
HEIGHT = 600 

def draw():
	screen.blit('tlo',(0,0))
	screen.draw.text('Halo, tu nasza gra.',  (10, 10),  fontsize=40)
	alien.draw()

def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        x , y = pos
        alien.pos = pos

############################################################################################################

# gra01.py

from random import randint

alien1 = Actor('robot')
alien2 = Actor('pirat')

alien1.pos = 100, 156

x = randint(100,700)
y = randint(100,500)

alien2.pos = x,y

WIDTH = 800
HEIGHT = 600 

def draw():
	screen.blit('tlo',(0,0))
	screen.draw.text('Halo, tu Adam Jurkiewicz.',  (10, 10),  fontsize=40)
	alien1.draw()
	alien2.draw()

def on_mouse_down(pos, button):
	if button == mouse.LEFT:
		x , y = pos
		print("Lewy klawisz myszy!",x,y)
		alien2.left = x - 50
		alien2.top  = y - 50
		
	if button == mouse.RIGHT:	
		x = randint(100,700)
		y = randint(100,500)
		alien1.pos = x , y
######################################################################################
Ankieta: https://goo.gl/forms/6Owvv92cnNxXWZDk2
		
###################################################
