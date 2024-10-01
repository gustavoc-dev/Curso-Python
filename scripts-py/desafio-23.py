numero = input('Digite um número de 0 a 9999:\n')

if len(numero) == 4:
    print('\nUnidade:{}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(numero[3],numero[2],numero[1],numero[0]))
elif len(numero) == 3:
    print('\nUnidade:{}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(numero[2],numero[1],numero[0],0))
elif len(numero) == 2:
    print('\nUnidade:{}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(numero[1],numero[0],0,0))
elif len(numero) == 1:
    print('\nUnidade:{}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(numero[0],0,0,0))