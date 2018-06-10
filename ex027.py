tamanho = float(input('\033[35mQual o tamanho da viagem? '))


if tamanho <= 200:
    preço = tamanho * 0.50
    print('\033[32mVocê irá pagar R${:.2f}'.format(preço))
else:
    tamanho > 200
    preço = tamanho * 0.45
    print('\033[31mVocê irá pagar R${:.2f}'.format(preço))