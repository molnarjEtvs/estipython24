def torlesztoRogzites():
    torlesztesek = []
    x = 1
    while True:
        szam = input(f"Add meg a(z) {x}. törlesztő részletet: ")
        x+=1
        szam = int(szam)
        if szam == 0:
            break
        szam = szam*0.9
        torlesztesek.append(szam)
    return torlesztesek

def torlesztoStatisztikak(torlesztok):
    db = len(torlesztok)
    print(f"Befizetések száma: {db} db")
    legkissebb = min(torlesztok)
    print(f"Legkisebb törlesztő részlet: {legkissebb} Ft")
    legnagyobb = max(torlesztok)
    print(f"Legnagyobb törlesztő részlet: {legnagyobb} Ft")
    osszbefizetes = sum(torlesztok)
    print(f"Összbefizetések: {osszbefizetes} Ft")
    atlag = osszbefizetes/db
    print(f"Átlag befizetés: {atlag}")
    dbOtven = 0
    for egyBefizetes in torlesztok:
        if egyBefizetes<50000:
            dbOtven+=1
    print(f"50.000Ft alatti befizetések száma: {dbOtven} db")

tr = torlesztoRogzites()
torlesztoStatisztikak(tr)