print('-=' * 20)
print('MAIOR OU MENOR?')
print('-=' * 20)

op1 = int(input('Digite um número inteiro: '))
op2 = int(input('Digite outro valor inteiro: '))

if op1 > op2:
    print('O PRIMEIRO número é o maior.')
elif op2 > op1:
    print('O SEGUNDO número é o maior')
else:
    print('Os dois números são iguais.')