num = int(input('Digite um numero: '))

res = 0

for i in range(1, num+1,):
    #se for divisivel pelo contador
    if num % i == 0:
        res = res + 1
        print("\033[32m" + str(i) + "\033[0m")
    else:
        print("\033[31m" + str(i) + "\033[0m")
if res == 2:
    print('eh primo')
else:
    print('nao eh primo')
    
    
    
    
    