#jokenpo
import random
from time import sleep

op = int(input('-=' * 20 + '\n1 - Pedra \n2 - Papel \n3 - Tesoura\n' + '-=' * 20))

#pc = random.randint(1,3)
pc = 1
lista = ['pedra', 'papel', 'tesoura']

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

if (op - pc) % 3 == 0:
    print('O computador jogou {} \n--EMPATE--'.format(lista[pc - 1]))
elif (op - pc) % 3 == 1:
    print('O computador jogou {} \n--VITORIA--'.format(lista[pc-1]))
elif (op - pc) % 3 == 2:
    print('O computador jogou {} \n--DERROTA--'.format(lista[pc-1]))













'''if pc != op:
    if pc == 1 and op == 2:
        print('ganhou')
    elif pc == 1 and op == 3:
        print('perdeu')
    elif pc == 2 and op == 1:
        print('perdeu')
    elif pc == 2 and op == 3:
        print('ganhou de {}'.format(pc))
    elif pc == 3 and op == 1:
        print('ganhou')
    elif pc == 3 and op == 2:
        print('perdeu')
else:
    print('empate')'''