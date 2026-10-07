#progressao aritimetica c while

pt = int(input('Digite o primeiro termo: '))
razao = int(input("Digite a razao: "))
con = 11

while con > 0:
    print(pt, ' ' , end='')
    pt = pt + razao
    con = con - 1
    if con == 1:
        print('\nPAUSA')
        con = int(input('Digite quantos ternos vc quer ver a mais: '))
        con += 1