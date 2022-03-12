import random

n1 = str(input('Digite o nome do aluno: '))
n2 = str(input('Digite o nome do aluno: '))
n3 = str(input('Digite o nome do aluno: '))
n4 = str(input('Digite o nome do aluno: '))

lista = [n1, n2, n3, n4]        # listas ficam entre [conchetes]

escolhido = random.choice(lista)
print('O aluno escolhido foi {}!'.format(escolhido))
