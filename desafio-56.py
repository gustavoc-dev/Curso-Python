somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1,5):
    print('------ {}º PESSOA -------'.format(p))
    
    nome = str(input('Nome:\n')).strip()
    idade = int(input('Idade:\n'))
    sexo = str(input('Sexo [M/F]:\n')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <20:
        totmulher20 += 1

mediaidade = somaidade / 4
print('Media de idade: {}'.format(mediaidade))
print('Homem mais velho: {}, idade: {}'.format(nomevelho,maioridadehomem))
print('Mulheres com menos de 20: {}'.format(totmulher20))
