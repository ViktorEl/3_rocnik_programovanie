#Využite programový kód z predchádzajúcej úlohy 
# (rozdelenie detí do jednotlivých športov) 
# a vytvorte funkciu urci_sport(), ktorá pre 
# zadané pohlavie a výšku zistí a vráti názov športu, 
# v ktorom bude dieťa súťažiť.

def urci_sport(pohlavie, vyska):
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


#urci_sport('dievca', 160)
#urci_sport('chlapec', 160)
#urci_sport('dievca', 170)
