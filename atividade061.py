"""Exercício Python 060:

Melhore o exercício 051 utilizando o while"""

'''Progressão aritmétrica é apenas uma contagem usando a razão como "pausas".
não é tão dificil como parece'''

# resolução Guanabara
print('Gerador de PA')
print('-='*20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

termo = primeiro
contador = 1

while contador <= 10:
    print('{} ➞ '.format(termo), end='')
    termo += razao
    contador += 1
print('FIM')
