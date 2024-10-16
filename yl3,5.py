#16.10.24 Steven Pikajago
#ülesanne 03.5

"""
Ülesanne 3.5: Unistuste auto
Loo muutuja auto_mark, mis sisaldab auto marki (string)
Loo muutuja auto_mudel, mis sisaldab mudelit (sting)
Loo muutuja auto, kus ühendad kokku kaks eelmist muutujat auto_mark ja auto_mudel ning nende vahel on tühik
Loo muutuja tootmisaasta, mis näitab auto tootmisaastat (integer)
Loo muutuja hind, mis näitab auto hinda (float)
"""
mark, mudel = "Audi", "A4"
auto = mark+" "+mudel
aasta = 2022
hind = 40000    

print("Minu unistuste auto on "+auto+", tootmisaastaga "+str(aasta)+" ja hind on "+str(hind)+" eurot.")