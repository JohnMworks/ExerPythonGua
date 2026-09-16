maior = 0.
menor = 0.

for i in range(1,6):
    pes = float(input(f'Digite o peso da {i}ª pessoa: '))
    if i == 1:
        maior = pes
        menor = pes
    else:   
        if pes > maior:
            maior = pes
        if pes < menor:
            menor = pes
            
print(f'O menor peso lido foi: {menor}')
print(f'O maior peso lido foi: {maior}')