# -*- coding: utf-8 -*-
"""
ABIX

Skrypt dla samouczka #4
"""

from time import sleep

high = 100
low = 0
guess = (high + low)/2  
count = 0
epsilon = 0.1

print('Wymyśl liczbę od 0 do 100!')

guessing = True
while guessing:

    count += 1
    print('Czy liczba to ' + str(guess) + '?')
    print(" 'h' - zbyt wysoko. 'l' - zbyt nisko. 'c' - wynik poprawny")
    pointer = input("Podaj: ")
    
    if pointer == 'h':
        high = guess
        guess = (low + guess)/2

    elif pointer == 'l':
        low = guess
        guess = (high + guess)/2

    elif pointer == 'c':
        guessing = False

    else:
        print('Sorry, nie rozumiem....')
        
    print('To się zawsze wykona...')
    sleep(1)
    
print('Koniec - wynik: ' + str(guess)+', ile testów: '+str(count) )
