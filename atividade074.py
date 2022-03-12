"""Exercício Python 074:

Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também,
indique o menor e o maior valor que estão na tupla."""


from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('Os valores sorteados foram: ', end='')

# imprime os valores bonitinhos, sem parenteses ou virgulas
for n in numeros:
    print(f'{n} ', end='')

print('\n')     # pula a última linha que seria puxada pelo (end='')

print(f'O menor número sorteado foi {min(numeros)}')    # min() - exibe o menor valor em ()
print(f'O maior número sorteado foi {max(numeros)}')    # max() - exibe o maior valor em ()
