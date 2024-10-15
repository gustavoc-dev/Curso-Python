n1 = float(input('Digite a primeira nota\n'))
n2 = float(input('Digite a segunda nota\n'))

media = (n1+n2)/2

if media <5:
    print('Reprovaddo! Média {:.2f}'.format(media))
elif media < 6.9:
    print('Recuperação! Média {:.2f}'.format(media))
elif media >= 7:
    print('Aprovado! Média {:.2f}'.format(media))