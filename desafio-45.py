import random

print('JOKENPO!')
n = (random.randint(1,3))

if n == 1:
    n = 'Pedra'
elif n ==2:
    n = 'Papel'
elif n == 3:
    n = 'Tesoura'

eu = int(input('Escolha oque você vai jogar?\n1-Pedra\n2-Papel\n3-Tesoura\n'))

if n == 'Pedra' and eu ==1:
    print('{}!!!'.format(n))
    print('Os 2 jogarem pedra, EMPATE')
elif n =='Pedra' and eu == 2:
    print('{}!!!'.format(n))
    print('Você ganhou!, Papel vence Pedra!')
elif n == 'Pedra' and eu ==3:
    print('{}!!!'.format(n))
    print('Eu ganhei, pedra vence tesoura')
elif n == 'Papel' and eu ==1:
    print('{}!!!'.format(n))
    print('Eu ganhei, papel vence perda')
elif n =='Papel' and eu ==2:
    print('{}!!!'.format(n))
    print('Os 2 jogarem papel, EMPATE')
elif n == 'Papel' and eu ==3:
    print('{}!!!'.format(n))
    print('Você ganhou, tesoura vence papel')
elif n == 'Tesoura' and eu ==1:
    print('{}!!!'.format(n))
    print('Você ganhou, pedra ganha tesoura')
elif n=='Tesoura' and eu ==2:
    print('{}!!!'.format(n))
    print('Você perdeu, tesoura vence papel')
elif n =='Tesoura' and eu ==3:
    print('{}!!!'.format(n))
    print('Os 2 jogarem tesoura, EMPATE')