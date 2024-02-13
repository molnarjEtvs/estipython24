def telefonHivasRogzites():
    hivasok = []
    while True:
        kezdoPerc = input("Add meg a kezdő értéket: ")
        kezdoPerc = int(kezdoPerc)
        if kezdoPerc == 0:
            break
        vegPerc = input("Add meg a végpercet: ")
        vegPerc = int(vegPerc)
        if vegPerc>kezdoPerc:
            egyHivas = {}
            egyHivas['start'] = kezdoPerc
            egyHivas['stop'] = vegPerc
            hivasok.append(egyHivas)
            print("A hívás rögzitésre került")
        else:
            print("A hívás NEM került rögzítésre")

    return hivasok

def telefonHivasokKiertekeles(hivasok):
    osszesen = 0
    hivasokIdotartalma = []
    for egyHivas in hivasok:
        hivasIdo = egyHivas['stop']-egyHivas['start']
        osszesen += hivasIdo
        hivasokIdotartalma.append(hivasIdo)
    atalag = osszesen/len(hivasok)
    leghosszabHivas = max(hivasokIdotartalma)

    print(f"Összes hívás összesen: {osszesen} perc")
    print(f"Átlag hívás: {atalag} perc")
    print(f"Leghosszabb hívás: {leghosszabHivas} perc")

telefonHivasokKiertekeles(telefonHivasRogzites())
