preco = float(input('Digite o valor do produto: '))
op = float(input('''Digite a forma de pagamento:
1 - Dinheiro ou cheque
2 - cartão
--> '''))

if op == 2:
    parce = int(input('''Deseja dividir em quantas vezes?
    1 - A vista no cartão
    2 - Duas vezes
    3 - TrêS vezes 
    --> '''))

if op == 1:
    print('O valor final é de R${}'.format(preco - (preco * 0.1)))
elif op == 2 and parce == 1:
    print('O valor final é de R${}'.format(preco - (preco * 0.05)))
elif op == 2 and parce == 2:
    print('O valor final é de R${}'.format(preco))
else:
    print('O valor final é de R${}'.format(preco + (preco * 0.2)))