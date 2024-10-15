produtoBarato = ' '
total = 0
produtoMil = 0
continuar = 1
preco =0
nome = ' '
while continuar == 1:
	ultimoProduto = preco
	nome=str(input('Qual é o nome do produto?\n'))
	preco=int(input('Qual é o preço do produto?\n'))
	
	total+=preco

	if preco >1000:
		produtoMil+=1
	
	if preco<ultimoProduto:
		produtoBarato = nome
	
	continuar = int(input('Deseja continuar?\n[1]Sim/n[2]Não\n'))
	
	if continuar ==2:
		break
		
print(f'Total: {total}, Produtos + de mil {produtoMil}, Produto + barato {produtoBarato}')