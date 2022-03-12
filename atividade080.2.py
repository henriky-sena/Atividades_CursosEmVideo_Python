"""Exercício Python 080:

Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()).

No final, mostre a lista ordenada na tela.
"""

lista = []

for contador in range(1, 6):
    valor = int(input(f'Digite o {contador}º valor: '))

    if contador == 1 or valor > lista[-1]:
        lista.append(valor)

    else:
        posicao = 0
        while posicao < len(lista):

            if valor < lista[posicao]:
                lista.insert(posicao, valor)

                break

            posicao += 1

print(f'Os valores digitados foram: {lista}')
