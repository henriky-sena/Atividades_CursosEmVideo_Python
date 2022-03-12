"""Exercício Python 069:

Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.

No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""

print('\033[31m-=\033[m'*21)
print('{:^41}'.format('CADASTRO DE PESSOAS'))
print('\033[31m-=\033[m'*21)

contidade = contsexo = contmulher20 = contpessoas = 0

while True:
    idade = int(input('Idade: '))

    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while 'M' != sexo != 'F':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    op = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while 'S' != op != 'N':
        op = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    print('\033[31m-=\033[m'*21)

    if idade > 18:
        contidade += 1

    if sexo == 'M':
        contsexo += 1

    if sexo == 'F' and idade < 20:
        contmulher20 += 1

    contpessoas += 1

    if op == 'N':
        break

print(f'Das {contpessoas} pessoas cadastradas:')
print(f'- {contidade} pessoas tem mais de 18 anos;')
print(f'- {contsexo} homens foram cadastrados;')
print(f'- {contmulher20} mulheres tem menos de 20 anos.')
print('\033[31m-=\033[m'*21)
