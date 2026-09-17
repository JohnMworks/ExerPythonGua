from random import randint

print("Sou seu computaodr...")
guess = int(input('Tente adivinhar o numero (entre 0 e 10) que pensei: '))
num = randint(0, 10)

while guess != num:
    if guess > num:
        guess = int(input('Quase, um pouco menor, tente de novo: '))
    elif guess < num:
        guess = int(input('Quase, um pouco maior, tente de novo: '))
    
print(f'chute = {guess} ; num = {num}')