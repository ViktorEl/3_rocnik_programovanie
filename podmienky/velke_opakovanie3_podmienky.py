print('---Program na konvertovanie ciselnych znamok na slovny ekvivalent---')

def slovne_hodnotenie(znamka):
    if znamka == 1:
        print(f'Slovny ekvivalent znamky {znamka} je: vyborný')
    elif znamka == 2:
        print(f'Slovny ekvivalent znamky {znamka} je: chválitebny')
    elif znamka == 3:
        print('dobry')
    elif znamka == 4:
        print('dostatocny')
    elif znamka == 5:
        print('nedostatocny')
    else:
        print('Chyba: zadali ste neexistujucu znamku')

znamka = input('Zadajte znamku od 1 do 5:')
znamka = int(znamka)

slovne_hodnotenie(znamka)



