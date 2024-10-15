n = 0
count = 0
soma = 0
while n!=999:
    n=int(input('Digite um número:\n'))
    if n!=999:
        count += 1
        soma +=n
print('Foram digitados {} números, e a soma deles foi {}'.format(count,soma))