"""Exercício Python 084:

Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.

No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

pessoas = []
dados = []
maior_peso = 0
menor_peso = 0

while True:

    print('{:-^31}'.format(' CADASTRO DE PESSOAS '))
    nome = str(input('NOME: '))             # nome = dados[0]
    peso = float(input('PESO [Kg]: '))      # peso = dados[1]

    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])

    # maior e menor peso
    if len(pessoas) == 1:
        maior_peso = dados[1]
        menor_peso = dados[1]
    else:
        # maior
        if dados[1] > maior_peso:
            maior_peso = dados[1]

        # menor
        if dados[1] < menor_peso:
            menor_peso = dados[1]

    dados.clear()

    op = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while 'S' != op != 'N':
        op = str(input('RESPOSTA INVÁLIDA. Deseja continuar? [S/N]: ')).strip().upper()[0]

    if op == 'N':
        break

print('-=' * 20)
print(f'Foram cadastradas {len(pessoas)} pessoas:')

# nome(s) do maior peso
print(f'- O maior peso foi {maior_peso} Kg. Peso de:', end=' ')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}]', end=' ')
print()

# nome(s) do menor peso
print(f'- O menor peso foi {menor_peso} Kg. Peso de:', end=' ')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}]', end=' ')
print()
