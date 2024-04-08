def rCharRecords():
    karakterek = []
    while True:
        karakter = input("Add meg a karakter nevét: ")
        if karakter == "": #if not karakter:
            break
        karakter = karakter.upper()
        if karakter not in karakterek:
            karakterek.append(karakter)
    return karakterek

def rCharStatistic(karakterek):
    db = len(karakterek)
    print(f"Rögzített karakterek száma: {db} db")
    utolso = max(karakterek)
    print(f"Legutolsó az ABC-ben: {utolso}")
    dbME = 0
    for egyKarakter in karakterek:
        if egyKarakter.startswith("M") == True and egyKarakter.endswith("E") == True:
            dbME += 1
    print(f"M-el kezdődik és E-re végződik: {dbME} db")
    szeparator = "|"
    osszefuzve = szeparator.join(karakterek)
    print(f"{osszefuzve}")

s = rCharRecords()
rCharStatistic(s)