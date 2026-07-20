import random
no1 = str(input('Digite o primeiro nome: '))
no2 = str(input('Digite o segundo nome: '))
no3 = str(input('Digite o terceiro nome: '))

lista = [no1,no2,no3]
random.shuffle(lista)

print('Aqui esta a lista embaralhada: {}'.format(lista))