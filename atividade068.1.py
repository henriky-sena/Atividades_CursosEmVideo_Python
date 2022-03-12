"""Exercício Python 68:

Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder;
mostrando o total de vitórias consecutivas que ele conquistou
no final do jogo."""

# resolução Guanabara - correta*

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(1, 10)
    total = jogador + computador

    # essa parte é importante
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}, total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')

    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU !')
            v += 1
        else:
            print('Você PERDEU !')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU !')
            v += 1
        else:
            print('Você PERDEU !')
            break

    print('Vamos jogar novamente...')
print('GAME OVER!')
print(f'Você venceu {v} vezes.')
