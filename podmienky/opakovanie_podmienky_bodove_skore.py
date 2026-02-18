# definujte funkciu prevod_bodov_na_znamku(pocet_bodov),
# ktorá na vstup zoberie pocet ziskanych bodov a vypise
# znamku
# 9 - 10    1 # samo
# 7 - 8     2 # filip
# 5 - 6     3 # bartos # balog = 3 (mesiac pauza od pisomiek)
# 3 - 4     4 # rado
# 0 - 2     5 # balog

# osetrite mozne chybne vstupy
def prevod_bodov_na_znamku(pocet_bodov):
    if pocet_bodov >= 9 and pocet_bodov <= 10:
        print(f'Dosiahli ste {pocet_bodov} bodov, znamka 1')
    elif pocet_bodov >= 7 and pocet_bodov <= 8:
        print(f'Dosiahli ste {pocet_bodov} bodov, znamka 2')
    elif pocet_bodov >= 5 and pocet_bodov <= 6:
        print(f'Dosiahli ste {pocet_bodov} bodov, znamka 3')
    elif pocet_bodov >= 3 and pocet_bodov <= 4:
        print(f'Dosiahli ste {pocet_bodov} bodov, znamka 4')
    elif pocet_bodov >= 0 and pocet_bodov <= 2:
        print(f'Dosiahli ste {pocet_bodov} bodov, znamka 5')
    else:
        print('Chyba')

prevod_bodov_na_znamku(5)

