#Na čerpacej stanici predávajú benzín, naftu a LPG. 
# Ceny pre dnešný deň boli stanovené nasledovne:
#benzín: 1,234 €/liter,
#nafta: 1,109 €/liter,
#LPG: 0,520 €/liter.

#Ak je kupujúci stálym zákazníkom, dostane zľavu 5%.
#Koľko má zaplatiť nový zákazník, ktorý natankoval 48,9 litrov benzínu?
#Koľko má zaplatiť stály zákazník, ktorý natankoval 55 litrov nafty?
#Koľko má zaplatiť stály zákazník, ktorý natankoval 45,9 litrov benzínu a 41,2 litrov LPG?
benzin = 1.234
nafta = 1.109
LPG = 0.52

zakaznik1 = benzin * 48.9
print(zakaznik1)
zakaznik2 = 55 * nafta * 0.95
zakaznik3 = (45.9 * benzin + 41.2 * LPG) * 0.95
print(zakaznik3)