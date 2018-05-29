
# Uwaga ! pierwsza funkcja wyświetla wynik na ekranie, a druga przekazuje wartość.

def nazwa(a,b):
    print(a+b)

# Druga funkcja ma też samoopisujacy sie kod.

def nazwa2(a,b):
    '''
    To jest moja dokumentacja
    a,b - wartości całkowite
    zwraca sumę a+b
    '''
    return a+b

def funkcja_z_if(litera):
    literka = litera.lower()
    if literka=='a':
        print('a..')
    elif literka=='b':
        print('b...')
    elif literka=='c':
        print('c...')
    else:
        print('zupełnie nie znam tej literki...',literka)
        
# Efekt działania powyższej funkcji w Ipython QT Console
# funkcja_z_if('a')
# a..

# funkcja_z_if('x')
# zupełnie nie znam tej literki... x

# funkcja_z_if('B')
# b...

