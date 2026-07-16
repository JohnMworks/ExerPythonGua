import math
co = float(input('digite o cateto oposto: '))
ca = float(input('digite o cateto adjacente: '))
hip = math.hypot(co,ca)
print('A hipotenusa eh {}'.format(hip))



'''from math import sqrt
co = float(input('digite o cateto oposto: '))
ca = float(input('digite o cateto adjacente'))
hip = (ca**2)+(co**2)
print('O valor da hipotenusa eh {:.2f}'.format(sqrt(hip)))'''