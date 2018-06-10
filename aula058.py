from random import randint
tentativas = 1
escolhac = randint(1, 10) #escolha do computador
escolhaj = int(input('Pensei em um numero de 0 a 10, qual seu palpite? ')) #escolha do jogador
while escolhaj != escolhac:
    print('Errou!')
    if escolhaj > escolhac:
        escolhaj = int(input('Menos...'))
        tentativas = tentativas + 1
    if escolhaj < escolhac:
        escolhaj = int(input('Mais...'))
        tentativas = tentativas + 1
if escolhaj == escolhac:
    print('Acertou!')
print('Voce fez {} tentativas, o numero era {}'.format(tentativas, escolhac))
