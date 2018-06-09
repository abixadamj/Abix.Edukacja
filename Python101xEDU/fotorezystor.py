#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fotorezystor.py
#  
#  Copyright 2018 ABIX Edukacja <adasiek@abix-edukacja>
#  
# 
from pyfirmata import *
from time import sleep

plytka = Arduino('/dev/ttyUSB0')


#### tutaj zaczynamy zabawę z czytaniem analogowego złącza
iterator = util.Iterator(plytka)
iterator.start()

czujka = plytka.get_pin('a:0:i')
czujka.enable_reporting()


while True:
    swiatlo = czujka.read()
    print('Poziom światła to:',swiatlo)

