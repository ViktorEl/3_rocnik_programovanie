#Vytvorte program, ktorý si od používateľa vypýta 
# cenu bez DPH a vypočíta a vypíše konečnú cenu. 
#Základná sadzba DPH je 23%



cena_bez_DPH = input('Zadajte sumu bez DPH:') # cez input si vypytame hodnoty od pouzivatela
cena_bez_DPH = float(cena_bez_DPH)              # pretypujeme string/retazec na float

cena_s_DPH = cena_bez_DPH * 0.23 + cena_bez_DPH
print(cena_s_DPH)               # pomocou print vypíseme cenu s dph


# 100.5     je typ float/desatinne cislo
# 100       je typ int/cele cislo
# '100'     je typ str/retazec, postupnost roznych znakov 