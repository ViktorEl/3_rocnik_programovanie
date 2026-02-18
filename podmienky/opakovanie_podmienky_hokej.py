# definujte funkciu hokejovy_zapas(skore_prvy_tim, skore_druhy_tim)
# ktorá porovná aktuálne skore obidvoch tímov a vypíše kto 
# vyhral
# •	Názov programu: Na začiatok skriptu pridajte názov programu (napríklad: 
#---Program pre porovnanie skore---), ktorý sa prehľadne zobrazí v termináli. Tento názov musí byť prvou vecou, ktorú používateľ po spustení uvidí. 

print('--Program pre porovnanie skore--')

def hokejovy_zapas(skore_prvy_tim, skore_druhy_tim):
    if skore_prvy_tim > skore_druhy_tim:
        print('vitaz prvý tím')
    elif skore_druhy_tim > skore_prvy_tim:
        print('vitaz druhy tím')
    elif skore_prvy_tim == skore_druhy_tim:
        print('remiza')
    #else:
    #   print('zapas skoncil remizou')

# VSTUPY OD POUZIVATELA
skore_prvy_tim = input('Zadajte goly prvého timu:') # POZOR TOTO VRATI STRING (RETAZEC)
skore_prvy_tim = int(skore_prvy_tim)
skore_druhy_tim = input('Zadajte goly druheho timu:')
skore_druhy_tim = int(skore_druhy_tim)

hokejovy_zapas(skore_prvy_tim, skore_druhy_tim)
