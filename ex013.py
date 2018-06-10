dias = int(input('Quantos dias alugado: '))
# nota que; cada dia é 60 reais
kmrodados = float(input('Quantos km andou: '))
# nota que; cada km rodado é 0,15 reais

solucaodias = dias * 60
solucaokm = kmrodados * 0.15
solucaogeral = solucaodias + solucaokm

print('Você ira pagar {} reais'.format(solucaogeral))