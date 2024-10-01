n = int(input('Digite um ano:\n'))
n = str(n)
last2 = n[2]+n[3]
last2 = int(last2)

if last2%4 ==0:
    print('O ano {} é BISSEXTO!'.format(n))
else:
    print('O ano {} não é BISSEXTO!'.format(n))