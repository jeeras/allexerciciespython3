import random

nome1 = str(input('Digite o nome: '))
nome2 = str(input('Digite o nome: '))
nome3 = str(input('Digite o nome: '))

lista = [nome1, nome2, nome3]
escolhido = random.choice(lista)

print("O aluno escolhido foi {}".format(escolhido))
