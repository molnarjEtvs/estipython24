
eletkorok = []
while True:
    eletkor = input("Adj meg egy életkort: ")
    eletkor = int(eletkor)
    if eletkor == 0:
        break
    eletkorok.append(eletkor)
print(eletkorok)