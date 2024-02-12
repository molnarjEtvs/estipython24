import os
os.system("cls")

def tabletGyartok():
    gyartok = []
    while True:
        gyarto = input("Add meg a gyártót: ")
        if gyarto == "":
            break
        gyartok.append(gyarto.capitalize())
    return gyartok

def tabletStatisztika(gy):
    db = len(gy)
    a = []
    e = []
    no = []
    for egy in gy:
        if egy.startswith("A") == True:
            a.append(egy)
        if egy.endswith("E") == True or egy.endswith("e") == True:
            e.append(egy)
        if egy.find("no")>0:
            no.append(egy)
    adb = len(a)
    edb = len(e)
    noDb = len(no)
    print(f"Darabszám: {db} db")
    print(f"A-betűvel kezd: {adb} db")
    print(f"E-betűvel végez: {edb} db")
    print(f"no találat: {noDb} db")


tabletStatisztika(tabletGyartok())

#x = tabletGyartok()
#tabletStatisztika(x)
        
