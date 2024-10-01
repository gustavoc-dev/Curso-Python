cidade = input('Digite o nome da sua cidade:\n')

cidadeSplit = cidade.strip().title().split()

if cidadeSplit[0].find('Santo') == -1:
    print('Sua cidade não começa com "Santo", Sua cidade: {}'.format(cidade))
elif cidadeSplit[0].find('Santo') == 0:
    print('Sua cidade começa com "Santo", Sua cidade: {}'.format(cidade.strip().title()))
