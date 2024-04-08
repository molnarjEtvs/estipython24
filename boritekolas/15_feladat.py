class Szemely:
    def __init__(self,nev,kor,nem):
        self.nev = nev
        self.kor = kor
        self.nem = nem
    
    def koszones(self):
        print(f"Üdvözöllek kedves {self.nev}!")
    
szemely1 = Szemely("Gerzsonka",35,"Férfi")
szemely1.koszones()