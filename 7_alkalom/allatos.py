import os
os.system("cls")

def allatBekeres():
    allatok = []
    while True:
        allat = input("Add meg az állat nevét: ")
        if allat == "":
            break
        allatok.append(allat)
    return allatok

def kezdoBetuSzamolas(allatLista): 
    db = len(allatLista)
    a=[]
    b=[]
    mm = []
    for egyAllat in allatLista:
        if egyAllat.startswith("a") == True:
            a.append(egyAllat)
        elif egyAllat.startswith("b") == True:
            b.append(egyAllat)
        else:
            mm.append(egyAllat)

    aDb = len(a)
    bDb = len(b)
    mmDb = len(mm)

    print(f"Összesen: {db} db")
    print(f"a betűvel: {aDb} db")
    print(f"b betűvel: {bDb} db")
    print(f"minden más: {mmDb} db")

#másik megoldás:
def kezdoBetuSzamolas2(allatLista): 
    db = len(allatLista)
    a=0
    b=0
    mm = 0
    for egyAllat in allatLista:
        if egyAllat.startswith("a") == True:
            a+=1
        elif egyAllat.startswith("b") == True:
            b+=1
        else:
            mm+=1

    print(f"Összesen: {db} db")
    print(f"a betűvel: {a} db")
    print(f"b betűvel: {b} db")
    print(f"minden más: {mm} db")   

l = allatBekeres()
kezdoBetuSzamolas(l)