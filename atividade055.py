"""Exercício Python 55:

Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos."""

maior = 0
menor = 0

for pessoa in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso            # se tem apenas uma pessoa:
        menor = peso                # tanto o maior quanto o menor peso será o dela
    else:
        if peso > maior:        # se não for a primeira pessoa:
            maior = peso            # se o próximo peso for maior / menor, a variável substitue o valor anterior
        if peso < menor:            # e assim por diante
            menor = peso
print('O maior peso lido foi {} Kg.'.format(maior))
print('O menor peso lido foi {} Kg.'.format(menor))
