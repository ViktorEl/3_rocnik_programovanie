#Pomocou meracieho pásma sme odmerali rozmery telocvične: 
# šírka 15 m a 32 cm, dĺžka 22 m a 12 cm. Koľko plechoviek 
# farby budeme potrebovať na premaľovanie podlahy telocvične,
#  ak farba z jednej plechovky vystačí na 14 m2?

import math         # importovanie/vlozenie matematickej kniznice. 
                    # po importovani vieme vyuzivat matematicke funkcie (ceil, floor, sin, ...)

sirka = 15.32
dlzka = 22.12

farba = 14

obsah = sirka * dlzka
pocet_plechoviek = obsah / farba
pocet_plechoviek = math.ceil(pocet_plechoviek)  # math.ceil() zaokruhlenie hore napríklad cislo 3.2 zaokruhli na 4
# viacslovne premenne zapisat cez podciarkovnik
# napriklad pocet_plechoviek, spotreba_auta, a pod. 

print(pocet_plechoviek)

