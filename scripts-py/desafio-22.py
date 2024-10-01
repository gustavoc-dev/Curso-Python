nome = input('Escreva Gseu nome completo:\n')
print('Seu nome em maiúsculo: {}\nSeu nome em minúsculo: {}'.format(nome.upper(),nome.lower()))
print('Total de letras no seu nome completo: {}'.format(len(nome.replace(' ',''))))
print('Total de letras no seu primeiro nome: {}'.format(len(nome.split()[0])))