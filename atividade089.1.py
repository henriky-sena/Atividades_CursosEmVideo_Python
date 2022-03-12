"""Exercício Python 089:

Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.

No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individualmente."""

ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], media])

    op = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while 'S' != op != 'N':
        op = str(input('RESPOSTA INVÁLIDA. Deseja continuar? [S/N]: ')).strip().upper()[0]

    if op == 'N':
        break

print()
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('=' * 26)

# exibir os dados
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('=' * 35)
    opc = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:       # não entendi desse - 1, sem ele o programa funiona igual :/
        print(f'Notas de {ficha[opc][0]}: {ficha[opc][1]}')

print()
print('Obrigado por usar o programa :)')
