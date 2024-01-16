szamok = []
for x in range(5):
    szam = input("Add meg az évszámot: ")
    szam = int(szam)
    szamok.append(szam)

kicsi = min(szamok)
nagy = max(szamok)
print(f"A legkisebb: {kicsi}")
print(f"A legnagyobb: {nagy}")

