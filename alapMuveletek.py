import os
os.system("cls")

def muvelet(jel,szam1,szam2):
    if jel == "+":
        return szam1+szam2
    elif jel == "-":
        return szam1-szam2
    elif jel == "*":
        return szam1*szam2
    elif jel == "/":
        if szam2 == 0:
            return "Nullával nem osztunk"
        else:
            return szam1/szam2
    else:
        return "Nem tudom értelmezni a műveletet"
    
eredmeny = muvelet("*",10,2)
print(eredmeny)