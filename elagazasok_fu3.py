a = int(input('A gép gondolt egy számra 1 és 10 között, probáld meg ki találni.'))
gondolt_szam = int(3)

if gondolt_szam < a :
    print('sajnos nem talált! de egy tippet adok egy picit nagyobb.')
elif gondolt_szam > a:
    print('sajnos nem talált! de egy tippet adok egy picit kissebb.')
else:
    print('Nagyon ügyes vagy kitaláltad amire a gép gondolt.')