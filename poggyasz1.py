"""A csomag.txt forrásállomány, csomagok méret adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használja!
A csomag.txt állomány szerkezete:
·         a (szélesség cm): pl: 51
·         b (magasság cm): pl.: 33
·         c (mélység cm): pl.: 24
·         m (súly kg-ban megadva): pl.: 10
Az állomány első sora a mezőneveket tartalmazza kettőskereszttel elválasztva.
A megoldás mintája:
III/A, B:
            	A pogyászok száma: 101
III/C:
            	Az 51 cm-es pogyászok átlag súlyértéke: 7375 g
III/D:
            	A legmagasabb pogyász méretei: 47x46x16, súlya: 4 kg.
A.	Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a csomag.txt fájlból a játékosok adatait, és tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)
B.	Írassa ki a pogyászok számát a mintának megfelelően a konzolra! (2p)
C.	Határozza meg és írassa ki a konzolra a minta szerint, hogy mennyi az 51 cm széles pogyászok átlag súlya gramban. (1kg = 1000g) (4p)
D.	Írassa ki konzolra a mintának megfelelően a legmagasabb pogyász  méreteit és súlyát (ha több is van, akkor az első legmagasabb adatait).(4p)
"""
from Csomagclass import Csomagclass
csomagok_lista=[]
def beolvas():
    fajlom=open("csomag.txt","r",encoding="utf-8")
    fajlom.readline()
    fajltartalom=fajlom.readlines()
    #print(fajltartalom)
    i=0
    while i<len(fajltartalom):
        sor=fajltartalom[i].strip().split("#")
        #print(sor)
        csomagok_lista.append(Csomagclass(sor))
        i+=1
    print(f"A pogyászok száma: {len(csomagok_lista)}")

def atlag_51_suly():
    i=0
    db=0
    ossz51suly=0
    while i< len(csomagok_lista):
       if csomagok_lista[i].szelesseg==51:
            ossz51suly+=csomagok_lista[i].suly
            db+=1
       i+=1
    print(f"Az 51 cm-es pogyászok átlag súlyértéke: {(ossz51suly/db)*1000} g")

def legmagasabb():
    i=0
    legmagasabb=0
    while i < len(csomagok_lista):
        if csomagok_lista[legmagasabb].magassag < csomagok_lista[i].magassag:
            legmagasabb=i
        i+=1
    print(f"A legmagasabb pogyász méretei: {csomagok_lista[legmagasabb].szelesseg}x{csomagok_lista[legmagasabb].magassag}x{csomagok_lista[legmagasabb].melyseg}, súlya: {csomagok_lista[legmagasabb].suly} kg")

