import time

contagem = int(input('Digite um número para iniciar a contagem: '))

for i in range(contagem, -1, -1):
    time.sleep(1)
    print(i)
print('Boom!')