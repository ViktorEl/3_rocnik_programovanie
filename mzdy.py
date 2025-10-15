#Vytvorte program, v ktorom používateľ zadá počet 
# odpracovaných hodín za mesiac a hodinovú mzdu a vypočíta 
# celkovú mesačnú mzdu. 

pocet_hodin = input('zadajte pocet odpracovanych hodin za mesiac:')
hodinova_mzda = input('zadajte vasu hodinovu mzdu:')
pocet_hodin = float(pocet_hodin)
hodinova_mzda = float(hodinova_mzda)

celkova_mesacna_mzda = pocet_hodin * hodinova_mzda
print(f'Vasa hruba mzda za tento mesiac je {hodinova_mzda}')

