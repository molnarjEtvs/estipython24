import random
class Fa:
    def __init__(self,fajnev,kerulet,telepulesnev,feljegyzesEv):
        self.fajnev = fajnev
        self.kerulet = kerulet
        self.telepulesnev = telepulesnev
        self.feljegyzesEv = feljegyzesEv
        self.kor = 0
        self.hatralevoIdo = 0
    
    def elteltIdo(self):
        self.kor = 2024-self.feljegyzesEv
    
    def Becsles(self):
        szam = random.randint(10,100)
        return szam
    
fakListaja = []

f = open("faforr.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split("\t")
    fa1 = Fa(adatok[0],int(adatok[1]),adatok[2],int(adatok[3]))
    fa1.elteltIdo()
    fa1.hatralevoIdo = fa1.Becsles()
    fakListaja.append(fa1)
    del fa1
f.close()

w = open("kimutatas.txt","w",encoding="utf-8")
for egyFa in fakListaja:
    w.write(f"Feljegyzés éve: {egyFa.feljegyzesEv}\n")
    w.write(f"{egyFa.telepulesnev} településen található fa fajneve: {egyFa.fajnev}, melynek átmérője: {egyFa.kerulet}cm\n")
    w.write(f"A feljegyzés óta eltelt: {egyFa.kor} év\n")
    w.write(f"A fa még kb {egyFa.hatralevoIdo} év\n")
    if egyFa.kor>10:
        w.write(f"ELLENŐRIZENDŐ\n")
    else:
        w.write(f"NINCS TEENDŐ\n")
    w.write("--------------------\n")
w.close()

