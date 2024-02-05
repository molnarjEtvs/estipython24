import os
os.system("cls")

class Ajto:
    def __init__(self,szin,tipus):
        self.szin = szin
        self.tipus = tipus
        self.m2Ar = 6000
    
    def setMeretek(self,szelesseg,magassag):
        self.szelesseg = szelesseg
        self.magassag = magassag

    def arSzamolas(self):
        self.ajtoAr = (self.szelesseg/100)*(self.magassag/100)*self.m2Ar

ajtok = []
f = open("ajtok.lst","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split(";")
    ajto = Ajto(adatok[1],adatok[0])
    ajto.setMeretek(int(adatok[2]),int(adatok[3]))
    ajto.arSzamolas()
    ajtok.append(ajto)
f.close()

i = open("arajanlat.txt","w",encoding="utf-8")
for egyAjto in ajtok:
    i.write(f"Ajtó típusa: {egyAjto.tipus}\n")
    i.write(f"Ajtó ára: {egyAjto.ajtoAr} Ft\n")
    i.write(f"Méret: {egyAjto.szelesseg}x{egyAjto.magassag} cm\n")
    i.write("-----------------------\n")
i.close()