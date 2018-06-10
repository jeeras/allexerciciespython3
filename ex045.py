from random import randint
from time import sleep

print('Sua opção: ')

print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

opcão = int(input('Qual sua jogada?'))

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
jogadapc = randint(0, 2)
if opcão == 0 and jogadapc == 0:
    print('-=-=-= RESULTADOS =-=-=-')
    print('EMPATE')
elif opcão == 0 and jogadapc == 1:
    print('-=-=-= RESULTADOS =-=-=-')
    print('Computador ganhou!')
elif opcão == 0 and jogadapc == 2:
    print('-=-=-= RESULTADOS =-=-=-')
    print('Você ganhou!')
elif opcão == 1 and jogadapc == 0:
    print('-=-=-= RESULTADOS =-=-=-')
    print('Você ganhou!')
elif opcão == 1 and jogadapc == 1:
    print('-=-=-= RESULTADOS =-=-=-')
    print('EMPATE!')
elif opcão == 1 and jogadapc == 2:
    print('-=-=-= RESULTADOS =-=-=-')
    print('Computador ganhou!')
elif opcão == 2 and jogadapc == 0:
    print('-=-=-= RESULTADOS =-=-=-')
    print('Computador ganhou!')
elif opcão == 2 and jogadapc == 1:
    print('-=-=-= RESULTADOS =-=-=-')
    print('Você ganhou!')
elif opcão == 2 and jogadapc == 2:
    print('-=-=-= RESULTADOS =-=-=-')
    print('EMPATE!')
else:
    print('Você não digitou 0, 1 ou 2. Tente novamente')




