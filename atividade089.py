"""Exercício Python 089:

Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.

No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individualmente."""

from time import sleep

ficha_do_aluno = []

while True:
    print('=' * 30)
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    ficha_do_aluno.append([nome, [nota1, nota2], media])

    op = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while 'S' != op != 'N':
        op = str(input('RESPOSTA INVÁLIDA. Deseja continuar? [S/N]: ')).strip().upper()[0]

    if op == 'N':
        break

# tabela
print('=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')

# exibir dados
for i, a in enumerate(ficha_do_aluno):
        print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('='*45)
    escolha = int(input('Mostrar notas de qual aluno? [999 finaliza]: '))
    if escolha == 999:
        print('Finalizando...')
        sleep(1)
        break
    if escolha <= len(ficha_do_aluno):
        print(f'Notas de {ficha_do_aluno[escolha][0]} foram: {ficha_do_aluno[escolha][1]}')

print()
print('Obrigado por utilizar o programa :)')
print('=' * 45)

# :)
