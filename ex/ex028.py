import random

a = random.randint(0,5)

num = int(input('Vou pensar em um numero entre 0 e 5, tente adivinhar: '))

if num == a:
    print('Parabens, eu realmente pensei no {}'.format(num))
else:
    print('Errou! eu pensei no {}, não no {}'.format(a,num))