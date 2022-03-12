"""Exercício Python 64:

Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag (999))."""


q = 0
s = 0

print('[Digite 999 para parar o programa]')

# se colocar o flag[999] antes do whale, quando ele for 'acionado' ele não entrará no algoritmo
n = int(input('Digite um número: '))

while n != 999:
    q = q + 1
    s = s + n
    n = int(input('Digite um número: '))
print('')

print('Foram digitados {} números;'.format(q))
print('A soma dos números foi de {}.'.format(s))
