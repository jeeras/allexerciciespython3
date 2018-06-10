from math import factorial
n = int(input('Digite um numero para ver seu fator: '))
f = factorial(n)
c = n
while c > 0:
    c = c - 1
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
print(f)