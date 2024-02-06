import os
os.system("cls")

szelesseg = input("Add meg a szoba szélességét: ")
szelesseg = int(szelesseg)

hosszusag = input("Add meg a szoba hosszúságát: ")
hosszusag = int(hosszusag)

nmAr = input("Add meg a m2 árát a burkolásnak: ")
nmAr = int(nmAr)

terulet = szelesseg*hosszusag
burkolasiKoltseg = terulet*nmAr*1.1

print(f"A szoba {terulet}m2, burkolási költség: {burkolasiKoltseg} Ft")