# 15.11.24 Steven Pikajago
# ülesanded 12



# Looge funktsioon, mis võimaldab lisada või eemaldada summasid pangakontolt.
# Funktsioon peaks algama algse saldoga ja võimaldama teha operatsioone: deposiit (raha lisamine) ja väljavõte (raha eemaldamine). Tagastage peale igat toimingut konto jääk.
# Funtsiooni parameetrid:
    # algne_saldo: Algse saldo väärtus.
    # toiming: String, mis tähistab tehtavat toimingut ('deposiit' või 'valjavote').
    # summa: Summa, mida soovitakse lisada või eemaldada.
# Näide: Alustades algse saldoga 100, deposiidi toiminguga 50, peaks funktsioon konto_haldur tagastama uue saldo 150. Väljavõtte toiminguga 20 uus saldo oleks siis 130.
# Kirjutage selge dokumentatsioon, mis kirjeldab, kuidas algset saldot seada, kuidas toiminguid teostada ja millist tüüpi väärtusi tagastatakse.

pangakonto=15

def konto_haldur(saldo,toiming,summa):
    """
    Eriti oluline dokumentatsioon, et kõik aru saaks
    """
    global pangakonto
    if toiming=="deposiit":
        summa=summa+saldo 
        pangakonto=summa
    else:
        summa=summa-saldo
        pangakonto=summa
    return summa

print(konto_haldur(20,"deposiit",pangakonto))
print(konto_haldur(40,"deposiit",pangakonto))
print(konto_haldur(50,"valjavote",pangakonto))


# Loo lambda funktsioon nimega, mis arvutab vajaliku kütuse koguse teatud vahemaa läbimiseks, kasutades sõiduki kütusekulu normi (liitrit 100 km kohta).
# Funktsioon võtab kaks argumenti: kütusekulu norm (kytusekulu) ja läbitava vahemaa (vahemaa).
# Tagastab kütuse koguse liitrites, arvutatuna valemiga (kytusekulu / 100) * vahemaa.
# Näiteks, kui sõiduki kütusekulu norm on 5 liitrit 100 kilomeetri kohta ja soovite läbida 150 kilomeetrit, kasutage funktsiooni kytusekulu(5, 150), mis tagastab vajaliku kütusekoguse liitrites.

"""
kytuseKulu=lambda x, y: (x/100)*y
print(kytuseKulu(5,3)) #väljastab: 8
"""

# Loo funktsioon, mis võimaldab kasutajal teisendada temperatuuri Celsiusest Fahrenheitiks ja vastupidi.
# Funktsioon võtab kaks argumenti: temperatuuri väärtuse ja teisendamise suuna, kus ‘C’ tähendab Celsiusest Fahrenheitiks teisendamist ja ‘F’ vastupidi.
# Vaikimisi on teisendamise suund Celsiusest Fahrenheitiks.
# Funktsiooni peab kaasnema selge dokumentatsioon, mis kirjeldab selle ülesannet, parameetreid ja mida tagastab.
# Implementeeri loogika temperatuuri teisendamiseks kasutades vastavaid valemeid:


# def temperatuur(temp,yhik):
#     """
#     See on maailma parim manual
#     Parameetrid: kui ei tea, siis ei tea
#     Näide: uuri ise
#     """
#     if yhik=="c":
#         v=temp*5/9+32
#     else:
#         v=(temp-32)*5/9
#     return round(v,2)

# print(temperatuur(3,"c"))
# print(temperatuur(3,"f"))
# print(temperatuur.__doc__)
