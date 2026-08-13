pn = float(input('Digite a primeira nota: '))
sn = float(input('Digite a segunda nota: '))

med = (pn + sn) / 2

if med >= 7:
    print(f'Com notas {pn} e {sn}, o aluno está Aprovado')
elif med < 7:
    print(f'Com notas {pn} e {sn}, o aluno está Reprovado')
