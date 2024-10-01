v = int(input('Qual é a velocidade do carro?\n'))
multa = v*7
if v >80:
    print('Você foi multado por andar em {}km/h. Sua multa será de R${}'.format(v,multa))
else:
    print('Você está dentro do limite de velocidade.')