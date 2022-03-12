"""Exercício Python 060:

Faça um programa que leia um número qualquer e mostre o seu fatorial.

Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120"""

# from math impor factorial
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))       # :)
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))


# while
n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
f = 1       # multiplicação: quando precisar somar qualquer coisa e deixar a soma limpa, comece com 1, nunca com 0

print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')        # formatando cálculos
    f *= c
    c -= 1                                      # o 'c' é: cada vez que ele passar pelo 'c' ele soma mais um
print('{}'.format(f))


# for
n = int(input('Digite um número para calcular o seu fatorial: '))
f = 1       # multiplicação: quando precisar somar qualquer coisa e deixar a soma limpa, comece com 1, nunca com 0

print('Calculando {}! = '.format(n), end='')
for a in range(n, 0, -1):
    print(a, end='')
    print(' x ' if a > 1 else ' = ', end='')
    f *= a
print('{}'.format(f))
