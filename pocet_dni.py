#Vytvorte funkciu premena_tyzdnov(), 
# ktorá si od používateľa vypýta počet 
# týždňov a vypíšte koľko obsahuje dní, hodín a minút. 

def premena_tyzdnov():
    pocet_tyzdnov = input('Zadajte pocet tyzdnov:')
    pocet_tyzdnov = int(pocet_tyzdnov)
    dni = pocet_tyzdnov * 7
    hodin = dni * 24
    minut = hodin * 60
    print(f'pocet dni: {dni}, pocet hodin {hodin} pocet minut {minut}')

premena_tyzdnov()   # zavolali sme funkciu
