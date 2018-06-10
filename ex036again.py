

valorcasa = float(input('Valor da casa: '))
valorsalario = float(input('Valor do seu salário: '))
anos = int(input('Em quantos anos irá pagar? '))

meses = anos * 12
cadames = valorcasa / meses

print('Para pagar uma casa de {} reais em {} anos, emprestimo sera de R${:.2f}'.format(valorcasa, anos, cadames))
if cadames >= (valorsalario * 0.30):
    print('Emprestimo negado!')
else:
    print('Emprestimo condedido!')