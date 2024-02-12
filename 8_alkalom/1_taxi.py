import os
os.system("cls")

alapDij = 1100
kilometerDij = 440
percDij = 110

km = input("Add meg hány km-t utaztál: ")
km = float(km)
km = round(km)

percekSzam = input("Add meg hány percet utaztál: ")
percekSzam = int(percekSzam)

percAr = percekSzam*percDij
kilmeterAr = km*kilometerDij
utazasiDij = alapDij+percAr+kilmeterAr

print(f"A percdíj összesen: {percekSzam} perc/{percAr} Ft")
print(f"A km díj összesen: {km} km / {kilmeterAr} Ft")
print(f"FIZETENDŐ ÖSSZEG: {utazasiDij} Ft")
