"""minta:
II/A, B, C:
           	20$28$124$166$15$188$174$243$221$22$945$841
II/D, E:
           	A páratlanok száma: 5.
kimutatas.txt tartalma:
II/F:
A páratlanok száma: 5.

A.	Írasson ki a konzolra dollár jelel ($) elválasztva 12 számból álló véletlen számsorozatot [-10,1000] zárt intervallumon a mintának megfelelően! (4p)
B.	A generált értékeket tárolja lista adatszerkezetben! (1p)
C.	A $ jel csak az értékek között szerepeljen (a végén, elején ne)! (2p)
D.	Írjon függvényt paratlanok_szama néven, amiben számolja meg, hogy hány olyan elem van, ami páratlanok. A visszatérési érték legyen egy egész szám! (3p)
E.	A paratlanok_szama függvény eredményét írassa ki a mintának megfelelően a konzolra, amit konzol_kiir nevű metódusban fogalmazzon meg! (2p)
F.	A paratlanok_szama függvény eredményét írassa ki a mintának megfelelően a eredmeny.txt nevű fájlba, amit fajlba_kiir nevű metódusban fogalmazzon meg! (2p)
"""
import random

nyolcas_lista=[]
def listmaker():
    i=0
    while i<12:
        nyolcas_lista.append(random.randint(-10,1000))
        i+=1
    print("@".join(str(szamok) for szamok in nyolcas_lista))

def paratlanok_szama():
    i=0
    paratlan_db=0
    while i < len(nyolcas_lista):
        if nyolcas_lista[i]%2!=0:
            paratlan_db +=1
        i+=1
    return paratlan_db
    konzol_kiir(paratlan_db)
    fajlba_kiir(paratlan_db)

def konzol_kiir(paratlan_db):
    print(f"A páratlanok száma:{paratlan_db}")

def fajlba_kiir(paratlan_db):
   fajlom= open("eredmeny.txt","w",encoding="utf-8")
   fajlom.write(f"kimutatas.txt tartalma: {paratlan_db}")




