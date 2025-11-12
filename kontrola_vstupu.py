#V programovaní sa často stretneme so situáciou, 
# kedy potrebujeme otestovať správnosť vstupu. 
# Vtedy je najefektívnejšie si vytvoriť pomocnú 
# funkciu, ktorá to bude kontrolovať. 
# Vytvorte funkciu skontroluj_vstup(), 
# ktorá na vstup zoberie číslo a  vráti True alebo False 
# podľa toho či zadané číslo spĺňa alebo 
# nespĺňa nasledovné kritéria:
# v tomto prípade sa musí jednať o celé číslo väčšie ako nula.

def skontroluj_vstup(cislo):
    if cislo <= 0:
        print('False')    
    elif type(cislo) != int:        # funkcia type zistí datovy typ premmenej
        print('False')
    else:
        print('True')

skontroluj_vstup(5)
    