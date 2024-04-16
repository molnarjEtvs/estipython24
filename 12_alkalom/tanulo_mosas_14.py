def mosogepRogzites():
    markanevek = []
    while True:
        markaNev = input("Add meg a mosógép márkáját: ")
        if markaNev == "": #if not markaNev:
            break
        markaNev = markaNev.capitalize()
        markanevek.append(markaNev)
    return markanevek

def mosogepElemzes(mnevek):
    db = len(mnevek)
    print(f"Darabszám: {db} db")
    sDb = 0
    for egyElem in mnevek:
        if egyElem.find("s")>-1 or egyElem.find("S")>-1:
            sDb+=1
    print(f"{sDb}db s betűs van.")
    szeparator = "/"
    szoveg = szeparator.join(mnevek)
    print(f"Rögzített mosógépek: {szoveg}")

r = mosogepRogzites()
mosogepElemzes(r)