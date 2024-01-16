
szam = input("Adj meg egy számot: ")
szam = int(szam)
while szam>0:
    if szam%3==0:
        print(szam)
    szam-=1 # szam=szam-1


#másik megoldás
szam = input("Adj meg egy számot: ")
szam = int(szam)
for x in range(szam2,0,-1):
    if x%3==0:
        print(x)
    