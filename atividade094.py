"""Exercício Python 094:

Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.

No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""

lista = []
pessoas = {}
mulheres = []
soma = 0

while True:
    print(' - CADASTRE UMA PESSOA - ')
    pessoas['nome'] = str(input('NOME: '))
    pessoas['idade'] = int(input('IDADE: '))
    soma += pessoas['idade']
    pessoas['sexo'] = str(input('SEXO [M/F]: ')).strip().upper()[0]
    while 'M' != pessoas['sexo'] != 'F':
        print('Por favor, Responda apenas "M" ou "F". ')
        pessoas['sexo'] = str(input('SEXO [M/F]: ')).strip().upper()[0]

    lista.append(pessoas.copy())

    if pessoas['sexo'] == 'F':
        mulheres.append(pessoas['nome'])

    op = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while 'S' != op != 'N':
        print('Por favor, Responda apenas com "S" ou "N".')
        op = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    if op == 'N':
        break
    print('='*30)

print(lista)
print('='*30)

# A)
print(f'> Foram cadastradas {len(lista)} pessoas;')
print()


# B)
media = soma / len(lista)
print(f'> A média de idade é de {media:.1f} anos;')
print()

# C)
if len(mulheres) > 0:
    print(f'> Mulheres cadastradas:')
    for m in mulheres:
        print(f'- {m}; ')
else:
    print('> Não houve mulheres cadastradas;')
print()

# D)
print('> Pessoas com idade acima da média:')
for p in lista:
    if p['idade'] >= media:
        print(f'- {p["nome"]} com {p["idade"]} anos;')

print()
print('<< PROGRAMA ENCERRADO >>')
print('='*30)

# :)
