"""Exercício Python 086:

Crie um programa que declare uma matriz de dimensão 3x3, preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela, com a formatação correta."""

# RESOLUÇÃO GUANABARA
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# a parte dos 'for' é para o programa 'achar o caminho' na hora de inserir os valores
for linha in range(0, 3):       # [0 0 0] [1 1 1] [2 2 2]
    for coluna in range(0, 3):      # [0 1 2] [0 1 2] [0 1 2]

        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}][{coluna}]: '))

print('=' * 31)

# para mostrar bonitinho, fazemos (aparentemente) o inverso
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f' [ {matriz[linha][coluna]:^5} ]', end='')
    print()

print('=' * 31)
