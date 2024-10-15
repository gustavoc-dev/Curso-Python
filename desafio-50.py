s = 0
for c in range(1,7):
    n = int(input('Digite um número:\n'))
    if n%2==0:
        s+=n
print('A soma de todos os pares foi: {}'.format(s))