import os
os.system("cls")

pontszam = input("Add meg a pontszámot: ")
pontszam = int(pontszam)

if pontszam<50:
    print("elégtelen")
elif pontszam>=50 and pontszam<60:
    print("elégséges")
elif pontszam>=60 and pontszam<70:
    print("közepes")
elif pontszam>=70 and pontszam<85:
    print("jó")
else:
    print("jeles")