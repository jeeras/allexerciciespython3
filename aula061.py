
print('Leitor PA')
pt = int(input('Primeiro termo: '))
razao  = int(input('Razão: '))
termo = pt
cont = 1

while cont <= 10:
    print('{} >'.format(termo), end=' ')
    termo = termo + razao
    cont = cont + 1
print('acabou')
