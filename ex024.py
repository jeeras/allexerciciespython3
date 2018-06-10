import random
import time


print("""\033[31m==================
        JOGO DA ADIVINHAÇÃO
        ===================""")

print('TENTE ADIVINHAR O NÚMERO, QUE EU COMPUTADOR PENSEI! (DICA: ENTRE 0 E 10)')

numeroescolhido = random.randint(0, 10)


chute = int(input('Seu chute: '))
print('Analisando...\033[m')
time.sleep(2.5)

if chute == numeroescolhido:
    print('\033[35mParabéns, você me venceu!')
else:
    print('\033[31mHAHAHA! Você perdeu para mim!')
    print('\033[31mO número escolhido por mim era: {}'.format(numeroescolhido))
