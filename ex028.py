from datetime import date

ano = int(input('\033[31mDigite que ano você quer saber, ou coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[4;32mO ano {} é bissexto!'.format(ano))
else:
    print('\033[4;31mO ano {} não é bissexto!'.format(ano))