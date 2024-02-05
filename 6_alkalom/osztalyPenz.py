import random
class Befizetes:
    def __init__(self,nev,osszeg,darabaszam):
        self.nev = nev
        self.osszeg = osszeg
        self.darabaszam = darabaszam
    
    def atlagBefizetes(self):
        self.atlag = self.osszeg/self.darabaszam
    
    def kedvezmenyVeletlen(self):
        kedvezmenyek = [10,20,30,40]
        veletlen = random.choice(kedvezmenyek)
        self.kedvezmeny = veletlen
        self.kedvezmenyOsszeg = self.osszeg*(self.kedvezmeny/100)

befizetesek = []
f = open("befizetesek.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split(",")
    bef = Befizetes(adatok[0],int(adatok[1]),int(adatok[2]))
    bef.atlagBefizetes()
    bef.kedvezmenyVeletlen()
    befizetesek.append(bef)
    del bef
f.close()

i = open("kimutatas.txt","w",encoding="utf-8")
for egyBefizetes in befizetesek:
    i.write(f"Név: {egyBefizetes.nev}\n")
    i.write(f"Befizetett összeg: {egyBefizetes.osszeg} Ft\n")
    i.write(f"Átlag befizetés: {egyBefizetes.atlag} Ft\n")
    i.write(f"Kedvezmény: {egyBefizetes.kedvezmeny} Ft\n")
    i.write(f"Kedvezmény összege: {egyBefizetes.kedvezmenyOsszeg} Ft\n")
    i.write("-----------------------------\n")
i.close()