from datetime import date
ano = int(input('Qual é o ano de nascimento do atleta?\n'))
atual = date.today().year

if atual - ano <=9:
    print(atual - ano)
    print('Atleta Mirim!')
elif atual - ano <=14:
    print(atual - ano)
    print('Atleta Infantil!')
elif atual - ano <=19:
    print(atual - ano)
    print('Atleta Júnior')
elif atual - ano ==20:
    print(atual - ano)
    print('Atleta Sênior')
elif atual - ano >20:
    print(atual - ano)
    print('Atleta Master')