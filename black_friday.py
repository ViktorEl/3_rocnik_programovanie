#Podmienka uplatnenia zľavy na nákup:
#nákup musí byť v hodnote nad 100 eur
#  inak sa zľava na nákup nevzťahuje.

#VIP                                        #Klasik                                                                      2. Klasik
#nad 100€ do 200€ vrátane zľava 10%          5%
#nad 200€ do 400€ vrátane zľava 15%          8%
#nad 400                 zľava 20%           10%                                         10%

#Vytvorte funkciu, celkova_cena_nakupu(), 
# ktorá vypočíta celkovú sumu nákupu 
# po zohľadnení zľavy. 
#Funkcia zoberie na vstup sumu nákupu a 
# údaj či zákazník je vlastníkom vernostnej 
# karty alebo nie a na základe týchto parametrov 
# vráti celkovú sumu nákupu. 

def celkova_cena_nakupu(suma, karta):
    if suma < 0:
        print('chyba')
    elif suma <= 100:
        print(suma)
    elif karta == 'ano' and suma > 100 and suma <= 200:
        suma = suma * 0.9
        print(suma)
    elif karta == 'nie' and suma > 100 and suma <= 200:
        suma = suma * 0.95
        print(suma)
    elif karta == 'ano' and suma > 200 and suma <= 400:
        suma = suma * 0.85
        print(suma)

    
celkova_cena_nakupu(150, 'ano')
