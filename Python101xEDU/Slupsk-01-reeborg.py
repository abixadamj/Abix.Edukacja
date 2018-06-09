from library import *
from random import randint

wschod()
move()
turn_left()
do_przodu(2)
w_prawo()
move()
while object_here():
    take()
move()
iloscr = randint(1,10)
print(iloscr)
plecak = carries_object()
w_prawo()
do_przodu(2)
w_prawo()
do_przodu(7)
take()
wschod()
do_przodu(5)
w_prawo()
do_przodu(4)
odloz(plecak,'strawberry')
wschod()
move()


# Biblioteka
################
def w_prawo():
    for i in range(3):
        turn_left()
        
def wschod():
    while not is_facing_north():
        turn_left()
    w_prawo()
    
def do_przodu(ile):
    for i in range(ile):
        move()
    
def odloz(p, co):
    ile = p[co]
    for i in range(ile):
        put(co)
    
