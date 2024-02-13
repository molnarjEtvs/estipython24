import os
os.system("cls")

kor = input("Add meg az életkorod: ")
kor = int(kor)
kezdo = input("Kezdő vagy-e? (i/n): ")

if kezdo == "i":
    felsoSzorzo = 0.8
else:
    felsoSzorzo = 0.7

alsoHatarertek = (220-kor)*0.65
felsoHatarertek = (220-kor)*felsoSzorzo

print(f"A kardió edzéshez a megfelelő pulzus intervallumod: {alsoHatarertek}-{felsoHatarertek}/perc")