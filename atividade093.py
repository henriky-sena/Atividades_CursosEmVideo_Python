"""Exercício Python 093:

Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""

jogador = dict()
gols = []

jogador['nome'] = str(input('NOME: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))


for p in range(0, partidas):
    gols.append(int(input(f'Quantos gols {jogador["nome"]} fez na {p+1}ª partida ? ')))

jogador['gols'] = gols[:]

# para somar a quantidade de gols dentro da lista:
'''
jogador['total'] = 0
for g in gols:
    jogador['total'] += g
'''

# ou assim tbm:
jogador['total'] = sum(gols)


# é possível imprimir os valores de 3 formas:

# 1.
print('==' * 25)
print(jogador)
print('==' * 25)


# 2.
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('==' * 25)


# 3.
print(f'O jogador {jogador["nome"]} jogou {len(gols)} partidas:')

for i, v in enumerate(jogador['gols']):         # é possível fazer enumerate de uma lista dentro do dict
    print(f' > Na {i+1}ª partida fez {v} gols.')

print(f'Foi um total de {jogador["total"]} gols!')
print('==' * 25)

# :)
