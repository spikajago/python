# 29.11.24 Steven Pikajago
# ülesanded 17


# Pangakonto – pangakonto.txt

#     Sinu ülesandeks on kirjutada Pythoni skript, mis loeb andmeid failist pangakonto.txt. Fail sisaldab eraldi ridadel pangatehingute summasid: positiivsed summad tähistavad sissetulekuid ja negatiivsed summad väljaminekuid. Skript peab arvutama ja väljastama:
#         kogu tehingute arvu
#         positiivsete tehingute arvu
#         positiivsete tehingute kogusumma
#     Tulemused tuleb väljastada konsool
# fail=open("pangakonto.txt")
# loend=fail.readlines()
# positiivsed=[]
# for i in loend:
#       if float(i)>0:
#             positiivsed.append(float(i))
# print(len(loend)) #tehinguid kokku 100
# print(positiivsed)


# Palgastatistika – palgad.txt

#     Kirjuta Pythoni skript, mis loeb failist palgad.txt töötajate andmed ja arvutab eraldi
#         meeste keskmised  palk
#         naiste keskmised  palk
#     Tulemused prindi konsooli
mpalgad=[]
npalgad=[]

fail=open("palgad.txt")
loend=fail.readlines()
for i in loend:
    sugu=i.split(",")[3]
    palk=i.split(",")[6]
    if sugu=="Mees":
        mpalgad.append(float(palk))
    else:
        npalgad.append(float(palk))
print(mpalgad)
avg = sum(mpalgad) / len(mpalgad)
print(avg)



# Palgatõendid – palgad.txt

#     Kirjuta Pythoni skript, mis loeb failist palgad.txt töötajate andmed ja genereerib iga töötaja kohta eraldi palgatõendi.
#     Tõendid salvesta kausta, mille nimi on käesolev kuu ja aasta (näiteks 02.2025).
#     Failinimeks kasuta formaati ID_Nimi.txt (näiteks 1_Robin.txt). Iga palgatõendi sisu peab olema järgnev:
#     Nimi: [Nimi]
#     Isikukood: [Isikukood]
#     Sugu: [Sugu]
#     Töötunnid: [Töötunnid]
#     Tunnitasu: [Tunnitasu]€
#     Makstav tasu: [Palk]
