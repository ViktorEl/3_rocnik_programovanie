print('Vekové kategórie')
vek = input('Zadaj vek človeka rokoch: ')
vek = float(vek)

if vek < 0:
    print('chyba zadali ste zaporne cislo')
elif vek == 0:
    print('Novorodenec alebo dojča')
elif vek <= 3:
    print('Batoľa')
elif vek <= 6:
    print('Predškolský vek')
elif vek <=  12:
    print('Mladší školský vek')
elif vek <= 15:
    print('Starší školský vek')
elif vek <= 18:
    print('Puberta')
elif vek < 70:    
    print('Dospelý')
else:
    print('Staroba')

