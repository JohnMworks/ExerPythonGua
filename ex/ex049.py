num = int(input('Digite um número para receber sua tabuada: '))

print("=+" * 8)

for i in range (11):
    print(f'   {num} x {i} = {num*i}')

print("=+" * 8)