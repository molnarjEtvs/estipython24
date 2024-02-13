import os
os.system("cls")

darabOra = input("Add meg hány órád volt: ")
darabOra = int(darabOra)
hianyzasok = input("Add meg hány hiányzásod volt: ")
hianyzasok = int(hianyzasok)

szazalek = hianyzasok/darabOra*100
print(f"Hiányzás aránya: {szazalek} %")
if szazalek>=20:
    print("Az órkat pótolnod kell Bajban vagy")
elif szazalek>=10 and szazalek<=19:
    print("Ne hiányozz többet mert pótolnod kell")
else:
    print("Minden rendben van")