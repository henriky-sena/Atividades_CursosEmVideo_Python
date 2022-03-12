# apresentações - o shuffle <3
from random import shuffle                              # importar processador dos dados

n1 = str(input('Digite o nome do aluno: '))
n2 = str(input('Digite o nome do aluno: '))             # recebe os dados
n3 = str(input('Digite o nome do aluno: '))
n4 = str(input('Digite o nome do aluno: '))

lista = [n1, n2, n3, n4]                                # armazena esses dados

shuffle(lista)                                          # processar os dados
print('A ordem de apresentação será: ')
print(lista)                                            # exibir os dados
