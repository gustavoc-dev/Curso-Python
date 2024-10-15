import random
print('Escolhi um número entre 0 e 5, tente advinhar qual!')

n = (random.randint(0,10))
count = 0
win = False

while win == False:
    t = int(input('Qual número você acha que é?\n'))
    if t >10 :
        print('Escolha um número entre 0 e 10 apenas!')
    elif n == t:
        print('Você acertou! Eu escolhi o número {}'.format(n))
        win=True
    else:
        print('Você errou! Tente de novo!')
        count +=1
print('Você deu {} palpites até acretar!'.format(count))


