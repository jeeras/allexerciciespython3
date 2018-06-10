r1 = float(input('\033[33mDigite o valor da primeira reta: '))
r2 = float(input('\033[33mDigie o valor da segunda reta: '))
r3 = float(input('\033[33mDigite o valor da terceira reta: '))

if (r2 - r3) < r1 < r2 + r3 and (r1 - r3) < r2 < r1 + r3 and (r1 - r2) < r3 < r1 + r2:
    print('\033[4;32mEssas medidas podem formar um triangulo!')
else:
    print('\033[4;31mNão pode formar um triangulo!')