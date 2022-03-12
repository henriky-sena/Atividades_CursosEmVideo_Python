"""Exercício Python 077:

Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = 'banana', 'ameixa', 'abacate', 'beringela'

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()}, temos: ', end='')

    # embora são tuplas, as palavras dentro dela são listas
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
