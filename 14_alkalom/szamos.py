'''
Olvassuk be az alábbi fájl tartalmmát egy listába,
majd a következő feladatokat oldjuk meg.
Minden feladat előtt a program írja ki a feladat sorszámát!
1. Hány eleme van a sorozatnak? 
2. Van-e a sorozatban negatív szám? "IGEN/NINCS negatív szám"
3. Hány páros szám található a sorozatban?
4. Mennyi a sorozatban található legnagyobb szám?
5. Írjuk ki a sorozatban található 10-zel osztható számokat!
6. Írjuk ki az első 29-cel osztható szám indexét!
7. Igaz-e, hogy minden szám páros? "IGEN/NEM mindegyik szám páros"
8. Mennyi a sorozatban található számok átlaga?
9. Van-e a sorozatban olyan negatív szám, amelyet nulla követ? 
"IGEN/NINCS olyan szám amit 0 követ"
10. Írjuk ki az utolsó 17-tel osztható szám indexét!
'''
import os
os.system("cls")

szamok = []
f = open("szamok.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    szamok.append(int(sor))
f.close()

db = len(szamok)
print("1.feladat: ")
print(f"{db} db szám van\n\n")

print("\n\n2.feladat: ")
vanNegativ = False
for szam in szamok:
    if szam<0:
        vanNegativ = True
if vanNegativ == True:
    print("VAN negatív szám benne")
else:
    print("NINCS benne negatív szám")

print("\n\n3.feladat: ")
parosDb = 0
for szam in szamok:
    if szam%2==0:
        parosDb+=1
print(f"{parosDb} db páros szám van.")

print("\n\n4.feladat: ")
legnagyobb = max(szamok)
print(f"A legnagyobb szám: {legnagyobb}")


print("\n\n5.feladat: ")
tizesSzamok = []
for szam in szamok:
    if szam%10==0:
        tizesSzamok.append(str(szam))
kiiras = ", ".join(tizesSzamok)
print(f"10-el osztható számok: {kiiras}")


print("\n\n6.feladat: ")
for index in range(0,len(szamok)):
    if szamok[index]%29==0:
        print(f"Az első 29-cel osztható szám indexe: {index}")
        break


print("\n\n7.feladat: ")
mindParos = True
for szam in szamok:
    if szam%2!=0:
        mindParos = False
if mindParos == True:
    print("MIND PÁROS")
else:
    print("NEM MIND PÁROS")



print("\n\n8.feladat: ")
atlag = sum(szamok)/len(szamok)
print(f"Az átlag: {atlag}")

print("\n\n9.feladat: ")
vanNullaKovet = False
for index in range(0,len(szamok)-1):
    if szamok[index]<0 and szamok[index+1] == 0:
        vanNullaKovet = True
if vanNullaKovet == True:
    print("Van olyan negatív szám amit 0 követ")
else:
    print("Nincs olyan szám amit 0 követ")

print("\n\n10.feladat: ")
for index in range(len(szamok)-1,0,-1):
    if szamok[index]!=0 and szamok[index]%17==0:
        print(f"Az utolsó 17-el osztható szám INDEXE: {index}")
        break

