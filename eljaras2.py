szam = int(input("adj meg egy számot!"))
def eldonto(szam):
    if szam < 0:
        print("negatív")
    elif szam > 0:
        print("pozitiv")
    elif szam == 0:
        print("a szám nulla")
eldonto(szam)
    