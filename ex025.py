from time import sleep

velocidade = float(input('Digite a velocidade do carro: '))
print('PROCESSANDO...')
sleep(5)
multa = (velocidade - 80) * 7

if velocidade > 80:
    print('VOCÊ EXCEDEU O LIMITE DE VELOCIDADE QUE É 80KM/H! MULTADO!')
    print('Valor da multa: R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia motorista, e dirija sempre com atenção!')