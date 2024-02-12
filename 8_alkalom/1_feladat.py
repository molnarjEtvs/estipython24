import os
os.system("cls")

ft = input("Add meg hány Ft-ot szeretnél átváltani: ")
ft = int(ft)
euro = input("Add meg az euro árfolyamát: ")
euro = int(euro)

FtEuroban = ft//euro
print(f"A {ft} Ft összeg Euróban: {FtEuroban} €")
if FtEuroban<100:
    kezelesiKoltseg = 3
    FtEuroban -= kezelesiKoltseg
else:
    kezelesiKoltseg = 0
print(f"A kezelési költség: {kezelesiKoltseg} €")
print(f"Átváltott összeg {FtEuroban} €")

