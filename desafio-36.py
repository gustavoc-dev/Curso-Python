valorCasa = float(input("Qual é o valor da casa?\n"))
salario = float(input('Quanto é o salário do(a) comprador?\n'))
anos = int(input("Em quantos anos ele(a) vai pagar?\n"))

parcela = ((valorCasa/anos)/12)*100
porcentagem = salario*0.30

if parcela >= porcentagem:
    print("Financiamento negado")
else:
    print("Financiamento aprovado! você pagará R${:.3f} por mês durante {} anos".format(parcela,anos))


