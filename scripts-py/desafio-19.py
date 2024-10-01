#ler 4 alunos e selecionar apenas 1

import random

aluno1 = input('Digite o nome do primeiro aluno(a):\n')
aluno2 = input('Digite o nome do segundo aluno(a):\n')
aluno3 = input('Digite o nome do terceiro aluno(a):\n')
aluno4 = input('Digite o nome do quarto aluno(a):\n')

listaAlunos = [aluno1,aluno2,aluno3,aluno4]

choice = random.choice(listaAlunos)

print('O professor escolheu o aluno(a) {}'.format(choice))