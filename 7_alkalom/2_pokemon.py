import os
os.system("cls")

def pokemonRogzites():
    pokemonok = []
    while True:
        pokemon = input("Add meg a pokemon nevét: ")
        if pokemon == "":
            break
        pokemonok.append(pokemon)
    return pokemonok

def kiErtekeles(nevek):
    db = len(nevek)
    b = []
    c = []
    mm = []
    for egy in nevek:
        if egy.startswith("b") == True:
            b.append(egy)
        elif egy.startswith("c") == True:
            c.append(egy)
        else:
            mm.append(egy)
    
    separator = ","
    bBetusek = separator.join(b)
    cBetusek = separator.join(c)
    mmBetusek = separator.join(mm)

    print(f"Rögzített adatok száma: {db} db")
    print(f"B betűsek: {bBetusek}")
    print(f"C betűsek: {cBetusek}")
    print(f"Mindne más: {mmBetusek}")


m = pokemonRogzites()
kiErtekeles(m)