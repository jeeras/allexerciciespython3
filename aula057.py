sexo = str(input('Informe seu sexo [M/F]')).upper().strip()
while sexo not in "MF":
    sexo = str (input('Dados invalidos. Tente novamente informar o sexo: ')).upper().strip()
print('Sexo {} registrado'.format(sexo))