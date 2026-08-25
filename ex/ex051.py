#an = a1 + (n - 1) * r (PA)

pt = int(input('Digite o 1° termo: '))
razao = int(input('Digite a razão: '))

for i in range(pt, pt*11, razao):
    print(i)