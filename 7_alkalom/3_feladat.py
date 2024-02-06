import os, random
os.system("cls")

class Pokemon:
    def __init__(self,dexSzam,nev,ero):
        self.dexSzam = dexSzam
        self.nev = nev
        self.ero = ero

    def beallitas(self):
        self.ugrasiMagassag = self.ero*3*0.885
    
    def kepessegValasztas(self):
        kepessegek = ["párolgás","tűzhányás","lövés","gurulás"]
        self.kepesseg = random.choice(kepessegek)


pokemonok = []
f = open("pokemonLista.txt","r",encoding="utf-8")
for sor in f:
    adatok = sor.strip().split(",")
    pokemon1 = Pokemon(int(adatok[0]),adatok[1],int(adatok[2]))
    pokemon1.beallitas()
    pokemon1.kepessegValasztas()
    pokemonok.append(pokemon1)
    del pokemon1
f.close()

i=open("pokemonjaim.txt","w",encoding="utf-8")
for egyPokemon in pokemonok:
    i.write(f"Dex szám #: {egyPokemon.dexSzam}\n")
    i.write(f"Név: {egyPokemon.nev}\n")
    i.write(f"Erő: {egyPokemon.ero} pont\n")
    i.write(f"Képesség: {egyPokemon.kepesseg}\n")
    i.write(f"Ugrási magasság: {egyPokemon.ugrasiMagassag} m\n")
    i.write("-------------------------\n")
i.close()

