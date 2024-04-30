import random
class Macska:
    def __init__(self, nev, kor, fajta):
        self.nev = nev
        self.kor = kor
        self.fajta = fajta
        self.ehseg = 50
        self.mozgasigeny = 0

    def etetes(self, mennyiseg):
        self.ehseg -= mennyiseg
        if self.ehseg < 0:
            self.ehseg = 0

    def jatszas(self, ido):
        self.mozgasigeny -= ido
        if self.kor < 1:
            self.ehseg += ido * 2
        else:
            self.ehseg += ido

    def alvas(self, ido):
        self.mozgasigeny += ido
        if ido >= 8:
            self.ehseg += 5
        else:
            self.ehseg += 2

    def setallapot(self):
        if self.ehseg < 20:
            self.allapot = "éhes"
        elif self.ehseg>=20 and self.ehseg < 60:
            self.allapot ="éhesen járkál"
        else:
            self.allapot = "jól lakott"

macskak = []
o = open("macskak.txt","r",encoding="utf-8")
for sor in o:
    sor = sor.strip()
    adatok = sor.split(",")
    macska1 = Macska(adatok[0],int(adatok[1]),adatok[2])
    macska1.jatszas(random.randint(5,10))
    macska1.etetes(random.randint(1,5))
    macska1.alvas(random.randint(5,10))
    macska1.setallapot()
    macskak.append(macska1)
    del macska1
o.close()

i = open("keszmacskak.txt","w",encoding="utf-8")
for macska in macskak:
    i.write(f"Név: {macska.nev}\n")
    i.write(f"Kor: {macska.kor} éves\n")
    i.write(f"Fajta: {macska.fajta}\n")
    i.write(f"Mozgasigény/Éhségállapot: {macska.mozgasigeny}/{macska.ehseg}\n")
    i.write(f"Pillanatnyi állapot: {macska.allapot}\n")
    i.write(f">"*30+"\n")
i.close()