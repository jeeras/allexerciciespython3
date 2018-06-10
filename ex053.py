frase = str(input('Digite uma frase: ')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
for letras in range(junto, -1):
    print(letras)