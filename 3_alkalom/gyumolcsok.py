import os
os.system("cls")

gyumolcsok = []

while True:
    gyumolcs = input("Add meg  a gyümölcs nevet: ")
    if gyumolcs == "":
        break
    gyumolcs = gyumolcs.capitalize()
    gyumolcsok.append(gyumolcs)

print(gyumolcsok)