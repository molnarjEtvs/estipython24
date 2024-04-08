def szamolas(szam):
    osszeg = 0
    for x in range(1,szam+1):
        osszeg += x
    return osszeg

e = szamolas(6)
print(f"{e}")