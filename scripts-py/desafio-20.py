#ler 4 alunos e selecionar a ordem de apresentação de um trabalho

import random

aluno1 = input('Digite o nome do primeiro aluno(a):\n')
aluno2 = input('Digite o nome do segundo aluno(a):\n')
aluno3 = input('Digite o nome do terceiro aluno(a):\n')
aluno4 = input('Digite o nome do quarto aluno(a):\n')

listaAlunos = [aluno1,aluno2,aluno3,aluno4]

print('O professor escolheu a seguinte ordem: {}'.format(random.sample(listaAlunos, k= 4)))