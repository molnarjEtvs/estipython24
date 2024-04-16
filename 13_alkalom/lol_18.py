import random
class lolHos:
    def __init__(self,az,nev,tip,stilus):
        self.az = az
        self.nev = nev
        self.tip = tip
        self.stilus = stilus

    def setNehezsegiSzint(self,nehezsegiFok):
        if nehezsegiFok==1:
            self.nsz = "Easy"
        elif nehezsegiFok==2:
            self.nsz = "Medium"
        else:
            self.nsz = "Hard"
    
    def setKepessegek(self):
        lehet = ["átokszórás","végítélet","halál","bájolás"]
        self.kepesseg = random.choice(lehet)

hosok = []
f = open("hosok.hsk","r",encoding="utf-8")
for sor in f:
    sor = sor.strip() #1|Aatrox|Warrior|3|2|P
    adatok = sor.split("|")
    hos1 = lolHos(adatok[0],adatok[1],adatok[2],int(adatok[3]))
    hos1.setNehezsegiSzint(int(adatok[4]))
    hos1.setKepessegek()
    hosok.append(hos1)
    del hos1
f.close()

i = open("hoseim.txt","w",encoding="utf-8")
for egyHos in hosok:
    i.write(f"Azonosító: {egyHos.az}\n")
    i.write(f"Hős neve: {egyHos.nev}\n")
    i.write(f"Nehézségi szint: {egyHos.nsz}\n")
    i.write(f"Képesség: {egyHos.kepesseg}\n")
    i.write(f"###################################\n")
i.close()