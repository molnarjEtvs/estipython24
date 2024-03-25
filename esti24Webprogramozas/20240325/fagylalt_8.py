gombocAr = input("Mennyibe kerül egy gombóc fagylalt?: ")
gombocAr = int(gombocAr)

tolcserAr = input("Mennyibe kerül egy tölcsér? ")
tolcserAr = int(tolcserAr)

gombocokSzama = input("Hány gombócot szeretnél venni?: ")
gombocokSzama = int(gombocokSzama)

if gombocokSzama>3:
    tolcserAr = 0

fizetendo = (gombocokSzama*gombocAr)+tolcserAr

print(f"{gombocokSzama} gombóc fagylalt a tölcsérrel együtt {fizetendo} Ft lesz.")