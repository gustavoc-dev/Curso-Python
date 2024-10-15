preco = float(input('Qual o valor do produto?\n'))
pagamento = int(input('Qual é a forma de pagamento?\n1-Dinheiro/Cheque\n2-Cartão\n3-2x no Cartão\n4-3x no Cartão\n'))

if pagamento==1:
    print('Você ganhou 10 por cento de desconto, de {} você pagará {:.2f}'.format(preco,preco - (preco*0.10)))
elif pagamento==2:
     print('Você ganhou 5 por cento de desconto, de {} você pagará {:.2f}'.format(preco,preco - (preco*0.05)))
elif pagamento == 3:
     print('Preço Normal: {}'.format(preco))
elif pagamento ==4:
      print('Você pagara 20 por cento de juros, de {} você pagará {:.2f}'.format(preco,preco + (preco*0.20)))