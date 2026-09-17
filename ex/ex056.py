mm20a = 0
med_idade = 0.
hom_velho = 0
nom_homem_velho = ''
idades = []

for i in range(1,5):
    print('-'*5, f'{i}ª PESSOA', '-'*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: '))
    
    #mm20a
    if sex == 'F' and idade < 20:
        mm20a = mm20a + 1
    
    #adiciona as idades na lista 'idades'
    idades.append(idade)
    
    #homem mais velho
    if sex == 'M' and idade > hom_velho:
        hom_velho = idade
        nom_homem_velho = nome
        
med_idade = sum(idades)/len(idades)

print(f'A média de idade do grupo é de {med_idade} anos')
print(f'O homem mais velho tem {hom_velho} anos e se chama {nom_homem_velho}')
print(f'Ao todo são {mm20a} mulheres com menos de 20 anos')

#sex in 'Mm' ; sex in 'Ff'