#progressao aritimetica c while

pt = int(input('Digite o primeiro termo: '))
razao = int(input("Digite a razao: "))
con = 10

while con > 1:
    print(pt, ' ' , end='')
    pt = pt + razao
    con = con - 1