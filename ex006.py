print("Digite uma medida em metros: ")
medida = float(input(''))

medidakm = medida / 1000

medidacm = medida * 100

medidamm = medida * 1000

print("Sua medida foi {}, em km é {}, em cm é {}, em mm é {}".format(medida, medidakm, medidacm, medidamm))