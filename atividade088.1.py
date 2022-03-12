"""Exercício Python 088:

Faça um programa que ajude um jogador da MEGA SENA a criar palpites.

O programa vai perguntar quantos jogos serão gerados,
sorteando 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint
from time import sleep

print('='*40)
print('{:^41}'.format('MEGA SENA'))
print('='*40)

quant = int(input('Quantos palpites deseja sortear? '))
print()

print('SORTEANDO... ')
for c in range(0, quant):

    lista = []
    cont = 0

    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break

    lista.sort()

    sleep(0.7)
    print(f'▹ {c+1}º JOGO: {lista}')

print()
print('=============== BOA SORTE ===============')
