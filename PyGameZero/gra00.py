#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

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
        # alien.left = x - 50
        # alien.top = y - 50
        
