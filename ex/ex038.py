num1 = int(input('Digite o numero 1: '))
num2 = int(input('Digite o numero 2: '))

if num1 > num2:
    print('{} é maior que {}'.format(num1, num2))
elif num2 > num1:
    print('{} é maior que {}'.format(num1, num2))
else:
    print('{} e {} são iguais'.format(num1, num2))