import random
class OkosCserep:
    def __init__(self,nev,fenyigeny,vizigeny,ultetesHonapja):
        self.nev = nev
        self.fenyigeny = fenyigeny
        self.vizigeny = vizigeny
        self.ultetesHonapja = ultetesHonapja
        self.talajnedvesseg = 0
        self.tartalyszint = 100

    def napfenySzimulacio(self,ido):
        self.talajnedvesseg -= ido/2
        if self.talajnedvesseg<0:
            self.talajnedvesseg = 0
    
    def locsolas(self,mennyiseg):
        self.talajnedvesseg += mennyiseg
        self.tartalyszint -= mennyiseg

    def tartalyToltes(self,mennyiseg):
        if self.tartalyszint+mennyiseg>500:
            self.tartalyszint = 500
            return True
        else:
            self.tartalyszint += mennyiseg
            return False
    
cserepek = []

o = open("novenyek.txt","r",encoding="utf-8")
for sor in o:
    sor = sor.strip()
    adatok = sor.split("|")
    cserep1 = OkosCserep(adatok[0],adatok[1],adatok[2],int(adatok[3]))
    cserep1.napfenySzimulacio(random.randint(10,60))
    cserep1.locsolas(random.randint(0,50))
    cserep1.tartalyToltes(50)
    cserepek.append(cserep1)
    del cserep1
o.close()

i = open("cserepek.txt","w",encoding="utf-8")
for egyCserep in cserepek:
    i.write(f"Növény: {egyCserep.nev}\n")
    i.write(f"Fényigény/Vízigény: {egyCserep.fenyigeny}/{egyCserep.vizigeny}\n")
    i.write(f"Ültetés hónapja: {egyCserep.ultetesHonapja}.hónap\n")
    i.write(f"Talajnedvesség: {egyCserep.talajnedvesseg}%\n")
    i.write(f"Tartályszint: {egyCserep.tartalyszint}ml\n")
    if egyCserep.vizigeny == "magas" and egyCserep.fenyigeny == "magas":
        i.write("KÉNYES NÖVÉNY!\n")
    i.write("*"*30+"\n")

i.close()
