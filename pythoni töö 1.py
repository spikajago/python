# Steven Pikajago 05.12.2024
# töö 1


# 1.1. Tervitus

# print("Tere, maailm!")


# 1.2. Aasta liblikas

# aasta=2020
# liblikas=" teelehe-mosaiikliblikas "
# lause_keskosa=". aasta liblikas on "
# lause=str(aasta)+" "+lause_keskosa+" "+liblikas
# print(lause)


# 1.3. Pilved

# pilvedekorgus=int(input("Mis on pilvekõrgus km? "))
# if pilvedekorgus>6:
#     print("Ülemiste pilvede alus on kõrgemal kui 6 km, keskmistel pilvedel on 2-6 km kõrgusel, alumistel pilvedel on madalamal kui 2 km.")
# else:
#     print("Need ei ole ülemised pilved")

# 1.4. Bussid

# kohad= 40
# inimesed= 60
# bussid=inimesed//kohad
# viimases_bussi=inimesed%kohad
# if viimases_bussi==0:
#     print(f"Busse on vaja {bussid} bussi, viimases bussis on {kohad} kohta")
# else:
#     print(f"Busse on vaja {bussid} bussi, bussis on {viimases_bussi} kohta")
    
# 2.1 Äratus
# Aratus=int(input("Sisestage mitu korda äratada "))
# for i in range(Aratus):
#     print("Tõuse ja sära")
    
# 2.2 Murelikud lapsevanemad
# ringide_arv=int(input("Sisesta ringide arv "))
# i=1
# porgandite_arv=0
# while i <= ringide_arv:
#     if i%2==0:
#         porgandite_arv
# print(f"porgandite koguarv on: {porgandite_arv}")

#2.3 Täringud
# import random
# Taring=int(input("Täringute arv "))
# for i in range(Taring):
#     print(random.randint(1,6))

#2.4 Male
# arv=10
# nisutera=0
# korda=arv

# if arv >64:
#     print("nii palju ruute ei pole")

# if arv>= 1:
#     nisutera+=1
#     korda-=1

# while korda>=1:
#     nisutera *=2
#     korda -=1

# print(nisutera)

# 2.5 Õunad
# import random
# ounu=14
# poisse=4
# for i in range(poisse):
#     ounu-=random.randint(1,2)
# print(ounu)

# 3.1 Ülikooli vastuvõetud
# fail=open("rebased.txt", encoding="UTF-8")
# vastuvõetud=[]
# for rida in fail:
#     vastuvõetud.append(int(rida))
# print(vastuvõetud)
# fail.close()

# a=input("palun sisesta; millise aasta andmeid vajate? ")
# print(vastuvõetud[int(a[3])-1])

# 3.2 Jänesevanemate mure ver.3
# ringide_arv=int(input("Sisesta ringide arv "))
# i=1
# porgandite_arv=0
# for i in range(ringide_arv):
#     if i%2==0:
#         porgandite_arv
# print(f"porgandite koguarv on: {porgandite_arv}")

# 3.3 Sissetulekud
# fail=open("konto.txt", encoding="UTF-8")
# for rida in fail:
#     if float(rida) >0:
#         print(rida)

# 3.4 Jukebox
