
stopSzam = input("Add meg a stop számot: ")
stopSzam = int(stopSzam)

szamok = []
while True:
    szam = input("Add meg a számot: ")
    szam = int(szam)
    if szam == stopSzam:
        break
    if szam not in szamok:
        szamok.append(szam)

print(szamok)