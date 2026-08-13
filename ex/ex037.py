#bases de conversao

op = int(input('1 - Binario\n2 - octal\n3 - hexadecimal\nEscolha base de conversão: '))
num = int(input('Digite o numero a ser convertido: '))

if op == 1:
    res = bin(num)
    print('resposta: {}'.format(res))
elif op == 2:
    res = oct(num)
    print('resposta: {}'.format(res))
else:
    res = hex(num)
    print('resposta: {}'.format(res))