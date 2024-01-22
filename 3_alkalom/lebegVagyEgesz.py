import os,random
os.system("cls")

valasz = input("Add meg mit szeretnél generálni? Egész szám(e), Lebegőpontos (l): ")
if valasz == "e":
    szam = random.randint(1,3000)
    print(szam)
elif valasz == "l":
    szam = random.uniform(1,3000)
    print(szam)
else:
    print("Nem tudom értelmezni a válaszod")
