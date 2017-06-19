
from pyfirmata import *
from time import sleep

plytka = Arduino('/dev/ttyUSB0')

pin11 = plytka.get_pin('d:11:p')
pin13 = plytka.get_pin("d:13:o")


while True:
    pin11.write(True)
    sleep(0.03)
    pin13.write(True)
    sleep(0.06)
    pin11.write(False)
    sleep(0.03)
    pin13.write(False)
    sleep(0.1)




while True:
    for i in range(100):
        sleep(0.02)
        pin11.write(i/100)
    sleep(0.1)
    for i in range(100,1,-1):
        sleep(0.02)
        pin11.write(i/100)
    sleep(0.3)


#### tutaj zaczynamy zabawę z czytaniem analogowego złącza
iterator = util.Iterator(plytka)
iterator.start()

czujka = plytka.get_pin('a:0:i')
czujka.enable_reporting()




while True:
    swiatlo = czujka.read()
    print('Poziom światła to:',swiatlo)



while True:
    swiatlo = czujka.read()
    print('Poziom światła to:',swiatlo)
    if swiatlo > 0.3:
        pin13.write(False)
    else:
        print('Trochę za ciemno...',swiatlo)
        pin13.write(True)
    pin11.write(swiatlo)
