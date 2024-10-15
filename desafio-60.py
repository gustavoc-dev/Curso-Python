n = int(input('Digite o número que você quer o fatorial:\n'))
fac = n
calc = 1
while fac > 1:
    calc *= fac
    fac -=1
print('O fatorial de {} é {}'.format(n,calc))