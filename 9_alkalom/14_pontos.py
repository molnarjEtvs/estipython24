def termekBekeres():
    arak = []
    while True:
        ar = input("Add meg a termék árát: ")
        ar = int(ar)
        if ar == 0:
            break
        if ar<0:
            ar *= -1
            #ar = ar*-1
        arak.append(ar)
    return arak

def kiszamolas(arak):
    osszertek = sum(arak)
    atlag = osszertek/len(arak)
    parosOsszeg = 0
    for egyAr in arak:
        if egyAr%2==0:
            parosOsszeg += egyAr
            #parosOsszeg = parosOsszeg+egyAr
    print(f"Termékek összértéke: {osszertek} Ft")
    print(f"Átlag érték: {atlag} Ft")
    print(f"Párosak összege: {parosOsszeg} Ft")


termekArak = termekBekeres()
kiszamolas(termekArak)
#kiszamolas(termekBekeres())

