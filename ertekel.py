"""minta:
I/A, B:
Étel neve: Ananászos pizza
Étel rendelőjének neve: Kiss Előd
Értékelés (1-5): 4

I/C:
Köszönjük az értékelést!
A.	Kérje be az alábbi adatokat a fenti mintának megfelelően:
étel neve, étel rendelőjének neve és értékelés!  (2p)
B.	A program az adatbekérés után írja ki, ha az értékelés nem a megfelelő határokon belül lett megadva ( [1,5], zárt intervallum értendő):
Amennyiben negatív számot adott meg:
“Az értékelés nem lehet negatív!”,
Amennyiben 5 feletti egész számot adott meg:
“5 pont feletti értékelés nem elfogadható!”
Helyes pont-adat esetén:
“Köszönjük az értékelést!”
Feltételezzük, hogy csak egész számokat adnak meg. (4p)
C.	A mintának megfelelően írassa ki az eredményt! (1p)
"""
def adatbeker():
    etel_nev=input("Étel neve: ")
    rendelo_nev=input("Étel rendelőjének neve: ")
    ertekeles=int(input("Értékelés (1-5): "))
    i=0
    while ertekeles not in range(1,5):
        if ertekeles < 0:
            ertekeles=int(input("Az értékelés nem lehet negatív!:"))
        elif ertekeles > 5:
            ertekeles=int(input("5 pont feletti értékelés nem elfogadható!"))
        elif ertekeles ==0 :
            ertekeles=int(input("Az értékelés nem lehet 0 :"))
    print("Köszönjük az értékelést!")
