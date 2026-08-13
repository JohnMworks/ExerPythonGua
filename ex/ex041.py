#9 mirim   14 infantil   19 junior   20 senior    acima de 20 master

idade = int(input('Digite sua idade: '))

if idade < 9:
    print('Sua categoria é mirim')
elif idade < 14:
    print('Sua categoria é infantil')
elif idade < 19:
    print('Sua categoria é junior')
elif idade < 20:
    print('Sua categoria é senior')
else:
    print('Sua categoria é master')