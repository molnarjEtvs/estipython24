def macskaRogzites():
    macskak = []
    while True:
        macska = input("Add meg a macska nevét:")
        if not macska:
            break
        if macska not in macskak:
            macskak.append(macska.capitalize())
    return macskak
def macskaElemzes(cats):
    db = len(cats)
    print(f"{db}db macska lett rögzítve")
    ibetusek = []
    for cat in cats:
        if cat.find("i")>-1:
            ibetusek.append(cat)
    sep = ">>"
    iSzoveg = sep.join(ibetusek)
    print(f"i betűs macskak: {iSzoveg}")

m = macskaRogzites()
macskaElemzes(m)