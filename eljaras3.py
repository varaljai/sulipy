szam = int(input("adj meg egy számot!"))
szam1 = int(input("adj meg még egy számot!"))
def eldonto(szam,szam1):
    if szam < szam1:
        print(f"{szam1} volt a nagyobb mert a másik {szam}")
    elif szam > szam1:
        print(f"{szam} volt a nagyobb mert a másik {szam1}")
    elif szam == szam1:
        print("a két szám egyenlő!")
eldonto(szam,szam1)