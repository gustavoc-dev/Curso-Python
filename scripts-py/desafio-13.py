#aumento funcionario 15%

salario = float(input('Qual é o salario do funcionario?\nR$'))

aumento = salario*0.15

print('O salário do funcionario que era R${}, agora será R${:.2f}\nCom um aumento de R${:.2f}'.format(salario,salario+aumento,aumento))
