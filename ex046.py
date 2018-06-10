from time import sleep
print('A contagem REGRESSIVA está para começar!!!')
sleep(5)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[33mBOOOM! VIVA ANO NOVO')