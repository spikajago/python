# Steven Pikajago
# 18.12.24
# KT

# 5. Shopping List
# 	Create a program that will keep track of items for a shopping list. The program should keep asking for new items until nothing is entered (no input followed by enter/return key). The program should then display the full shopping list.

# int(input("Mida teie soovite lisada ostunimekirja: "))


# 6. Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris vÃµi paaritu
# 	kuvatakse korrektne arusaadav kÃ¼simus ja vastus - 1p
# 	eelnev kontroll, kas kasutaja ei lisanud arvu vÃµi pani nulli - 1p
# 	kood mis teavitab paaris vÃµi paaritust arvust - 1p
# 	kuvatakse programmi pealkiri - 1p
# 	kood kommenteeritud - 1p

# number=int(input("kirjutage mingi arv: "))
# if number%2==0:
#     print("paaris")
# else:
#     print("paaritu")

# 15. Temperatuurid - Programm peab tÃ¶Ã¶tlema Ã¼he aasta kÃµigi pÃ¤evade temperatuure. Kirjutada programm, mis leiab kuude kaupa, mitmendal kuupÃ¤eval oli kÃµige soojem. VÃ¤ljasta kuupÃ¤ev ja vastav temperatuur. (Kui sama temperatuuriga oli mitu pÃ¤eva, vÃ¤ljasta vÃ¤hemalt Ã¼ks)

# [[jaanuar -16 -12 -15 -20 0 -1 -20 -2 -20 -14 -18 -8 2 -1 -14 -7 -15 -17 -6 -17 -17 -7 0 3 -20 -17 -15 -8 -12 3]
# [veebruar -9 -2 -7 1 -16 -19 -19 -11 -16 -15 -9 -2 -16 -4 -20 -5 -6 -17 -5 0 -16 2 0 -20 -16 -2 -18]
# [mÃ¤rts 2 -9 -1 -3 -6 -2 1 -2 -3 -9 -1 -4 0 -6 -7 1 0 2 -5 -10 2 -7 -3 2 -10 2 -9 -8 -5 -2]
# [aprill -5 0 10 -9 0 -9 -8 6 -5 3 -1 4 9 -1 2 0 10 0 5 0 -10 0 6 3 -6 -2 -10 -8 -2]
# [mai 12 5 8 -1 -2 4 10 -1 7 15 7 3 6 4 10 9 13 6 14 10 14 2 6 12 15 2 14 11 9 1]
# [juuni 12 5 17 6 10 14 9 7 15 23 29 11 16 18 9 25 14 8 16 22 19 22 23 18 16 16 26 24 22]
# [juuli 15 8 21 28 18 13 9 9 8 6 8 12 12 29 28 20 6 9 12 8 14 18 14 13 23 6 24 24 17 20]
# [august 7 6 5 19 18 18 17 20 15 11 7 10 13 12 20 11 10 14 18 14 24 6 17 16 6 17 5 13 11]
# [september 21 19 21 9 13 18 6 6 20 7 25 13 8 9 14 16 19 10 7 25 7 17 16 15 17 18 15 9 19]
# [oktoober 2 2 1 5 -2 5 5 2 2 2 1 -2 1 -2 0 -2 5 4 0 1 -1 2 0 2 2 2 -1 1 4 -1]
# [november -6 -7 -2 -7 -2 -4 0 -7 -8 -6 0 -9 -2 -3 -2 0 -8 -2 -5 -2 -5 -8 -10 0 -2 -9 -9 -7 -1]
# [detsember -15 2 -11 -14 -15 -5 -5 -18 -18 -19 0 0 2 -7 -16 -7 -4 -1 -1 -16 -18 -10 -3 -19 -6 -16 -16 -8 -2 -18]]

kuud = [["jaan", 2, -2, 30],["veeb", -10, -20, 31]]
for i in range(len(kuud)):
    print(kuud[i][0])
    k=[]
    for j in range(1,len(kuud[i])):
        k.append(kuud[i][j])
    print(kuud[i].index(max(k)))

# 16. TÃ¤ringud
# 	Kasutaja vÃµistleb kahe tÃ¤ringuga arvuti vastu. Kasutaja teeb pakkumise ning suurima tÃ¤ringupunktisumma vÃµitja saab laual oleva raha endale juurde. MÃ¤ng kestab kuni kummalgi on raha otsas.
# 	(Vihjed: kÃ¼si kasutajalt nime, kuva pidevalt konto seisu ja tÃ¤ringuviskeid, kasutajate raha hulga mÃ¤ngu alguses mÃ¤Ã¤rad sina)


# 17. Email
# 	Kasutaja lisab emaili kujul enimi.pnimi@server.com
# 	Programm kontrollib kas email on sisestatud Ãµigesti
# 	Programm tÃ¼keldab selle ja vÃ¤ljastab lause: Tere enimi, sinu email on server serveris ja domeeniks on sul com
	

# ---------------
# sport.txt
# klass2 23.4
# klass1 15.7
# klass3 19.6
# klass3 20.6
# klass2 22.5
# klass1 23.7
# klass3 19.0
# klass2 28.5
# klass1 23.4
# klass2 15.7
# klass2 21.2
# klass3 23.8
# klass3 18.6
# klass3 21.6
# klass1 22.4
# klass2 16.7