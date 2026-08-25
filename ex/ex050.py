lista = []

for i in range(1, 7):
    num = int(input(f"digite o numero {i}: "))
    if num % 2 == 0:
        lista.append(num)
print(sum(lista))