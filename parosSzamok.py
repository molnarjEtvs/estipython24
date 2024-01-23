import os
os.system("cls")

def parosSzamok(szamok):
    parosak = []
    for egy in szamok:
        if egy%2==0:
            parosak.append(egy)

    return parosak

sz = [1,2,3,4,5,6,7,8,9,10]
p = parosSzamok(sz)
print(p)