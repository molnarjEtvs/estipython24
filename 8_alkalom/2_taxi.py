def taxiAzonositoRogzitese():
    azonositok = []
    while True:
        azonosito = input("Add meg a taxi azonosítóját: ")
        if azonosito == "":
            break
        azonositok.append(azonosito.upper())
    return azonositok

def taxiElemzes(tAzonsitok):
    db = len(tAzonsitok)
    szervizesek = []
    kivonasok = []
    for taxi in tAzonsitok:
        if taxi.startswith("A") == True:
            szervizesek.append(taxi)
        if taxi.endswith("X") == True and taxi.find("0")>0:
            kivonasok.append(taxi)

    print(f"Összesen: {db} db")
    print(f"Szervízek száma: {len(szervizesek)} db")
    print(f"Flottából kivonni: {len(kivonasok)} db")

taxiElemzes(taxiAzonositoRogzitese())