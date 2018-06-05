#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kod_morse.py
#  
#  Copyright 2018 ABIX Edukacja <adasiek@abix-edukacja>
#  

from pyfirmata import *
from time import sleep

#definicja kodu

morse = { 'a' : '.-' , 'b' : '-..*.' , 'c' : '.-.-' , 'd' : '-..' , 
		  'e' : '.' , 'f' : '..-.', 'g' : '--.' , 'h' : '....' ,
		   }

'''
uwaga - kod niekompletny, ale proszę zauważyć, że na końcu
jest znak przecinka mimo, że dalej nic nie ma
to daje możliwości lepszej edycji kodu.... dobra praktyka
'''

# definicja obiektu
plytka = Arduino('/dev/ttyUSB0')

# definicje funkcji
def swiec( obiekt_arduino, pin , znak ):
	'''
	obiekt_arduino ( obiekt stworzony z klasy Arduino )
	pin - numer pinu napłytce (integer)
	znak - '.' lub '-' (string)
	'''
	if znak == '.':
		obiekt_arduino.digital[ pin ].write(0)
		sleep(0.1)
		obiekt_arduino.digital[ pin ].write(1)
		sleep(0.4)
		obiekt_arduino.digital[ pin ].write(0)
	if znak == '-':
		obiekt_arduino.digital[ pin ].write(0)
		sleep(0.1)
		obiekt_arduino.digital[ pin ].write(1)
		sleep(0.7)
		obiekt_arduino.digital[ pin ].write(0)
	if znak == '*':
		obiekt_arduino.digital[ 11 ].write(0)
		for i in range(100,1,-1):
			obiekt_arduino.digital[ 11 ].write(1/i)
			sleep(0.01)
		for i in range(1,100):
			obiekt_arduino.digital[ 11 ].write(1/i)
			sleep(0.01)
		obiekt_arduino.digital[ 11 ].write(0)



# teraz testowy string do wyswietlania, do wyboru ;-)

# napis = 'befaBghAdbh'.lower()
napis = 'beddhgdeaabccdd'

for litera in napis:
	znaczek = morse[litera]
	print('Litera ' + litera + ' => ' + znaczek)
	for kod in znaczek:
		swiec(plytka, 8, kod)
