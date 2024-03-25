def fagylaltNevek():
    fagyik = []
    while True:
        nev = input("Add meg a fagylalt nevét: ")
        if nev == "":
            break
        nev = nev.capitalize()
        fagyik.append(nev)
    return fagyik

def Statisztika(fagyikak):
    db = len(fagyikak)
    print(f"{db} féle fagylalt kapható.")
    dbVegan = 0
    for egyFagyika in fagyikak:
        if egyFagyika.find("vegán")>-1 or egyFagyika.find("Vegán")>-1:
            dbVegan+=1
    print(f"Ebből vegán ízesítésú: {dbVegan} db")

f = fagylaltNevek()
Statisztika(f)