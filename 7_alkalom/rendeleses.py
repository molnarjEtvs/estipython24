import random
class Rendeles:
    def __init__(self,datum,osszeg,tetelszam):
        self.datum = datum
        self.osszeg = osszeg
        self.tetelszam = tetelszam
    
    def kedvezmenyGeneralas(self):
        kedvezmenyek = [5,10,12,15]
        self.kedvezmeny = random.choice(kedvezmenyek)

    def kedvezmenySzamolas(self):
        self.kedvezmenyForintban = (self.kedvezmeny/100)*self.osszeg
        self.kedvezmenyesAr = self.osszeg-self.kedvezmenyForintban
    
rendelesek = []
f = open("rendelesek.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split(";")
    rendeles1 = Rendeles(adatok[0],int(adatok[1]),int(adatok[2]))
    rendeles1.kedvezmenyGeneralas()
    rendeles1.kedvezmenySzamolas()
    rendelesek.append(rendeles1)
    del rendeles1
f.close()


i = open("rendelesKedvezmenyek.txt","w",encoding="utf-8")
for egyRendeles in rendelesek:
    i.write(f"Rendelés dátuma: {egyRendeles.datum}\n")
    i.write(f"Összeg: {egyRendeles.osszeg} Ft\n")
    i.write(f"Kedvezmény: {egyRendeles.kedvezmeny}% -> {egyRendeles.kedvezmenyForintban} Ft \n")
    i.write(f"Végösszeg: {egyRendeles.kedvezmenyesAr} Ft\n")
    i.write("---------------------------------\n")
i.close()