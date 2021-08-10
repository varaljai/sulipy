a = int(input('Kérlek adj meg egy számot, és én megmondom hogy páros vagy páratlan.'))
paros = ( a % 2 == 0)
paratlan = ( a % 2 == 1)
if paros:
    print('Páros!')
elif paratlan:
    print('Páratlan!')