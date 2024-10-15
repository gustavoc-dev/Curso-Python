sexo = ''

while sexo !='M' and sexo !='F':
    sexo = str(input('Qual é o seu sexo: [M/F]?\n')).upper()
    if sexo !='M' and sexo !='F':
        print('Opção Inválida')
print('Obrigado por informar seu sexo!')