import os
os.system("cls")

zeneLista = []

while True:
    eloado = input("Add meg az előadót: ")
    eloado = eloado.capitalize()
    if eloado == "":
        break
    cim = input("Add meg a címet: ").capitalize()
    mp = input("Add meg a mp-t: ").capitalize()
    mp = int(mp)
    zene = {}
    zene['eloado'] = eloado
    zene['cim'] = cim
    zene['mp'] = mp
    zeneLista.append(zene)

print(zeneLista)