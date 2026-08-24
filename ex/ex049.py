num = int(input('Digite um número para receber sua tabuada: '))

print("=+" * 8)
for i in range (11):
    res = num *i
    print(f'   {num} x {i} = {res}')
print("=+" * 8)