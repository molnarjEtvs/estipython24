import os
os.system("cls")

utasLista = []
while True:
    nev = input("Add meg az utas nevét: ")
    if nev == "":
        break
    szulEv = input("Add meg a születési évet: ")
    szulEv = int(szulEv)
    km = input("Add meg a km számot: ")
    km = int(km)
    utas = {}
    utas['nev'] = nev
    utas['szulEv'] =szulEv
    utas['km'] = km
    utasLista.append(utas)

print(utasLista)