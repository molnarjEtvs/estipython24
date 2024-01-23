import os,random
os.system("cls")

def veletlenSzamok(db,a,b):
    szamok = []
    for _ in range(db):
        szam = random.randint(a,b)
        szamok.append(szam)

    return szamok


b = veletlenSzamok(5,1,10)
print(b)