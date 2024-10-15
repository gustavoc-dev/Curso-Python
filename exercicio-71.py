print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
n = int(input('Qual o valor que você quer sacar?\nR$'))
print('='*30)
nota50 = 0
nota20 = 0
nota10 = 0
nota1=0

if n >1000:
    nota50 += n//50
    n = n-(50*nota50)
    if n > 100:
        nota50 += n//50
        n = n-(50*nota50)
    if n <100:
        nota20+= n//20
        n = n-(20*nota20)
        nota10+=n//10
        n = n-(10*nota10)
    if n <10:
        nota1+= n//1
        n = n-(1*nota1)


print(f'Total de {nota50} cédulas de R$50')
print(f'Total de {nota20} cédulas de R$20')
print(f'Total de {nota10} cédulas de R$10')
print(f'Total de {nota1} cédulas de R$1')
