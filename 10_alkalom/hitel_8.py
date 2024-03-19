import os
os.system("cls")

felvettOsszeg = input("Add meg a felvett összeget: ")
felvettOsszeg = int(felvettOsszeg)

honapokSzama = input("Add meg a hónapok számát: ")
honapokSzama = int(honapokSzama)

thm = input("Add meg a THM-et: ")
thm = float(thm)

visszafizetendo = felvettOsszeg*(thm/100+1)
haviTorleszto = round(visszafizetendo/honapokSzama)

print(f"Visszafizetendő összeg: {visszafizetendo} Ft")
print(f"Havi törlesztő részlet: {haviTorleszto} Ft")