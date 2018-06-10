from datetime import date
from time import sleep

ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano

if idade < 10:
    print('Você tem {} anos'.format(idade))
    print('E sua categoria como nadador é MIRIM')
elif idade >= 10 and idade < 15:
    print('Você tem {} anos'.format(idade))
    print('E sua categoria como nadador é INFANTIL')
elif idade >= 15 and idade < 20:
    print('Você tem {} anos'.format(idade))
    print('E sua categoria como nadador é JUNIOR')
elif idade >= 20 and idade < 26:
    print('Você tem {} anos'.format(idade))
    print('E sua categoria como nadador é SÊNIOR')
else:
    print('Você tem {} anos'.format(idade))
    print('E sua categoria como nadador é MASTER')