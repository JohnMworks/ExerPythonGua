#80km/h - 7 reais de multa

speed = float(input('Insira a Velocidade: '))

multa = (speed - 80)*7

if speed > 80:
    print('Voçê Foi Multado em  R${:.2f}!'.format(multa))
else:
    print('Voçê não foi multado.')