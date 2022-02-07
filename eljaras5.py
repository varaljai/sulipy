'''
4. Feladat
Írj egy programot, amelyben van egy 'kerulet' nevű függvény, amely az egyetlen kötelező paramétere mellett fogadhat több paramétert is! 
Az opcionális paraméterek száma alapján döntse el milyen síkidomról van szó, és számolja ki a kerületét (0 tetszőleges paraméter: négyzet, 1 tetszőleges paraméter: téglalap, 2 tetszőleges paraméter: háromszőg, 3 vagy több tetszőleges paraméter: sokszög)!

A program tartalmazzon mindegyik síkidom típusra egy-egy függvényhívást!
'''

def kerulet(a, *args):
    if len(args) == 0:
        return 4*a
    elif len(args) == 1:
        return a*2 + args[0] * 2
    else:
        return a + sum(args)

print(kerulet(8,))


    



    
    
    
    