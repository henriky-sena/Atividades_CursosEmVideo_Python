"""Exercício Python 100:

Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().

A primeira função vai sortear 5 números e vai colocá-los na lista
e a segunda função vai mostrar a soma entre todos os valores pares sorteados
pela função anterior."""

from random import randint
from time import sleep

lista = []
lista_pares = []

# def's ficam em cima
def sorteia():
    for c in range(0, 5):
        n = randint(1, 10)
        sleep(0.5)
        print(f'{n}', end=' ')
        lista.append(n)
    print('PRONTO!')

def soma_par():
    soma = 0
    for n in lista_pares:
        soma += n
    print(f'{soma}.')


# PROGRAMA PRINCIPAL
# (pega de referência os def's acima)
print('> Sortando os valores: ', end='')
sorteia()

for num in lista:
    if num % 2 == 0:
        lista_pares.append(num)

print(f'> Somando os valores pares em: {lista}; temos um total de ', end='')
soma_par()

# :)
