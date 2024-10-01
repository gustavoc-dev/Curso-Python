salario = float(input('Qual é o seu salário?:\n'))

if salario > 1250:
    print('Você recebeu um aumento de 10%, R${:.2f}, seu salário agora é R${:.2f}'.format(salario*0.10,salario + (salario*0.10)))
else:
     print('Você recebeu um aumento de 15%, R${:.2f}, seu salário agora é R${:.2f}'.format(salario*0.15,salario + (salario*0.15)))