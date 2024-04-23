import os
os.system("cls")

gyumolcs = input("Milyen gyümölcsöt szeretnél venni?: ")
egyseg = input("Milyen egységben árulják?: ")
ar = input(f"Mennyibe kerül 1 {egyseg} {gyumolcs}: ")
ar = int(ar)
mennyiseg = input(f"Hány {egyseg} -t szeretnél venni?: ")
mennyiseg = float(mennyiseg)

vegosszeg = ar*mennyiseg
if mennyiseg>10:
    vegosszeg = vegosszeg*0.9
print(f"{mennyiseg} {egyseg} {gyumolcs} {round(vegosszeg)} Ft lesz")