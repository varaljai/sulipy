l = []
szam = 0
while True:
    szo = input("Adj meg egy szót")
    szam = szam + 1
    l.append(szo)
    if szam == 3:
        break
    else:
        break

def vizsgalo(l):
    print(min((word for word in l if word), key=len))
    
vizsgalo(l)

    
    
    
    