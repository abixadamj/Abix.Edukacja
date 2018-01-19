class Torebka(object):
    '''
    Tego opisu i tak nie widzimy
    '''
    def __init__(self, zawartosc, nazwa='Torebeczka'):
        '''
        Tu __init__ - co podajemy na starcie, czyli:
        elementy początkowe listy
        nazwę naszej torebki (Domyślnie: Torebeczka)
        '''
        self.zawartosc_torebki = []
        self.ilosc_elementow = 0 
        self.nazwa_torebki = nazwa
        for element in zawartosc:
            self.zawartosc_torebki.append(element)
        self.ilosc_elementow = len(self.zawartosc_torebki)      

    def dodaj(self,element):
        '''
        dodaj pojedynczy element do listy
        zwiększa licznik ilości pozycji
        '''
        self.ilosc_elementow += 1
        self.zawartosc_torebki.append(element)

    def pokaz(self):
        '''
        listuje zawartość naszej listy / torebki
        '''
        print('Zawartość torebki o nazwie: '+ self.nazwa_torebki)
        print('Ilość elementów: '+ str(self.ilosc_elementow))
        for elem in self.zawartosc_torebki:
            print('Element: '+ elem)
            
            
            
# definicja klasy z polem, które jest widoczne w klasie, a nie tylko w obiekcie

class Torebka2(object):
    '''
    Tego opisu i tak nie widzimy
    '''
    liczba_torebek = 0 
    
    def __init__(self, zawartosc, nazwa='Torebeczka'):
        '''
        Tu __init__ - co podajemy na starcie, czyli:
        elementy początkowe listy
        nazwę naszej torebki (Domyślnie: Torebeczka)
        '''
        self.zawartosc_torebki = []
        self.ilosc_elementow = 0 
        self.nazwa_torebki = nazwa
        for element in zawartosc:
            self.zawartosc_torebki.append(element)
        self.ilosc_elementow = len(self.zawartosc_torebki)      
        Torebka2.liczba_torebek += 1

    def dodaj(self,element):
        '''
        dodaj pojedynczy element do listy
        zwiększa licznik ilości pozycji
        '''
        self.ilosc_elementow += 1
        self.zawartosc_torebki.append(element)

    def pokaz(self):
        '''
        listuje zawartość naszej listy / torebki
        '''
        print('Zawartość torebki o nazwie: '+ self.nazwa_torebki)
        print('Ilość elementów: '+ str(self.ilosc_elementow))
        for elem in self.zawartosc_torebki:
            print('Element: '+ elem)
