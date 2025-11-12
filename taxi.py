#Vytvorte funkciu cena_za_taxi(), 
#ktorá vypočíta a vráti cenu za odvoz taxíkom.
#Cenník taxi služby je nasledovný:
#- štartovné – 1,00 €
#- cena za km – 0,90 €
#- minimálne jazdné – 3,00 €

def cena_za_taxi(pocet_km):
    startovne = 1
    spolu_za_km = pocet_km * 0.9
    suma_spolu = startovne + spolu_za_km
    if suma_spolu < 3:
        print('platite 3 eura')
    else:
        print(suma_spolu)

cena_za_taxi(5.5)