a = float(input('Valor do primeiro segmento: '))
b = float(input('Valor do segundo segmento: '))
c = float(input('Valor do terceiro segmento: '))

if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    print('Pode formar um triangulo.')
    if a == b and a == c:
        print('É um triangulo EQUILATERO')
    elif a != b and a != c and b != a and b != c and c != a and c != b:
        print('É um triangulo ESCALENO')
    else:
        print('É um triangulo ISOSCELES')
else:
    print('Não pode formar um triangulo')

