n1 = int(input('Digite a medida 1: '))
n2 = int(input('Digite a medida 2: '))
n3 = int(input('Digite a medida 3: '))

if n1 < n2+n3 and n2 < n1+n3 and n3 < n2+n1:
    print('Os ângulos inseridos podem formar um trinângulo')
else:
    print('Os ângulos inseridos não podem formar um trinângulo')
