#Algoritmo que calcule, dobro, triplo e raiz quadrada

n = int(input('Digite um número:\n'))

dobro = n*2
triplo = n*3
raiz = n**(1/2)

print('O dobro de {} é {}\nO triplo é {}\nA Raiz Quadrada é {:.2f}'.format(n,dobro,triplo,raiz))