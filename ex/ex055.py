maior = 0.
menor = 0.

for i in range(1,6):
    pes = float(input('Digite seu peso: '))
    if i == 1:
        maior = pes
        menor = pes
    else:   
        if pes > maior:
            maior = pes
        if pes < menor:
            menor = pes
            
print(menor)
print(maior)