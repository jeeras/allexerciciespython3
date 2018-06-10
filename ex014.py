import math
n1 = float(input('digite um numero decimal (utilize o ponto) '))
print('Seu numero {} agora vira {}'.format(n1, math.floor(n1)))

# or

'''print("Seu numero e {} e viro {}".format(n1, math.trunc(n1)))'''

# or you can do

'''print("Seu numero e {} e viro {}".format(n1, int(n1)))'''