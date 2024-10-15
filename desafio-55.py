array = []

for c in range(0,5):
    peso = int(input('Digite o peso:\n'))
    array.append(peso)

print('O maior peso inserido foi {}kg e o menor foi {}kg.'.format(max(array),min(array)))