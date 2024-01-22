import os
os.system("cls")

mondat = input("Add meg a mondatot: ")
szo = input("Add meg a szót: ")
if mondat.startswith(szo) == True:
    print("A szó a mondattal kezdődik")
elif mondat.endswith(szo) == True:
    print("A szó a mondatra végződik")
else:
    print("Sem nem kezd se nem végződik")