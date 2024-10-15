n = int(input('Escolha o número para converter:\n'))
option = int(input('Escolha a base de conversão:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n'))

if option != 1 and option!= 2 and option != 3:
    print('Opção inválida')
elif option == 1:
    print('O número {} em binário é {}'.format(n,bin(n)))
elif option == 2:
     print('O número {} em octal é {}'.format(n,oct(n)))
elif option == 3:
     print('O número {} em hexadecimal é {}'.format(n,hex(n)))