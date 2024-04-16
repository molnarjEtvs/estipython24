def hosRogzites():
    lolNevek = []
    while True:
        nev = input("Add meg a lol nevét: ")
        if nev == "": #if not nev:
            break
        lolNevek.append(nev)
    return lolNevek

def hosErtekeles(hosok):
    db = len(hosok)
    print(f"Hősök darabszáma: {db} db")
    har=[]
    ot=[]
    hat=[]
    for hos in hosok:
        if len(hos) == 3:
            har.append(hos)
        elif len(hos) == 5:
            ot.append(hos)
        elif len(hos) == 6:
            hat.append(hos)
    szep = ", "
    print(f"Három betűsek: {szep.join(har)}")
    print(f"Öt betűsek: {szep.join(ot)}")
    print(f"Hat betűsek: {szep.join(hat)}")

h = hosRogzites()
hosErtekeles(h)