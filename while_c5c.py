a = True
while a:
  mszam = int(input('Kérlek írj nekem egy páros számot!'))
  paros = (mszam % 2 == 0)
  paratlan= (mszam % 2 == 1)
  if mszam and paros:
    print('köszi')
    break
  elif mszam and paratlan:
    print()