sex = str(input('Digite seu sexo [M/F]: '))

while sex not in ('M', 'm', 'F', 'f'):
    sex = str(input('Dados invalidos, Digite seu sexo: '))

print(f'Dado cadastrado como: {sex.upper()}')