num = int(input('Digite o numero para ver sua tabuada: '))
cont = 0
for cont in range(0, 10):
    cont = cont + 1
    print('{} x {} = {}'.format(num, cont, (num * cont)))