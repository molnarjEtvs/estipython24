import os,random
os.system("cls")

db = input("Add meg hány darab számot szertnél: ")
db = int(db)

for _ in range(db):
    vszam = random.randint(1,10000)
    print(vszam)