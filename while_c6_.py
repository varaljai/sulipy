
szam = 1
while szam < 20:
    szam = szam + 1
    
    import random
    rszam = random.randint(1,12)
    oszthato3 = ( rszam % 3 == 0 )
    if oszthato3:
        print(rszam)
    
    
        
    