"""Exercício Python 078:

Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. """

print('=='*26)
lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor na posição {c}: ')))

print('=='*26)

print(f'Você digitou os valores {lista}')
print('')

# para encontrar todos os maiores valores
print(f'O maior valor digitado foi {(max(lista))} na posição ', end='')
for posicao, valor in enumerate(lista):
    if valor == max(lista):
        print(f'{posicao}... ', end='')
print('')

# para encontrar todos os menores valores
print(f'O menor valor digitado foi {min(lista)} na posição ', end='')
for posicao, valor in enumerate(lista):
    if valor == min(lista):
        print(f'{posicao}...', end='')
# podemos usar print() assim, serve para o ultimo end='' não 'puxar' mais do que deve'
print()

print('=='*26)
