import random
class Macska:
    def __init__(self,nev,kor,faj):
        self.nev = nev
        self.kor = kor
        self.faj = faj
        self.ehseg = 50
        self.mozgasigeny = 0

    def etetes(self,mennyiseg):
        self.ehseg -= mennyiseg
        if self.ehseg <0:
            self.ehseg = 0


    def jatszas(self,ido):
        self.mozgasigeny -= ido
        if self.kor<1:
            self.ehseg += ido*2
        else:
            self.ehseg += ido

    def alvas(self,ido):
        self.mozgasigeny += ido
        if ido>=8:
            self.ehseg += 5 
        else:
            self.ehseg += 2



    def setallapot(self):
        if self.ehseg<20:
            self.allapot = "éhes"
        elif self.ehseg>=20 and self.ehseg<60:
            self.allapot = "éhesen járkál"
        else:
            self.ehseg = "jól lakott"
    

macskak = []
f = open("macskak.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    a = sor.split(",")
    cica1 = Macska(a[0],int(a[1]),a[2])
    cica1.jatszas(random.randint(5,10))
    cica1.etetes(random.randint(1,5))
    cica1.alvas(random.randint(5,10))
    cica1.setallapot()
    macskak.append(cica1)
    del cica1
f.close()

i = open("keszmacskak.txt","w",encoding="utf-8")
for egyCica in macskak:
    i.write(f"Név: {egyCica.nev}\n")
    i.write(f"Kor: {egyCica.kor} éves\n")
    i.write(f"Fajta: {egyCica.fajta}\n")
    i.write(f"Mozgásigény/Éhségállapot: {egyCica.mozgasigeny}/{egyCica.ehseg}\n")
    i.write(f"Pillanatnyi állapot: {egyCica.allapot}\n")
    i.write(">"*20+'\n')
i.close()

