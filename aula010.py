"""nome = str(input('Qual é seu nome: '))
nomeminusculo = nome.lower()
if nomeminusculo == 'luis':
    print('Que nome lindo vc tem')
print('Boa noite {}'.format(nome))"""

nota1 = float(input('\033[33mDigite a primeira nota do aluno: '))
nota2 = float(input('\033[33mDigite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

print('\033[33mA média do aluno foi {:.1f}.'.format(media))

if media >= 6:
    print('\033[32mO aluno teve uma boa nota e não reprovou.')
else:
    print('\033[31mO aluno teve uma nota ruim, e reprovou')