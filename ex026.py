num = int(input('\033[33mMe diga um numero inteiro qualquer: '))
resultado = num % 2
if resultado == 0:
    print('\033[34mO número {} recebe o resultado PAR'.format(num))
else:
    print('\033[31mO número {} recebe o resultado ÍMPAR'.format(num))