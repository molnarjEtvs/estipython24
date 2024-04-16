import os
os.system("cls")

kw = input("Add meg az éves fogyasztást kw-ban: ")
kw = int(kw)
db = input("Add meg a mosások számát: ")
db = int(db)
aramDij = 40

if kw<=0 or db<=0:
    print("Sajnos ezekkel az adatokkal nem tudok számolni")
else:
    aramIgeny = kw/db
    aramKoltseg = aramIgeny*aramDij
    print(f"Egy mosás áramköltsége: {round(aramKoltseg,2)} Ft")

