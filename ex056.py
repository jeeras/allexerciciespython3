nome = 0
idademedia = 0
homem_maisv = 0
mulher_menor = 0
idade = 0
cont = 0

for p in range(1, 5):
    print('=== {}º pessoa ==='.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]'))
    idademedia = (idade + idademedia) / p
if sexo == 'm':
    if idade > homem_maisv:
        homem_maisv = nome
    else:
        print('nao existem homens')
elif sexo == 'f':
    if idade < 20:
        cont = cont + 1 #prefiro usar assim do que cont += 1
    else:
        print('nao existem mulheres no grupo')
print('a idade media é {:.2f}, o homem mais velho é {}, existem {} mulher com menos de vinte anos no grupo'.format(idademedia, homem_maisv, cont))
