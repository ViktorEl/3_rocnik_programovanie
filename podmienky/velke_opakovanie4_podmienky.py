
print('---Program na urcenie typu listku podla veku')

def typ_listka(vek):
    if vek < 0:
        print('zadali ste zaporne cislo')
    elif vek < 6:
        print('detsky')
    elif vek <= 15:
        print('student zlavneny')
    elif vek <= 18:
        print('studentsky')
    elif vek > 18 and vek <= 60:
        print('dospely')
    elif vek > 60 and vek < 110:
        print('dochodca')
    else:
        print('zadali ste chybne cislo')


typ_listka(50)