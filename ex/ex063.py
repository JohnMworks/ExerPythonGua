#fibonacci 1,1,2,3,5,8
res = 0
i = 10
lista =[0,1]

while i > 0:
    res = sum(lista[-2:])
    lista.append(res)
    i -= 1
    if i == 1:
        print(lista)
        i = int(input("Digite quantos termos a mais voçê gpstaria de ver: "))
        i + 1
    if i == 0:
        break
    
print(lista)

    
    
    
    
    
