import random
szamok = []
for _ in range(5):
    szam = random.randint(100,200)
    szamok.append(szam)
osszeg = sum(szamok)
print(f"összeg: {osszeg}")
print(f"{szamok[2]}")