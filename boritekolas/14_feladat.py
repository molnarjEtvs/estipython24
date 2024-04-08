class Auto:
    def __init__(self,marka,modell,evjarat):
        self.marka = marka
        self.modell = modell
        self.evjarat = evjarat
    
    def kilometerOraAllitas(self,ujErtek):
        self.ujErtek = ujErtek

auto1 = Auto("Suzuki","Ignis",2005)
auto1.kilometerOraAllitas(120000)