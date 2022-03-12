"""Exercício Python 079:

Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.

No final, serão exibidos todos os valores únicos digitados, em ordem crescente. """

lista = []
while True:
    # cadastra o valor na lista
    n = int(input('Cadastre um valor: '))
    lista.append(n)

    # se o valor for repetido, exclua o valor e informe 'valor repetido'
    while lista.count(n) > 1:
        print('VALOR REPETIDO')
        lista.remove(n)
        n = int(input('Cadastre um novo valor: '))
        lista.append(n)

    # deseja continuar?
    op = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while 'S' != op != 'N':
        op = str(input('RESPOSTA INVÁLIDA. Deseja continuar? [S/N]: ')).strip().upper()[0]

    # se a resposta do usuário for 'N', pare
    if op == 'N':
        break

# saída final
print('==' * 30)
lista.sort()
print(f'Você digitou os valores {lista}')
