import random
no1 = str(input('Digite o primeiro nome: '))
no2 = str(input('Digite o segundo nome'))
no3 = str(input('Digite o terceiro nome'))

list = [no1, no2, no3]
escolhido = random.choice(list)

print('o item escolhido é: {}'.format(escolhido))