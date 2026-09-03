# Soma dos numeros multiplos de 3

#num = int(input('Digite o numero: '))
num = 500

lista = []

for i in range(1, num+1, 2):
    if i % 3 == 0:
        lista.append(i)
        
res = sum(lista)
print(res)