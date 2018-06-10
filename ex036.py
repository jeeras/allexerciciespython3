from time import sleep
nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
media = (nota1 + nota2) / 2
print('PROCESSANDO...')
sleep(2.5)

if media < 5:
    print('O aluno está reprovado. Pois tirou {} na média.'.format(media))
elif media >= 5 and media < 7:
    print('O aluno está de recuperação. Pois tirou {} na média.'.format(media))
else:
    print('O aluno está APROVADO pois ficou com {} de média'.format(media))