import os,random
os.system("cls")

db = input("Add meg hány darab számot szertnél: ")
db = int(db)
mettol = input("Add meg mettől szeretnéd a számokat: ")
mettol = int(mettol)
meddig = input("Add meg meddig szeretnéd a számokat: ")
meddig = int(meddig)

for _ in range(db):
    vszam = random.randint(mettol,meddig)
    print(vszam)