palavra = str(input('Digite uma palavra: '))

lista = list(palavra)

listainv = lista[::-1]


print(f'O inverso de {lista} é {listainv}')

if lista == listainv:
    print('Temos um palindromo!')
else:
    print('Não temos um palindromo.')