import random
class LicitTermek:
    def __init__(self,nev,bid,licitLepcso):
        self.bid = bid
        self.nev = nev
        self.licitLepcso = licitLepcso
        self.lictekSzama = 0
        self.ar = 0
        self.nyeresiAllapot = "NEM"
    
    def bidVasarlas(self,osszeg):
        self.bid += (osszeg/1000)*0.9
    
    def arszamolas(self):
        self.ar = self.bid*1000*1.1
    
    def licitalas(self):
        vszam = random.randint(1,1000)
        self.lictekSzama += 1
        self.bid -= self.licitLepcso
        if vszam%12==0:
            self.nyeresiAllapot = "IGEN"
            return False
        elif self.nev.find('a')>0 and self.nev.endswith("0") == True:
            self.bidVasarlas(random.randint(1,8))
            return True
        elif self.bid <= 0:
            self.bid = 0
            return False
        else:
            return True

licitTermekek = []
f = open("licitTermekek.txt","r",encoding="utf-8")
for row in f:
    row = row.strip()
    adatok = row.split(";")
    '''
    nev = adatok[0]
    bid = int(adatok[1])
    licitLepcso = int(adatok[2])
    termek1 = LicitTermek(nev,bid,licitLepcso)
    '''
    termek1 = LicitTermek(adatok[0],int(adatok[1]),int(adatok[2]))

    while True:
        valasz = termek1.licitalas()
        if valasz == False:
            break
    termek1.arszamolas()

    licitTermekek.append(termek1)
    del termek1
f.close()

i = open("eredmenyek.txt","w",encoding="utf-8")
for egyTermek in licitTermekek:
    i.write(f"Név: {egyTermek.nev}\n")
    i.write(f"Licitek száma: {egyTermek.lictekSzama}\n")
    i.write(f"Maradék Bid: {egyTermek.bid}\n")
    i.write(f"Ár: {egyTermek.ar}\n")
    i.write(f"Megnyerve: {egyTermek.nyeresiAllapot}\n")
    i.write("-----------------------------\n")
i.close()