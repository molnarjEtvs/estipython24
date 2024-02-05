szamok = []

f = open("szamok.sza","r",encoding="utf-8")
for x in f:
    x = x.strip()
    szam = int(x)
    szamok.append(szam)
f.close()

parosFajl = open("parosSzamok.txt","w",encoding="utf-8")
paratlanFajl = open("paratlanSzamok.txt","w",encoding="utf-8")

for egySzam in szamok:
    if egySzam%2==0:
        parosFajl.write(f"{egySzam}\n")
    else:
        paratlanFajl.write(f'{egySzam}\n')
parosFajl.close()
paratlanFajl.close()