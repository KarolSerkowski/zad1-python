class Stos:
    wysokoscStosu = 0
    indexNowegoElementu = 0
    zawartoscStosu = {}

    def uaktualnijWysokoscStosu(self):

        self.zawartoscStosu.items()
        self.wysokoscStosu = len(self.zawartoscStosu)
        return self.wysokoscStosu

    def wypiszIloscElementowStosu(self):
         print("Ilość elemetów stosu to: %d " % self.uaktualnijWysokoscStosu())

    def dodaj(self, kolejnyElement):
        indexNowegoElementu = int (self.uaktualnijWysokoscStosu()) + 1
        self.zawartoscStosu[indexNowegoElementu]= kolejnyElement
        self.uaktualnijWysokoscStosu()

    def wypiszZawartoscWierzchuStosu(self):
        if self.uaktualnijWysokoscStosu() > 0:
            print ("Wierzch stosu to: %s" % self.zawartoscStosu[self.wysokoscStosu])
        else:
            print ("Błąd - stos jest pusty ! Nie można wypisać wierzchu stosu")


    def usunWierzchStosu(self):
        if self.uaktualnijWysokoscStosu() > 0:
            print("Element %s został usunięty" %self.zawartoscStosu[self.wysokoscStosu])
            self.zawartoscStosu.pop(self.wysokoscStosu)
            self.uaktualnijWysokoscStosu()
        else:
            print ("Błąd - stos jest pusty ! juz nic z niego nie usuniesz")




x = Stos()
x.dodaj('test')
x.dodaj('test2')
x.dodaj('test3')
x.dodaj('test4')
x.dodaj('test5')
x.dodaj('test6')

x.usunWierzchStosu()
x.usunWierzchStosu()
x.wypiszIloscElementowStosu()
x.wypiszZawartoscWierzchuStosu()


