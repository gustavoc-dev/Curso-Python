import random
print('Escolhi um número entre 0 e 5, tente advinhar qual!')
n = (random.randint(0,5))
t = int(input('Qual número você acha que é?\n'))
if t >5 :
    print('Escolha um número entre 0 e 5 apenas!')
elif n == t:
    print('Você acertou! Eu escolhi o número {}'.format(n))
else:
    print('Você errou! Eu escolhi {} e você {}'.format(n,t))
