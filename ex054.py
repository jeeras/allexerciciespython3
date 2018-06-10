#AGORA VAIIIIIIIIIIIIIIII
from datetime import date
menor = 0
maior = 0
for pess in range(1, 8):
    ano = int(input('Digite em que ano nasceu a {}º pessoa: '.format(pess)))
    idade = date.today().year - ano
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print('Temos {} pessoas de maior, e {} pessoas de menor.'.format(maior, menor))