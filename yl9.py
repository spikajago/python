# 24.10.24 Steven Pikajago
# ülesanded 9 

# import random

# #Genereeri ja kuva arvud arvud 1-20
# for i in range(1,21):
#     print(i, end=" ")
# print()

# #Genereeri ja kuva 20 suvalist arvu vahemikus 1-99
# for i in range(1,21):
#     print(random.randint(1, 99), end=" ")
# print()


#Kasuta loendit 60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75
#    Leia paaris ja paaritud arvud ning lisa oma loendisse
#   Kuva paaris ja paritute arvude summad
# loend=[60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]
# paaris=[]
# paaritud=[]
# for i in loend:
#     if i%2==0:
#         paaris.append(i)
#     else:
#         paaritud.append(i)
# print(f"Paaris arvude summa on: {sum(paaris)}")
# print(f"Paaritute arvude summa on: {sum(paaritud)}")
# print()

#Kuva arvud 1-42
#    Arvud, mis jagunevad 3, lisa tekst TIK (näiteks 3 TIK)
#    Arvud, mis jagunevad 5, lisa tekst TAK (näiteks 5 TAK)
#    Kui jagunevad mõlemaga, siis lisa tekst TIKTAK (näiteks 15 TIKTAK)

# for i in range(1,43):
#     if i%3==0 and i%5==0:
#         print(i,"TIKTAK",end=" ")
#     elif i%3==0:
#         print(i,"TIK", end=" ")
#     elif i%5==0:
#         print(i,"TAK", end=" ")
#     else:
#         print(i, end=" ")
# print()


# #Kuva nimekirjast unikaalsed nimed:
# nimed = ['Martin', 'Tõnu', 'Andres', 'Tõnu', 'Andres', 'Andres', 'Andres', 'Tõnu', 'Marko', 'Mari', 'Jüri', 'Liis', 'Marko', 'Piret', 'Anu']
# unimed=[]
# for nimi in nimed:
#     if nimi not in unimed:
#         unimed.append(nimi)
# print(unimed)



#Sulle on saadetud õpilaste keskmised hinded, mille lisasid loendisse. Eralda hinded ning leia kogu rühma parim ja kehvem tulemus ning keskmine hinne.
# ryhma_hinded = ["Mari 4.9", "Jüri 3.1", "Kadri 4.6", "Marko 4.7", "Liis 4.9", "Andres 4.2", "Anu 4.7", "Martin 4.2", "Piret 4.2", "Tõnu 4.1"]
# meeles=[]

# for opilane in ryhma_hinded:
#     meeles.append(float(opilane.split(" ")[1]))

# print(f"parim tulemus {max(meeles)}")
# print(f"halvim tulemus {min(meeles)}")
# print(f"halvim tulemus {round(sum(meeles)/len(meeles),2)}")


#Koosta programm, mis genereerib ja kuvab korrutustabeli, kus iga number korrutatakse iseendaga:
#Näiteks:
#0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
# for i in range(11):
#     print(f"{i}x{i}={i*i}")


#Loo programm, mis loob suvalised tehted 1-100 arvudega.
# import random
#    Kasuta tsükli puhul alakriipsu
#    kasuta suvalise tehte märgi jaoks loendit ja sealt suvalise märgi leidmiseks random.choice()
#    Näiteks:
#    7 – 2=
#    45 * 69=
#    71 – 45=
# tehted=["+","-","*","/"]

# for _ in range(6):
#     j=random.randint(1,10)
#     k=random.randint(1,10)
#     tehe=random.choice(tehted)
#     if tehe=="+":
#           print(f"{j}+{k}=")
#           vastus=int(input("vastus: "))
#             if vastus==j+k:
#                punktid+=1
#             else:
#                print("vale")
#             elif tehe=="-":
#          print(f"{j}-{k}=")
#          vastus=int(input("vastus: "))
#             if vastus==j-k:
#                punktid+=1
#             else:
#                print("vale")
#             elif tehe=="*":
#          print(f"{j}*{k}=")
#          vastus=int(input("vastus: "))
#             if vastus==j*k:
#                punktid+=1
#             else:
#                print("vale")
#      else:
#         print(f"{j}/{k}=")
#         vastus=float(input("vastus: "))
#           if vastus==j/k:
#                punktid+=1
#             else:
#                print("vale")
# print(str((punktid/kysimuste_arv)*100)+"%")
# if punkti/kysimuste_arv>=0.5:
#     print("A")
# else:
#     print("MA")

#Täienda eelmist ülesannet ja kasutaja käest küsitakse vastust.
#
#    Õiged vastused loetakse kokku
#    Kui saab vähemalt poole punktid, siis saab A, muul juhul MA



#    kuva samasugused kujundid:

# for i in range(1,6):
#     print("*"*i)
# print()
# for i in range(1,6):
#     print("*"*(6-i))
# print()
# for i in range(1,6):
#     print(" "*(5-i)+"*"*i)
# print()
# for i in range(1,6):
#     print(" "*(-1+i)+"*"*(6-i))
# print()

# Paariarvude summa
# summa=0
# even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 3, 32, 34, 36, 38]
# for i in even_nums:
#     if i%2==0:
#          summa+=i
#     else:
#          break

# print(summa)


ev_data = [
['vehicle', 'range', 'price'],
['Tesla Model Y Long Range', '330', '58990'],
['Volkswagen ID.4 Pro', '260', '39995'],
['Ford Mustang Mach-E', '300', '42995'],
['Audi e-tron GT', '238', '102700'],
['Nissan Leaf', '149', '27400'],
['BMW iX xDrive50', '324', '83995'],
['Polestar 2', '265', '45500'],
['Kia EV6 Long Range', '310', '47795'],
['Mercedes-Benz EQS 450+', '350', '102310'],
['Hyundai Kona Electric', '258', '37400']
]

labisoit=[]
hinnad=[]
kolmsada=[]
for car in ev_data:
    if car[1]!="range" or car[2]!="price":
        labisoit.append(int(car[1]))
        if int(car[1])>=300:
            kolmsada.append(car[0])
        hinnad.append(int(car[2]))
    for i in car:
        print(f"{i:30}", end=" ")
    print()
print(f"keskmine läbisõit: {sum(labisoit)/len(labisoit)}")
print(f"keskmine hind: {sum(hinnad)/len(hinnad)}€")
print(kolmsada)



# Kuva andmed ridade kaupa, vorminda tulpadena
# Leia keskmine läbisõidu ulatus ja hind
# Kuva auto nimed, mille läbisõidu ulatus on suurem kui 300 km
# Analüüsi andmeid, et tuvastada, kas kõrgema hinnaga autodel on tõepoolest pikem läbisõidu ulatus