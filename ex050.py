soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um numero inteiro: '))
    if num % 2 == 0:
        cont = cont + 1
        soma = soma + num
print('Foram {} numeros, e a soma é {}'.format(cont, soma))