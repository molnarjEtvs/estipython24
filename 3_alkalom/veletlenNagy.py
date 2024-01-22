import os,random
os.system("cls")

szam = input("Adj meg egy számot: ")
szam = int(szam)

vszam = random.random(1,100)

if szam>vszam:
    print("A felhasználó szám a nagyobb!")
elif szam<vszam:
    print("A random szám nagyobb!")
else:
    print("A két szám egyenlő")

print(f"Felhasználó száma: {szam}, Véletlen szám: {vszam}")