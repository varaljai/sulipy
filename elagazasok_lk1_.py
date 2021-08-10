a = int(input('Kérlek adj meg egy számot teljesen midegy hogy pozitív vagy nem,és én megmondom hogy páros vagy páratlan.'))
paros = ( a % 2 == 0)
paratlan = ( a % 2 == 1)
pozitiv = ( a > 0)
negativ = ( a < 0)
if paros and pozitiv:
    print('Ez pozitiv is meg páros is!')
elif paratlan and negativ:
    print('Ez negatív is meg páratlan is!')
elif paros and negativ:
    print('Ez páros is meg negatív is!')
elif paratlan and pozitiv:
    print('Ez páratlan is meg pozitív is!')