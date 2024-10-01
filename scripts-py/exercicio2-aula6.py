n = input('Digite algo:\n')
print('O tipo primitivo é {}'.format(type(n)))

print('{} só tem espaços? {}'.format(n,n.isspace()))
print('{} é alphanúmerico? {}'.format(n,n.isalpha()))
print('{} é númerico? {}'.format(n,n.isnumeric()))
print('{} só tem maisculo? {}'.format(n,n.isupper()))
print('{} só têm minusculo? {}'.format(n,n.islower()))
print('{} está capitalizada? {}'.format(n,n.istitle()))