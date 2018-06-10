num1 = int(input('\033[35mDigite um número: '))
num2 = int(input('\033[35mDigite outro número: '))
num3 = int(input('\033[35mDigite outro número: '))

menor = num1
maior = num3

if num2<num3 and num2<num1:
    menor = num2
if num3<num2 and num3<num1:
    menor = num3
# maior
if num1>num2 and num1>num3:
    maior = num1
if num2>num1 and num2>num3:
    maior = num2
print('\033[32mO menor número foi {}, e o maior foi {}'.format(menor, maior))

