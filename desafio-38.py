n1 = int(input('Digite um número\n'))
n2 = int(input('Digite um número\n'))

if n1 > n2:
    print('O Primeiro valor:{} é maior que o Segundo:{}'.format(n1,n2))
elif n2 > n1:
    print('O Segundo valor:{} é maior que o Primeiro:{}'.format(n2,n1))
elif n1 == n2:
    print('{} e {} são iguais'.format(n1,n2))