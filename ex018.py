import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
lista = [n1 ,n2, n3]
random.shuffle(lista)

print('A ordem de apresentação será: ')
print(lista)