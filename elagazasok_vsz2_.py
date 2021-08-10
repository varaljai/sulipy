a = int(input('Játszunk fej vagy írást, a fej lesz az 1-es, az írás pedig a 2-es tippeld meg hogy milesz én fel dobok egy érmét és a végen elmondom hogy eltaláltad-e.'))
import random

szam = random.randint(1,2)


if szam == a :
    print('eltaláltad, ügyes vagy!')
else:
    print('nem sikerült eltalálni majd kövinek.')