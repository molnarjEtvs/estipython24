def vizsgalat(szoveg):
    karakterekSzama = len(szoveg)
    print(f"Karakterek száma: {karakterekSzama} db")
    if szoveg.endswith("k") == True:
        print(f"k-ra végződik")
    csere = szoveg.swapcase()
    print(f"{csere}")
    if szoveg.isalnum() == True:
        print(f"Csak betűk és számok")