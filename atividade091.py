"""Exercício Python 091:

Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado."""

from random import randint
from operator import itemgetter

jogo = {'jogador_1': randint(1, 6),
        'jogador_2': randint(1, 6),
        'jogador_3': randint(1, 6),
        'jogador_4': randint(1, 6)}

ranking = []

print('🎲 VALORES SORTEADOS 🎲')
for k, v in jogo.items():
    print(f'- {k} tirou {v}')


# para deixar um dicionário em ordem importamos o itemgetter()
# e para finalizar o ranking, fazemos o reverse dele
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)


print()
print('🏆 RANKING FINAL 🏆')
for i, v in enumerate(ranking):
    print(f'- {i+1}º LUGAR: {v[0]} com {v[1]}')

