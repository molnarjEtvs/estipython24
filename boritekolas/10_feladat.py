import random
szamokx = []
for _ in range(30):
    szam = random.randint(10,999)
    szamokx.append(szam)

legkissebb = min(szamokx)
legnagyobb = max(szamokx)
osszeg = sum(szamokx)
atlag = osszeg/len(szamokx)

print(f"{legkissebb}, {legnagyobb}, {osszeg}, {atlag}")