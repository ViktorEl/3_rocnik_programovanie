1 # vytvorte funkciu cislo_kladne(), ktorá na vstup 
# zoberie cislo

# ak je cislo kladne a menšie ako 100
# funkcia vypise som kladne mensie ako 100

# ak je cislo kladne a vacsie ako 100
# funkcia vypise som kladne vacsie ako 100

# ak je cislo kladne a vacsie ako 1000
# funkcia vypise som kladne vacsie ako 1000


def cislo_kladne(cislo):
    if cislo >= 0 and cislo < 100:
        print('som kladne mensie ako 100')
    elif cislo >= 0 and cislo >= 100 and cislo < 1000:
        print('som kladne vacsie ako 100')
    elif cislo >= 0 and cislo >= 1000:
        print('som kladne vacsie ako 1000')
 
 
cislo_kladne(50)    
cislo_kladne(120)
cislo_kladne(1500)