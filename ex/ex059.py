n1 = int(input('Digite o numero 1: '))
n2 = int(input('Digite o nuemro 2: '))
op = 0

while op != 5:
    print('--=' * 20)
    op = int(input('''
[1] = somar
[2] = multiplicar
[3] = maior
[4] = novos numeros
[5] = sair do programa
num = '''))
    print('--=' * 20)
    
    if op == 1:
        res = n1 +n2
        print(f'O resultado da soma é {res}.')
    elif op == 2:
        res = n1 * n2
        print(f'O resultado da multiplicação é {res}')
    elif op == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        if n2 > n1:
            print(f'{n2} é maior que {n1}')
        if n1 == n2:
            print(f'{n1} e {n2} São iguais')
    elif op == 4:
        print('Novos Numeros: ')
        n1 = int(input('Digite o numero 1: '))
        n2 = int(input('Digite o nuemro 2: '))

print('Fim!')