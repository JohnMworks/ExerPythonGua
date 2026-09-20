num = int(input('Digite um numero p calcular o ftorial: '))
res = 1

while num > 1:
    res = res * num
    num = num - 1

print(res)