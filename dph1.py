#Vytvorte program, ktorý si od používateľa vypýta 
# cenu bez DPH a vypočíta a vypíše konečnú cenu. 
#Základná sadzba DPH je 23%

cena_bez_DPH = input('Zadajte sumu bez DPH:')

cena_s_DPH = cena_bez_DPH * 23 / (100+23)
print(cena_s_DPH)