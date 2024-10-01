# Desconto de 5%

p = float(input('Qual é o preço do produto?\n'))

desconto = (p*0.05)


print('O produto que valia R${}, valerá R${:.2f} com 5 por cento de deconto'.format(p,p-desconto))