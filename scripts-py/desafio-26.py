frase = input('Digite um frase:\n')
primeira = frase.strip().find('A')
ultima = frase.strip().upper().rfind('A')
print('A letra "A" aparece {} vezes'.format(frase.upper().strip().count("A")))
print('A letra "A" aparece pela primeira vez na posição {}'.format(primeira+1))
print('A letra "A" aparece pela ultima vez na posição {}'.format(ultima+1))
