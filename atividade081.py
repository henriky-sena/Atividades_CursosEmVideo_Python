"""Exercício Python 081:

Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

lista = []
while True:

    # opção do usário
    lista.append(int(input('Digite um número: ')))
    op = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    # caso a resposta for inválida
    while 'S' != op != 'N':
        op = str(input('RESPOSTA INVÁLIDA. Deseja continuar? [S/N]: ')).strip().upper()[0]

    # stop
    if op == 'N':
        break

print('-='*30)

print(f'Os valores inseridos foram: {lista}')
print()

# quantos valores foram inseridos
print(f'Foram inseridos {len(lista)} valores;')

# a lista em ordem decrescente
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente: {lista};')

# se o valor 5 foi digitado na lista
if 5 in lista:
    print(f'O número 5 está na lista e aparece um total de {lista.count(5)} vezes;')
else:
    print('O número 5 não está entre os valores digitados;')

print('-=' * 30)
