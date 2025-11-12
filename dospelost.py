
# Vytvorte funkciu dospelost(), 
# ktorá pre zadaný vek vráti či už bola 
# dosiahnutá dospelosť alebo nie. 

def dospelost(vek):         # definovanie funkcie
    if vek >= 18:           # telo funkcie
        print('dospelý')    #telo funkcie
    else:                   # telo funkcie
        print('este nie ste dospelý')   # telo funkcie


vek = input('Zadajte vas vek:')     # vytvorenie premennej vek a ziskanie informacie od pouzivatela
vek = int(vek)  # pretypovanie veku na cele cislo 

dospelost(vek)       # zavolanie funkcie