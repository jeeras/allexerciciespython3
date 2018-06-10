from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano

if idade < 18:
    print('Você ainda não pode se alistar, você tem {} anos, apenas quando passar {} ano(s), você poderá se alistar.'.format(idade, 18 - idade))
    print('Apenas em {}'.format((18 - idade) + date.today().year))
elif idade > 18:
    print('Você já deveria ter se alistado a {} ano(s)'.format(idade - 18))
    print('Já deveria ter se alistado em {}'.format(date.today().year - (idade - 18)))
else:
    print('Já está na hora de você se alistar!')
    print('Aliste-se imediatamente!')