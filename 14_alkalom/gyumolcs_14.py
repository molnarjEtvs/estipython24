def gyumolcsGeneralas():
    gyumolcsNevek = []
    while True:
        nev = input("Add meg a gyümölcs nevét: ")
        if not nev: #if nev == "":
            break
        gyumolcsNevek.append(nev)
    return gyumolcsNevek

def kimutatas(fruits):
    db = len(fruits)
    print(f"Gyümölcsök száma a listában: {db} db")
    dbm = 0
    for egyGyumolcs in fruits:
        if egyGyumolcs.find("m")>-1:
            dbm += 1
    print(f"Az m karaktert tartalmazó gyümölcsnevek száma: {dbm} db")


m = gyumolcsGeneralas()
kimutatas(m)