import os
os.system("cls")

koleszosok = []
szabadHelyek = 10
maradt = szabadHelyek
while len(koleszosok)<szabadHelyek:
    nev = input("Add meg a nevet: ")
    km = input("Add meg a távolságot: ")
    km = int(km)
    atlag = input("Add meg az átlagot: ")
    atlag = float(atlag)
    if atlag>2.7 and km>=50:
        koleszos = {}
        koleszos['nev'] = nev
        koleszos['km'] = km 
        koleszos['atlag'] = atlag
        koleszosok.append(koleszos)
        print("A diák rögzítése megtörtént")
        maradt -= 1
        print(f"Szabad helyek száma: {maradt}")
    else:
        print("A diák nem felel meg a feltételeknek")
print("A koleszosok száma megtelt")