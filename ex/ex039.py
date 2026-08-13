#alistamento militar

ano = int(input('ano de nascimento: '))
at = 2026
alis = ano + 18

if alis < at:
    print('Voçê deveria ter se alistado em {} kk'.format(alis))
elif alis > at:
    print('Voçê deverá se alistar em {}'.format(alis))
else:
    print('Voçê deve se alistar esse ano')