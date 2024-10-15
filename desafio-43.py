peso = float(input('Qual é o seu peso?\n'))
altura = float(input('Qual é a sua altura?\n'))

imc = peso / (altura*2)

if imc <18.5:
 print('Abaixo do peso. IMC: {:.2f}'.format(imc))
elif imc <25:
 print('Peso Ideal IMC: {:.2f}'.format(imc))
elif imc <30:
 print('Sobrepeso. IMC: {:.2f}'.format(imc))
elif imc <40:
 print('Obesidade. IMC: {:.2f}'.format(imc))
elif imc >40:
 print('Obesidade mórbida. IMC: {:.2f}'.format(imc))