#num = int(input('Digite o numero: '))
num = 500

lista = []

for i in range(1, num+1):
    if i % 3 == 0 and i % 2 == 1:
        lista.append(i)
        
res = sum(lista)
print(res)