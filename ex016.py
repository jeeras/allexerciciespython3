import math

angulo = float(input('Digite o valor do angulo: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('O cosseno seno e tangiante do angulo é respectivamente {:.2f}, {:.2f}, {:.2f}'.format(seno, cos, tan))