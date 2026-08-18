km = float(input('Digite a quantidade de km: '))

if km < 200:
    preco = km/2
    print('O valor ficou R${:.2f}'.format(preco))
else:
    preco = km/2.2
    print('O valor ficou R${:.2f}'.format(preco))

    print()



