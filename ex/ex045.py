#jokenpo
import random

op = int(input('-=' * 20 + '\n1 - Pedra \n2 - Papel \n3 - Tesoura\n' + '-=' * 20))

pc = random.randint(1,3)

if pc == 1 and op == 2:
    print('ganhou')
elif pc == 1 and op == 3:
    print('perdeu')
elif pc == 2 and op == 1:
    print('perdeu')
elif pc == 2 and op == 1:
    print('ganhou de {}'.format(pc))
elif pc == 3 and op == 1:
    print('ganhou')
elif pc == 3 and op == 2:
    print('perdeu')