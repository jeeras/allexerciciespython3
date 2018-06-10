
co = float(input('Medida do cateto oposto: '))
ca = float(input('Medida do cateto adjacente: '))

hipotenusa = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

# or

import math

co = float(input('Medida do cateto oposto: '))
ca = float(input('Medida do cateto adjacente: '))

hi = math.hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))
