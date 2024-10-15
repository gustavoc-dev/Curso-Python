from datetime import date

ano = int(input('Em que ano você nasceu?\n'))
anoAtual = date.today().year
idade = anoAtual - ano

if idade <18:
    print('Você ainda vai se alistar, faltam {} pra você se alistar!'.format(18-idade))
elif idade >18:
    print("Você já se alistou, foi há {} anos atrás".format(idade-18))
else:
    print("Você se alista esse ano")