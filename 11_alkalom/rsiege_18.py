import random
class Jatekos:
    def __init__(self,nev,rang,szint,hatekonysag):
        self.nev = nev
        self.rang = rang
        self.szint = szint
        self.hatekonysag = hatekonysag

    def teljesitmenyGeneralas(self):
        self.teljesitmenyek = []
        for _ in range(5):
            vszam = random.uniform(1.1,5.0)
            vszam = round(vszam,1)
            self.teljesitmenyek.append(vszam)

    def hatekonysagNoveles(self):
        self.hatekonysag += sum(self.teljesitmenyek)/len(self.teljesitmenyek)

    def rangFrissites(self,ujRang):
        if ujRang>self.rang:
            self.rang = ujRang
            return True
        else:
            return False        

karakterek = []
f = open("karakterek.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split(",")
    jatekos1 = Jatekos(adatok[0],int(adatok[1]),adatok[2],float(adatok[3]))
    jatekos1.teljesitmenyGeneralas()
    jatekos1.hatekonysagNoveles()
    jatekos1.rangFrissites(random.randint(20,50))
    karakterek.append(jatekos1)
    del jatekos1
f.close()

w = open("eredmenyek.txt","w",encoding="utf-8")
for egyKarakter in karakterek:
    w.write(f"Név: {egyKarakter.nev}\n")
    w.write(f"Rang: {egyKarakter.rang}\n")
    w.write(f"Szint: {egyKarakter.szint}\n")
    w.write(f"Név: {egyKarakter.hatekonysag}%\n")
    if sum(egyKarakter.teljesitmenyek)>10:
        w.write("KIVÁLÓ\n")
    w.write("#############################\n")
w.close()