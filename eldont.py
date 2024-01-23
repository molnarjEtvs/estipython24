import os
os.system("cls")

def eldontes(szam):
    if szam>0:
        print("Pozitív")
    elif szam<0:
        print("Negatív")
    else:
        print("Nulla")
szam = input("Add meg a számot: ")
szam = int(szam)
eldontes(szam)
eldontes(32)
eldontes(-18)
eldontes(0)