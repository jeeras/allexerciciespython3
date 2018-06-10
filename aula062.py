pt = int(input('Primeiro termo'))
razao = int(input('Razão da PA'))
cont = 1
termo = pt

while cont <= 10:
    print('{}'.format(termo), end=' > ')
    termo = termo + razao
    cont = cont + 1
print('PAUSA')
q_termos = int(input('Quantos termos quer mostrar a mais [0 para acabar]'))
if q_termos == 0:
    print('Finalizado.')
while cont <= q_termos:
    print('{}'.format(termo), end=' > ')
    termo = termo + razao
    cont = cont +1
