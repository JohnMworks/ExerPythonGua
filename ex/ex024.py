print('--Analizador Cidade com Nome de Santo--')
cidade = str(input('Didite o nome da sua cidade: '))

low = cidade.strip()
low = low.lower()

#res = 'santo' in low (so verifica se tem santo em algum lugar da palavra)
res = low.startswith('santo')

if res == True:
    print('O nome da sua cidade comela com santo')
else:
    print('O nome da sua cidade não começa com santo')