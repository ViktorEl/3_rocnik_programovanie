# v tejto casti si zopakujeme funkcie a podmienky
# if    je hlavná podmienka, zaciname stále podmienkou if
# elif  ak hlavna podmienka nie je splnena kontroluje sa podmienka pod nou podmienkou elif
# else  ak ani jedna z predchadzajucich podmienok nie je splnena vykona sa riadok else

# Vytvorte/Definujte funkciu sucet(cislo1, cislo2), ktora ako
# vstupne parametre zoberie dve cisla a vypise vysledok
# vypytajte si vstupne parametre od pouzivatela

def sucet(cislo1, cislo2):
    vysledok = cislo1 + cislo2
    print(vysledok)

cislo1 = input('Zadajte prve cislo:') # toto je vstup od pouzivatela vypise text dole terminaly
cislo1 = float(cislo1)
cislo2 = input('zadajte druhe cislo:') # vstup od pouzivatela, vracia hodnotu v stringu (v retazci)
cislo2 = float(cislo2) # pretoze sme pouzili prikaz input() tzn. vstup od pouzivatela
# input nam stále ulozi do premennej string, preto ho musime pretypovat bud na float alebo int

sucet(cislo1, cislo2)

