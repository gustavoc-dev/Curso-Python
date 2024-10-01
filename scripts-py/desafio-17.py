#Calcule a hipotenusa


import math
oposto = float(input('Informe o cateto oposto:\n'))
adjacente= float(input('Informe o cateto adjacente:\n'))

hipo = math.hypot(oposto,adjacente)

print('A hipotenusa desse triangulo é {:.2f}'.format(hipo))



