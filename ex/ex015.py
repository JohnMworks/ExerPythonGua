d = int(input('Digite a qtd de dias alugados: '))
km = float(input('Digite a qtd de km percorridos: '))

tot = (d * 60) + (km * 0.15)

print('o valor total eh de: {}'.format(tot))