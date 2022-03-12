""" Exercício Python 070:

Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não.

No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. """

total = totmil = contador = menor = 0
barato = ''

while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Preço: R$ '))

    print('-='*20)

    # contador de produtos
    contador += 1

    # total da compra
    total += valor

    # produtos + mil reais
    if valor > 1000:
        totmil += 1

    # mais barato
    if contador == 1 or valor < menor:
        menor = valor
        barato = produto

    # resposta [S/N]
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while 'S' != resp != 'N':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    # stop
    if resp == 'N':
        break

# fim do programa
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'- O total da compra foi R$ {total:.2f}')
print(f'- Temos {totmil} produto(s) custando mais de R$ 1000.00 reais')
print(f'- O produto mais barato custa R$ {menor:.2f} e foi {barato}')
