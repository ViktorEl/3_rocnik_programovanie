
def cena_nakupu(pocet, jednotkova_cena):
    if pocet <= 20:
        celkova_suma = 20 * jednotkova_cena
        print(celkova_suma)
    elif pocet > 20:
        suma_prvych_20 = jednotkova_cena * 20
        suma_zvysne_kusy = (jednotkova_cena * (pocet-20)) * 0.90
        celkova_suma = suma_prvych_20 + suma_zvysne_kusy
        print(celkova_suma)

cena_nakupu(20, 1)