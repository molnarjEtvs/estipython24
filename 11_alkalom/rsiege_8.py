import os
os.system("cls")

jatekos1 = input("Add meg a játékos 1 nevét: ")
jatekosRang1 = input("Add meg a játékos 1 rangját: ")
jatekosRang1 = int(jatekosRang1)

jatekos2 = input("Add meg a játékos 2 nevét: ")
jatekosRang2 = input("Add meg a játékos 2 rangját: ")
jatekosRang2 = int(jatekosRang2)

if jatekosRang1>jatekosRang2:
    gyoztes = jatekos1
    vesztes = jatekos2
elif jatekosRang1<jatekosRang2:
    gyoztes = jatekos2
    vesztes = jatekos1
else:
    gyoztes = "DÖNTETLEN"
    vesztes = "DÖNTETLEN"

print(f"A csata nyertese: {gyoztes}")
print(f"A csata vesztese: {vesztes}")