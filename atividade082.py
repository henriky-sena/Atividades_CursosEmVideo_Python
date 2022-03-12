"""Exercício Python 082:

Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras, que vão conter apenas os valores pares e os valores ímpares
digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas."""

lista_geral = []
lista_pares = []
lista_impares = []

while True:

    # colheita de dados
    lista_geral.append(int(input('Digite um valor: ')))
    op = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    # opção do usuário
    while 'S' != op != 'N':
        op = str(input('Resposta inválida. Deseja continuar? [S/N]: ')).strip().upper()[0]
    if op == 'N':
        break

print('-='*30)

# lista geral
print(f'Os valores inseridos foram: {lista_geral}')

# varredura para identificar se os valores são:
for valores in lista_geral:

    # pares
    if valores % 2 == 0:
        lista_pares.append(valores)

    # impares
    elif valores % 2 == 1:
        lista_impares.append(valores)

# saída final
print(f'Os números pares são {lista_pares}')
print(f'Os números impares são {lista_impares}')
print('-='*30)
