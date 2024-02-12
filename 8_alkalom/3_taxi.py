import os,random
os.system("cls")

class taxiFuvar:
    def __init__(self,azonosito,utasokSzama,kmAllas):
        self.azonosito = azonosito
        self.utasokSzama = utasokSzama
        self.kmAllas = kmAllas
        self.kmDij = 440
        self.szervizeles = "NEM"
    
    def fuvarozas(self,megtettUt):
        self.kmAllas += megtettUt
        self.utDij = megtettUt*self.kmDij

    def szamlaNyomtatas(self):
        self.szamlaSzam = random.randint(100,999)
        if self.utasokSzama>2:
            self.utDij*1.05
    
    def szervizCheck(self):
        if self.kmAllas>10000:
            self.szervizeles = "IGEN"

fuvarok = []

f = open("taxiFuvarok.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split("|")
    fuvar = taxiFuvar(adatok[0],int(adatok[1]),int(adatok[2]))
    fuvar.fuvarozas(random.randint(10,50))
    fuvar.szamlaNyomtatas()
    fuvar.szervizCheck()
    fuvarok.append(fuvar)
    del fuvar
f.close()


i = open("taxiSzamlak.txt","w",encoding="utf-8")
for egyFuvar in fuvarok:
    i.write(f"Azonosító: {egyFuvar.azonosito}\n")
    i.write(f"Utasok száma: {egyFuvar.utasokSzama} db\n")
    i.write(f"KM állás: {egyFuvar.kmAllas} km\n")
    i.write(f"Számlaszám: #{egyFuvar.szamlaSzam}#\n")
    i.write(f"Útdíj: {egyFuvar.utDij} Ft\n")
    i.write(f"Szervíz szükséglet: {egyFuvar.szervizeles}\n")
    i.write(f"------------------------------------\n")
i.close()


