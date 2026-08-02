n1 = int(input('Digite o numero 1: '))
n2 = int(input('Digite o numero 2: '))
n3 = int(input('Digite o numero 3: '))

if n1 > n2 and n1>n3:
    print('O numero 1 é o maior.')
elif n2>n1 and n2>n3:
    print('O numero 2 é o maior.')
else:
    print('O numero 3 é o maior.')