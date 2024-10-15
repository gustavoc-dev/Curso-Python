inicio = int(input('Inicio da Progressão:\n'))
razao =int(input('Razão da Progressão:\n'))
decimo = inicio + (10-1) * razao
for c in range(inicio,decimo+razao,razao):
    print(c)

# n = str(input(''))
# array = list(n)
# print(array)