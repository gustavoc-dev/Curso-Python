f = str(input('Digite uma frase:\n'))
right = f.lower().replace(' ','')
array = list(right)
teste = []

reverse = len(array)

for c in range(0,reverse):
    teste.append(array[reverse-(1+c)])

if array == teste:
    print('É palindromo')
else:
    print('Não é palindromo')