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

morse = { 'a' : '.-' , 'b' : '-...' , 'c' : '.-.-' , 'd' : '-..' , 
		  'e' : '.' , 'f' : '..-.', 'g' : '--.' , 'h' : '....' ,
		  'i' : '.' , 'j' : '..-.', 'k' : '--.' , 'l' : '..--' ,
		  'e' : '.-' , 'f' : '..-.', 'g' : '--.' , 'h' : '....' ,
		  'e' : '.' , 'f' : '..-.', 'g' : '--.' , 'h' : '....' ,
		  'e' : '.' , 'f' : '..-.', 'g' : '--.' , 'h' : '....' ,
		  'e' : '.' , 'f' : '..-.', 'g' : '--.' , 'h' : '....' ,
			  }
		   

'''
uwaga - kod niekompletny, ale proszę zauważyć, że na końcu
jest znak przecinka mimo, że dalej nic nie ma
to daje możliwości lepszej edycji kodu.... dobra praktyka
'''


# definicje funkcji
def swiec( obiekt_arduino, pin , znak ):
	'''
	obiekt_arduino ( obiekt stworzony z klasy Arduino )
	pin - numer pinu napłytce (integer)
	znak - '.' lub '-' (string)
	'''
	if znak == '.':
		siwec_dioda(obiekt_arduino, pin , 0.4)
	if znak == '-':
		siwec_dioda(obiekt_arduino, pin , 0.7)

def siwec_dioda(obiekt_arduino, pin , czas):
	obiekt_arduino.digital[ pin ].write(0)
	sleep(0.1)
	obiekt_arduino.digital[ pin ].write(1)
	sleep(czas)
	obiekt_arduino.digital[ pin ].write(0)
		
# teraz testowy string do wyswietlania, do wyboru ;-)

# napis = 'befaBghAdbh'.lower()
napis = 'beddhgdeaabccdd'

# definicja obiektu połączenia do Arduino
plytka = Arduino('/dev/ttyUSB0')
truskawka = Arduino('/dev/ttyUSB1')

for lqlk in napis:
	znaczek = morse[lqlk]
	print('Litera ' + lqlk + ' => ' + znaczek)
	for kod in znaczek:
		swiec(plytka, 13, kod)
		swiec(truskawka, 13, kod)
