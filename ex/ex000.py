num = int(input("aaa"))

print(f"a   {num}  a")

palavra = input("Digite uma palavra: ")

# Remove espaços e transforma em letras minúsculas
palavra_limpa = palavra.replace(" ", "").lower()

# Inverte a string usando slice
palavra_invertida = palavra_limpa[::-1]

# Compara a palavra limpa com a invertida
if palavra_limpa == palavra_invertida:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")