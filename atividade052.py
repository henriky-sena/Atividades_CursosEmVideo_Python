""" Exercício Python 52:
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

numero = int(input('Digite um número: '))

total = 0

for contador in range(1, numero + 1):
    if numero % contador == 0:
        print('\033[33m', end='')

        # ou t = t + 1 -> soma quantas vezes 'numero' é divisível pelo 'contador'
        total += 1

    else:
        print('\033[31m', end='')
    print(f'{contador}', end=' ')
print(f'\n\033[mO número {numero} é divisível por \033[33m{total}\033[m números.')

if total == 2:
    print('E por isso É PRIMO.')
else:
    print('E por isso NÃO É PRIMO.')
