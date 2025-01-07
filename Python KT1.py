
# ÜLESANNE 1 - Sisemine hääl

# KÕIK SUURTÄHTEDEGA KIRJUTAMINE ON NAGU KARJUMINE.
# Vahel on parem kasutada oma „sisemist häält" ja kirjutada täielikult väikeste tähtedega.

# Failis nimega sisemine_haal.py loo programm Pythonis, mis küsib kasutajalt sisendit ja väljastab selle sama sisendi väikeste tähtedega. Kirjavahemärgid ja tühikud peavad jääma muutmata.
# Sul on vabadus, kuid mitte kohustus, lisada sisestuskäsule oma tekst, näiteks andes input-ile enda sõne argumendiks.

# sisend=input("mis on teie sisend? ")
# print(sisend.lower())
# print("huvitav vastus")



# ÜLESANNE 3 - Einstein

# Isegi kui sa pole füüsikat (hiljuti või üldse!) õppinud, oled ilmselt kuulnud valemist E=mc², kus:

#     E tähistab energiat (mõõdetuna džaulides)
#     m tähistab massi (mõõdetuna kilogrammides)
#     c tähistab valguse kiirust (ligikaudu 300 000 000 meetrit sekundis)

# Albert Einsteini ja tema kaasautorite järgi tähendab see valem sisuliselt, et mass ja energia on ekvivalentsed.

# Failis nimega einstein.py loo programm Pythonis, mis küsib kasutajalt massi täisarvuna (kilogrammides) ja väljastab ekvivalendi energia džaulides täisarvuna. Eelda, et kasutaja sisestab alati täisarvu.

# mass=int(input("Mis on mass(kg)? "))
# c=300000000*300000000
# e=mass*c
# print(e)


# ÜLESANNE 8 - NämNaäm

# Oletame, et tavaks on süüa:
#     Hommikusööki vahemikus 7:00 – 8:00
#     Lõunasööki vahemikus 12:00 – 13:00
#     Õhtusööki vahemikus 18:00 – 19:00

# Oleks ju tore, kui sul oleks programm, mis ütleb sulle, millal on aeg süüa?
# Failis sook.py loo programm, mis küsib kasutajalt aega ja väljastab, kas on aeg hommikusöögiks, lõunasöögiks või õhtusöögiks. Kui pole söögi aeg, ei väljasta programm midagi.

# Eelda, et kasutaja sisestab aja 24-tunnises formaadis:

#     #:## või ##:##

# Ja eelda, et iga söögiaja vahemik on kaasav. Näiteks, kui aeg on 7:00, 7:01, 7:59 või 8:00, on aeg hommikusöögiks.
# Programmi struktuur peaks olema järgmine:
#     teisenda aeg (str) 24-tunnises formaadis vastavaks arvuks (float).
#     Näiteks, kui antakse aeg "7:30", tagastab funktsioon 7.5.
#     programm kontrollib aja alusel, kas on hommiku-, lõuna- või õhtusöögi aeg, ja väljastab vastava teate.


aeg=input("Mis kell on praegu? ")
if aeg==7==8:
    print("Hommikusöögi aeg")
else:
    print()




