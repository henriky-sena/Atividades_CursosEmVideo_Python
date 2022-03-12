"""Exercício Python 076:

Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular."""

            # PAR       #IMPAR
cardapio = ('Biscoito', 4.50,
            'Coxinha', 2.50,
            'X-Burguer', 6.50,
            'X-Bacon', 7.50,
            'Refrigerante', 4.99)

print('=' * 40)
print(f'{"LANCHONETE FELIZ":^40}')
print('=' * 40)

# menu
for posi in range(0, len(cardapio)):

    # PAR = aqui produtos estão em posições pares
    if posi % 2 == 0:
        print(f'{cardapio[posi]:.<30}', end='')

    # IMPAR = aqui preços estão em pocições impares
    else:
        print(f'R$ {cardapio[posi]:>4.2f}')

print('=' * 40)
