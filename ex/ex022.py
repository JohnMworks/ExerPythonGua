nome = str(input("Digite seu nome completo: "))
lista = nome.split()

print('Seu nome em maiusculas é: {}'.format(nome.upper()))
print('Seu nome em minusculas é: {}'.format(nome.lower()))
print('Seu nome tem {} caracteres'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(lista[0], len(lista[0])) )
