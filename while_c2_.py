paros = 0
paratlan = 0

while paros > -1 and paratlan > -1:
    bekertszam = int(input('Kérlek 0 és plusz végtelen egész szám közöt adj meg számokat és én meg mondom menyi páros és páratlan volt ha megadod a 0.'))
    
    if bekertszam % 2 == 0:
        paros +1
    elif bekertszam % 2 == 1:
        paratlan +1
    elif bekertszam == 0:
        print('paratlan:',paratlan,'páros:',paros)
        break
        