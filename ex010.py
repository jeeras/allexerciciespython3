preço = float(input('Qual o preço do produto? $: '))

promoção = preço * 0.05

promoçãofeita = preço - promoção

print("O produto que antes custava {} agora custa {}.".format(preço, promoçãofeita))