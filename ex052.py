num = int(input('Digite um número: '))
total = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[34m', end=' ')
    print('{}'.format(c), end=' ')
print('\no numero {} foi divisivel {} vezes'.format(num, total))

if total == 2:
    print('esse numero é primo')
else:
    print('esse numero nao e primo')