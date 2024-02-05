import os
os.system("cls")

def zsebpenzBekeres():
    penzek = []
    while True:
        penz = input("Mennyi zsebpénzt kaptál? ")
        if penz == "":
            break
        penz = int(penz)
        penzek.append(penz)
    return penzek

def kimutatas(penzek):
    db = len(penzek)
    osszeg = sum(penzek)
    atlag = osszeg/db
    print(f"Ennyi zsebpénzed van: {osszeg} Ft")
    print(f"{db}db befizetésed volt")
    print(f"Átlagosan: {atlag} Ft-ot fizettél be")

penzek = zsebpenzBekeres()
kimutatas(penzek)