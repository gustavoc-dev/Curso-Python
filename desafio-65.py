n = 0
opcao = 0
soma = 0
count = 0
maior = 0
menor = 0
while opcao !=2:
    opcao = int(input('Oque você quer fazer?\n[1]Digitar um número\n[2]Sair\n'))
    if opcao <1 or opcao >2:
        print('Opção Inválida!')
        opcao = int(input('Deseja continuar?\n[1]Sim\n[2]Não'))
    if opcao ==1:
        n = int(input('Digite um número\n'))
        count +=1
        soma+=n
        if n > maior:
            maior=n
            menor=maior
        if n <menor:
            menor=n
print('Média dos valores: {:.2f}.\nO maior numero digitado foi {}\nO menor foi {}'.format(soma/count,maior,menor))