inicio = int(input('Inicio da Progressão:\n'))
razao =int(input('Razão da Progressão:\n'))
termo = inicio
count = 1

while count<=10:
    print(termo)
    termo+=razao
    count+=1
print('Fim')