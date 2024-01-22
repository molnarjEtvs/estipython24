import os,random
os.system("cls")

szamok = []

while len(szamok) != 5:
    vszam = random.randint(1,90)
    if vszam not in szamok:
        szamok.append(vszam)
szamok.sort()
print(szamok)