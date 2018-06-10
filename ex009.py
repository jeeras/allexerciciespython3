alturaparede = float(input('Digite a altura da parede: '))
larguraparede = float(input('Digite a largura da parede: '))

area = alturaparede * larguraparede

print("Sua area é de {}.".format(area))

# Considerando que: a cada 2m² sera usado 1L de tinta então:

tinta = area / 2

print("Vc vai precisar de {} litros de tinta".format(tinta))