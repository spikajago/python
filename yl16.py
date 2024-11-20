# 20.11.24 Steven Pikajago
# ülesanded 16

import os
import datetime
# Skript tervitab kasutajat tema operatsioonisüsteemi sisselogimisnime alusel
nimi=os.getlogin()
print(f"Tere {nimi}!")

# Skript kuvab kasutajale praeguse töökataloogi tee
print(f"Sa oled:  {os.getcwd()}")

# Kataloogide loomine:
#     Skript küsib kasutajalt, mitu kataloogi ta soovib luua
#     Kataloogid luuakse praegusesse töökataloogi kuupäevaga märgistatud kataloogi sees, nummerdatuna (nt “1”, “2”)
kokku=3
x=datetime.datetime.now().strftime('%Y-%m-%d')
try:
    for i in range(kokku):
        kataloog=x+"_"+str(i+1)
        os.mkdir(kataloog)
        print(kataloog)
except:
    print("Sul on juba need kataloogid!")

# Kataloogi kustutamine:
#     Pärast kataloogide loomist küsib skript kasutajalt, millist äsja loodud või olemasolevat kataloogi soovitakse kustutada, esitades kataloogi nime 1, 2 jne
#     Kui sisestatud kataloogi nimi eksisteerib, kustutatakse see

valik=input("Lisa kataloog, mida kustudata: ")
try:
    os.rmdir(valik)
    print(valik + " kustutatud")
except:
    print("Mingi jama kustutamisel!")

# Kuva kuupäeva kasutas olevad kataloogid
items = os.listdir('.')
for item in items:
    if os.path.isdir(item):
        print(item)
