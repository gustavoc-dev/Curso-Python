n = float(input('Qual é a distancia da viagem?\n'))

if n <= 200:
    print('O valor da passagem é R${:.2f} para a distancia de {:.2f}km'.format(n*0.50,n))
else:
    print('O valor da passagem é R${} para a distancia de {}km'.format(n*0.45,n))