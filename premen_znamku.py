#Pomôžte učiteľovi vytvoriť program, 
# ktorý mu uľahčí známkovanie žiakov. 
#Vytvorte funkciu premen_na_znamku(), 
# ktorá na vstup zoberie dosiahnuté percentá a 
# vráti príslušnú známku. 
#<90, 100>	1
#<75, 90)	2     
#<55, 75)	3     
#<40, 55)	4    
#(40, 0>5      

def premen_na_znamku(percenta):
    if percenta >= 90 and percenta <= 100:
        print(1)
    elif percenta >= 75 and percenta < 90:
        print(2)
    pass
    
