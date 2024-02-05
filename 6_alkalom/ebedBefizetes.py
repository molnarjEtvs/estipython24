import os
os.system("cls")

napokSzama = input("Add meg a napok számát: ")
napokSzama = int(napokSzama)

napiDij = input("Add meg a napi díjat: ")
napiDij = int(napiDij)

nettoDij = napokSzama*napiDij
bruttoDij = nettoDij*1.27

print(f"Napok száma: {napokSzama}")
print(f"Nettó összeg: {nettoDij} Ft")
print(f"Bruttó összeg: {bruttoDij} Ft")
