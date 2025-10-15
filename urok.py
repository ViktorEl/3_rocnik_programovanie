#Vytvorte program, ktorý si od používateľa vypýta vklad 
# a úrokovú mieru v % a vypočíta a vypíše zisk z úroku za 
# jeden rok a aj celkovú sumu peňazí po jednom roku. 
#Pomôcka: použite formátovaný string / fstring
# f'Zisk z uroku = {nazov_premennej1} a celkova suma = {nazov_premennej2}'

vklad = input('Zadajte vysku vkladu:')
urok_v_percentach = input('zadajte vysku uroku v %:')
vklad = float(vklad)
urok_v_percentach = float(urok_v_percentach)

zisk = urok_v_percentach * vklad / 100
celkova_suma = vklad + zisk
# print(zisk)
# print(celkova_suma)
print(f'Vas zisk z urokov je:{zisk} a celkova suma po 1 roku je {celkova_suma}')
# ()    -> shift + ä
# []    -> pravý alt Gr + F
# {}    -> pravy alt Gr + B
# ''    -> pravy alt Gr + P
# f''   -> fstring alebo inak formátovany string