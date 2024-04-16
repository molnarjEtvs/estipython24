import os
os.system("cls")

nev = input("Add meg a lol karakter nevét: ")
alapEro = input("Add meg az alaperőt: ")
alapEro = float(alapEro)
futasiSebesseg = (alapEro*0.225)+10
magikusEro = (alapEro/2)*0.9
nagybetus = nev.upper()
print(f"A hősöd neve: {nagybetus}")
print(f"Futási sebesség: {futasiSebesseg} km/h")
print(f"Mágikus erő: {magikusEro} Mp")

