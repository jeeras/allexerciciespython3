from time import sleep

valorcasa = float(input('\033[33mFale o valor da casa: R$'))
valorsalario = float(input('\033[33mFale o seu salario: R$'))
emprestimoanos = int((input('\033[33mEm quantos anos pretende pagar: ')))
valorsalario30porcento = valorsalario * 0.30

print('PROCESSANDO...')
sleep(5)

print('Para pagar uma casa de {} em {} anos a prestação será de R${:.2f}'.format(valorcasa, emprestimoanos, valorcasa / (emprestimoanos * 12)))
if valorsalario30porcento <= valorcasa / (emprestimoanos * 12):
    print('\033[31mEmprestimo nao condedido')
else:
    print('\033[32mEmprestimo feito com sucesso')