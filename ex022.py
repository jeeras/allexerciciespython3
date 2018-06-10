frase = str(input('Digite uma frase: ')).strip()
fraselower = frase.lower()
if fraselower.count('a') >= 2 :
    print('A letra A apareceu {} vezes na frase'.format(fraselower.count('a')))
elif fraselower.count('a') < 1 :
    print('a letra A não existe na frase')
else:
    print('A letra A apareceu uma vez na frase')

print('A primeira letra A que apareceu foi na posição {}'.format(fraselower.find('a') + 1))
print('E a ultima letra A que apareceu foi na posição {}'.format(fraselower.rfind('a') + 1))