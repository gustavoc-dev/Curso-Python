n1 = int(input('Digite um valor:\n'))
n2 = int(input('Digite outro valor:\n'))
opcao = 0

while opcao !=5:
    print('Escolha:\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos Números\n[5]Sair do progama')
    opcao = int(input())
    if opcao >5 and opcao <=0:
        print('Opção Inválida!')
    if opcao ==1:
        print(n1+n2)
    if opcao ==2:
        print(n1*n2)
    if opcao ==3:
        print(max(n1,n2))
    if opcao ==4:
        n1 = int(input('Digite um valor:\n'))
        n2 = int(input('Digite outro valor:\n'))
print('Obrigado por usar o progama!')