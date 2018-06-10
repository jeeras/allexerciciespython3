peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura (m): '))

imc = peso / (altura ** 2)

print('Seu IMC é : {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc >=18.5 and imc <= 25:
    print('Você está no peso ideal!')
elif imc >= 25 and imc <= 30:
    print('Você está sobrepeso, tente mais exercicios!')
elif imc >= 30 and imc <= 40:
    print('Você está com OBESIDADE!')
else:
    print('Você está com OBESIDADE MÓRBIDA! Cuidado!')