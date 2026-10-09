'''

def fat(n):

    if n == 1 or n == 0:
        return 1

    else:

        return n * fat(n - 1)
    

print(fat(5))
'''


def cont(num):

    if num < 0:

        print('fim')
        return
    

    print(num)
    

    cont(num - 1)
    
        
cont(900)