import random
class Kolcsonzes:
    def __init__(self,nev,azonosito,ido,percdij):
        self.nev = nev
        self.azonosito = azonosito
        self.ido = ido
        self.percdij = percdij
        self.fizetendo = 0
        self.sorszam = ""

    def sorszamGeneralas(self):
        szam = random.randint(300,600)
        return str(szam)
    
    def vegosszegSzamolas(self):
        if self.azonosito == "A" or self.azonosito == "B":
            self.fizetendo = round(self.ido*self.percdij*0.9)
        else:
            self.fizetendo = self.ido*self.percdij

kolcsolnzesek = []

f = open("kolcsonzesek.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split(",")
    kolcsonzes1 = Kolcsonzes(adatok[0],adatok[1],int(adatok[2]),int(adatok[3]))
    kolcsonzes1.sorszam = kolcsonzes1.sorszamGeneralas()
    kolcsonzes1.vegosszegSzamolas()
    kolcsolnzesek.append(kolcsonzes1)
    del kolcsonzes1
f.close()

i = open("szamlak.txt","w",encoding="utf-8")
for egyKolcson in kolcsolnzesek:
    i.write(f"Név: {egyKolcson.nev}\n")
    i.write(f"Azonosító: {egyKolcson.azonosito}\n")
    i.write(f"Sorszám: #{egyKolcson.sorszam}\n")
    i.write(f"{egyKolcson.ido} perc * {egyKolcson.percdij} Ft = {egyKolcson.fizetendo} Ft\n")
    i.write("-------------------------\n")
i.close()
         