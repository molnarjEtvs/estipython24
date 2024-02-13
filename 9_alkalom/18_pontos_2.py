import random
class fociCsapat:
    def __init__(self,nev,bajnokiHelyezes,edzettsegiSzint,energiaSzint):
        self.nev = nev
        self.bajnokiHelyezes = bajnokiHelyezes
        self.edzettsegiSzint = edzettsegiSzint
        self.energiaSzint = energiaSzint
        self.edzesekSzama = 0
        self.pihenesekSzama = 0
        self.eredmeny = ""
    
    def pihen(self):
        self.pihen+=1
        vszam = random.randint(0,3)
        self.energiaSzint += vszam*0.5
    
    def edz(self):
        vszam = random.randint(1,3)
        self.energiaSzint += vszam*1.5
        self.edzettsegiSzint -= vszam*0.7
        self.edzesekSzama += 1
        if self.energiaSzint<3:
            self.pihen()
        if self.edzettsegiSzint>=9:
            return True
        else:
            return False
        
    def jatszik(self):
        dontoPont = random.randint(1000,10000)
        if self.nev.startswith("M") == True or dontoPont%13==0:
            self.bajnokiHelyezes -= 2
            self.eredmeny = "NYERT"
        elif self.nev.find("a")>0 and dontoPont%2==0:
            self.bajnokiHelyezes -= 1
            self.eredmeny = "DÖNTETLEN"
        else:
            self.bajnokiHelyezes += 3
            self.eredmeny = "VESZTETT"

csapatok = []
f = open("fociCsapatok.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split("|")
    csapat = fociCsapat(adatok[0],int(adatok[1]),int(adatok[2]),float(adatok[3]))
    print("fájl kész1")
    while True:
        valasz = csapat.edz()
        if valasz == False:
            break
    csapat.jatszik()
    csapatok.append(csapat)
    del csapat
f.close()

i = open("erdmenyekFoci.txt","w",encoding="utf-8")
print("fájl kész")
for egyCsapat in csapatok:
    i.write(f"Csapat neve: {egyCsapat.nev}\n")
    i.write(f"Bajnoki helyezés: {egyCsapat.bajnokiHelyezes}\n")
    i.write(f"Játék eredménye: {egyCsapat.eredmeny}\n")
    i.write(f"Új edzettségi szint: {egyCsapat.edzettsegiSzint}\n")
    i.write(f"Új energia szint {egyCsapat.energiaSzint}\n")
    i.write("**********************************\n")
i.close()

