salario = float(input('\033[36mDigite o salário do funcionario: '))

if salario < 1250:
    novosalario = salario * 0.15
    novosalario2 = novosalario + salario
    print('\033[4;33mO novo salário será: {}'.format(novosalario2))
else:
    novosalario = salario * 0.10
    novosalario2 = novosalario + salario
    print('\033[4;33mO novo salário será: {}'.format(novosalario2))