inicio = int(input('Inicio da Progressão:\n'))
razao =int(input('Razão da Progressão:\n'))
termo = inicio
count = 1
total = 0
mais = 10
while mais !=0:
    total += mais
    while count<=total:
        print(termo)
        termo+=razao
        count+=1
    print('Pausa')
    mais = int(input('Quantos termos a mais você quer?'))
print('Fim')