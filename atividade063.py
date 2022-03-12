"""Exercício Python 63:

Escreva um programa que leia um número N inteiro qualquer e
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8
"""

print('Sequência de Fibonacci')
termo = int(input('Quantos termos você quer mostrar: '))

t1 = 0
t2 = 1


print('')

print('{} ⇀ {}'.format(t1, t2), end='')

cont = 3

while cont <= termo:
    t3 = t1 + t2
    print(' ⇀ {}'.format(t3), end='')

    t1 = t2
    t2 = t3

    cont += 1                        # toda a vez que tive while tem que ter esse (contador += 1)

print(' ⇀ FIM')
