#maior que 1250 = 10%   resto=15%

sal = int(input('Digite o valor do salário: '))

if sal > 1250:
    novo_sal = sal * 1.1
else:
    novo_sal = sal * 1.15

print('O novo salário é de R${}'.format(novo_sal))