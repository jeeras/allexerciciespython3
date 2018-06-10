print('-=' * 11)
print('GERENCIADOR DE COMPRAS')
print('-=' * 11)
gastou = float(input('Quanto você gastou em compras?'))
print('Você vai pagar em: ')
print('[ 1 ]Dinheiro á vista')
print('[ 2 ]Á vista no cartão')
print('[ 3 ]2x no cartão')
print('[ 4 ]3x ou mais no cartão')

opcao = str(input('Sua opção: '))
if opcao == '1':
    print('Você ira pagar {:.2f} a vista.'.format(gastou - (gastou * 0.10)))
elif opcao == '2':
    print('Você ira pagar {:.2f} a vista no cartão'.format(gastou - (gastou * 0.5)))
elif opcao == '3':
    print('Você ira pagar {:.2f} 2x no cartão'.format(gastou))
elif opcao == '4':
    print('Quantas parcelas?')
    parcelas = int(input(''))
    print('Você comprando com {} parcelas irá pagar {:.2f}'.format(parcelas, gastou + (gastou * 0.20)))
else:
    print('\033[32mVocê não digitou 1, 2, 3 ou 4 ')

