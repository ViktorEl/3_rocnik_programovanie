pohlavie = input('zadajte pohlavie:')
vyska = input('Zadajte vysku:')
vyska = float(vyska)

if pohlavie == 'chlapec':
    if vyska < 160:
        print('futbal') 
    elif vyska <= 180:
        print('vodne polo')
    else:
        print('basketbal')
if pohlavie == 'dievca':
    if vyska < 160:
        print('akvabely')
    elif vyska <= 170:
        print('tenis')
    else:
        print('volejbal')