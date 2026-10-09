# progressao aritimetica c while

cores = {
    'limpar': '\033[0m',
    'azul': '\033[34m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'vermelho': '\033[31m',
    'ciano': '\033[36m',
    'roxo': '\033[35m'
}

pt = int(input(f"{cores['azul']}Digite o primeiro termo: {cores['limpar']}"))
razao = int(input(f"{cores['verde']}Digite a razao: {cores['limpar']}"))
con = 11

while con > 0:
    print(f"{cores['ciano']}{pt}{cores['limpar']}", end=' ')
    pt = pt + razao
    con = con - 1
    if con == 1:
        print(f"\n{cores['amarelo']}PAUSA{cores['limpar']}")
        con = int(input(f"{cores['roxo']}Digite quantos termos vc quer ver a mais: {cores['limpar']}"))
        con += 1