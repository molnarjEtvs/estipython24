import os
os.system("cls")

vizigeny = input("Add meg a növény napi vízigényét: ")
vizigeny = float(vizigeny)

db = input("Add meg a növények számát: ")
db = int(db)

m3Dij = 218.95

vizfogyasztas = (vizigeny*db)/1000
vizkoltseg = m3Dij*vizfogyasztas

if db<1000:
    vizkoltseg *= 2
elif db>=1000 and db<2000:
    vizkoltseg *= 1.8
else:
    vizkoltseg *= 1.5

print(f"{vizfogyasztas} m3 a vízfogyasztás, ami {round(vizkoltseg,2)} Ft-ba kerül.")
