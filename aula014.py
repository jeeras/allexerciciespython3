# se você está vendo isso, provavelmente sabe do meu fracasso com o FOR

# mas saiba que eu não vou desistir
'''além de dominar o for
eu irei dominar python
e trabalhar em alguma empresa famosa ok
for eu consigo entender fácil daqui a alguns meses, então menas ok'''
soma = 0
n = 0
r = 'S'
par = 0
impar = 0

while r == 'S':
    valor = int(input('digite um valor: '))
    n = n + 1
    if valor % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
    soma = soma + valor
    r = str(input('Quer continuar? [S/N]')).upper().strip()
print('vc digitou {} numeros e a soma de todos os numeros e {}, tem {} numeros pares e {} numeros impar'.format(n, soma, par, impar))