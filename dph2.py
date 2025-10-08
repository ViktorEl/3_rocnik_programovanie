#Vytvorte program, ktorý si od používateľa 
# vypýta cenu bez DPH, sadzbu a vypočíta a 
# vypíše konečnú cenu. 
#Napríklad sadzby na Slovensku majú momentálne 
# nasledovné sadzby DPH. 
#	základná sadzba DPH: 23 %,
#	prvá znížená sadzba DPH: 19 %,
#	druhá znížená sadzba DPH: 5 %.

cena_bez_dph = input('Zadajte cenu bez DPH:')
cena_bez_dph = float(cena_bez_dph)

sadzba = input('Zadajte vysku sadzby:')
sadzba = float(sadzba)

cena_s_dph = cena_bez_dph * (sadzba /100) + cena_bez_dph
print(cena_s_dph)
