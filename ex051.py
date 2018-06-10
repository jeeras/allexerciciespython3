print('Leitor de PA socorro')
pt = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for cont in range(pt, 11, razao):
    print(cont, end=' → ')
print('acabou')