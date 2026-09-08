ano = 2026
idades = []

for i in range(0,7):
    idadee = int(input(f"Digite o ano de nascimento da pessoa {i+1}: "))
    idades.append(idadee)

menor = 0
maior = 0
for i in range(0,7):
    if (idades[i]) <= 21:
        menor += 1
    else:
        maior += 1
        
print(f"Existem {menor} menores de idade")
print(f"Existem {maior} maiores de idade")