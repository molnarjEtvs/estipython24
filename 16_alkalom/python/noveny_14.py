def novenyRogzites():
    novenyek = []
    while True:
        noveny = input("Add meg a növény nevét: ")
        if not noveny: #if noveny == "":
            break
        noveny = noveny.lower()
        novenyek.append(noveny)
    return novenyek

def novenyElemzes(plants):
    db = len(plants)
    print(f"{db} növény lett rögzítve")
    adb = 0
    for noveny in plants:
        if noveny.endswith("a") == True:
            adb+=1
    print(f"a-betűre végződik: {adb} db")
    szeparator = ">>>"
    szoveg = szeparator.join(plants)
    print(f"Növények: {szoveg}")

g = novenyRogzites()
novenyElemzes(g)