"""Exercício Python 087:

Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
soma_pares = 0
soma_terc = 0
maior = 0

# coordenadas da matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}][{coluna}]: '))

print('=' * 31)

# matriz bonitinha
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f' [ {matriz[linha][coluna]:^5} ]', end='')
    print()

print('=' * 31)

# soma dos valores pares
for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
            pares.append(soma_pares)
print(f'A soma dos valores pares é igual a {soma_pares};')

# soma dos valores da terceira coluna
for linha in range(2, 3):
    for coluna in range(0, 3):
        soma_terc += matriz[coluna][linha]
print(f'A soma dos valores da terceira coluna é {soma_terc};')

# o maior valor da segunda linha
for linha in range(1, 2):
    for coluna in range(0, 3):
        if matriz[linha][coluna] > maior:
            maior = matriz[linha][coluna]
print(f'O maior valor da segunda linha é {maior}.')
