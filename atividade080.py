"""Exercício Python 080:

Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()).

No final, mostre a lista ordenada na tela.
"""

lista = []

for contador in range(0, 5):
    valor = int(input(f'Digite o valor: '))

    # se ele for o primeiro valor:
    # ele será o maior valor e então, será jogado para o final da lista;
    if contador == 0:
        lista.append(valor)
        print('Valor adicionado ao final da lista')

    # se ele não for o primeiro e for maior que o valor anterior:
    # o maior valor é jogado para o final da lista
    elif valor > lista[-1]:
        lista.append(valor)
        print('Valor adicionado ao final da lista;')

    # menor valor:
    else:
        # é necessário varrer a lista inteira:
        posicao = 0
        while posicao < len(lista):

            # se o valor inserido for menor que os outros valores:
            if valor <= lista[posicao]:

                # substitui a posição do menor valor.
                # fazendo com que o antigo menor valor se desloque para o lado direito
                lista.insert(posicao, valor)
                print(f'Valor adicionado a {posicao}ª posição;')

                # como não é mais necessário modificações, pare.
                break

            # a cada posição percorrida, posição recebe +1
            posicao += 1

print(f'Os valores digitados em ordem crescente foram: {lista}')
