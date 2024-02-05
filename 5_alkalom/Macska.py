class Macska:
    def __init__(self,nev,suly,ehesE):
        self.nev = nev
        self.suly =suly
        self.ehesE = ehesE

    def eszik(self,etelMennyiseg):
        if self.ehesE == True:
            self.suly += etelMennyiseg
            return True
        else:
            return False
        
    def futkos(self):
        self.suly -= 0.1
        if self.ehesE == False:
            self.ehesE = True

    
    def jelenlegiErtekek(self):
        print(f"Név: {self.nev}")
        print(f"Súly: {self.suly} kg")
        if self.ehesE == True:
            print(f"Éhes-e: Igen")
        else:
            print(f"Éhes-e: NEM")

macska1 = Macska("Garfield",4.9,True)
macska2 = Macska("Cirmi",2.1,False)
macska1.jelenlegiErtekek()
macska2.jelenlegiErtekek()
macska1.eszik(0.8)
macska2.eszik(0.2)
for _ in range(10):
    macska1.futkos()

macska1.jelenlegiErtekek()
macska2.jelenlegiErtekek()


