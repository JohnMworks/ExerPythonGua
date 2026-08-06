#Emprestimo bancario
#valor da casa; salariodo comprador; qtd anos p pagar

vcasa = float(input('Digite o valor da casa: '))
sal = float(input('Digite o salário do comprador: '))
anos = int(input('Digite a qtd de anos para pagar a ksa: '))

meses = anos * 12
prestacao = vcasa / meses

if prestacao > (sal * 0.3):
    print('Emprestimo negado!, o valor da prestação ultrapassa 30% do salario mensal do comprador.')
else:
    print('Emprestimo aprovado!, o valor da prestação não ultrapassa 30% do salario mensal do comprador.')