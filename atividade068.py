"""Exercício Python 68:

Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder;
mostrando o total de vitórias consecutivas que ele conquistou
no final do jogo."""

from random import randint

contador = 0

while True:
    computador = randint(0, 10)
    print('\033[36m-=\033[m'*20)
    print('{:^38}'.format('IMPAR OU PAR'))
    print('\033[36m-=\033[m'*20)

    # jogador 'joga'
    njogador = int(input('Diga um valor: '))
    opjogador = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]

    print('')

    # variáveis
    soma = njogador + computador
    resultado = soma % 2
    parimpar = ''

    # resultado: impar ou par
    if resultado == 0:
        parimpar = 'P'
    if resultado == 1:
        parimpar = 'I'

    # stop
    if opjogador != parimpar:
        break

    # jogo
    print(f'Você jogou {njogador} e o computador {computador}')

    # jogador vence
    if opjogador == 'P':
        print(f'Total de {soma}, deu PAR!')
        if resultado == 0:
            print('')
            print('VOCÊ VENCEU!!!')
    if opjogador == 'I':
        print(f'Total de {soma}, deu IMPAR!')
        if resultado == 1:
            print('')
            print('VOCÊ VENCEU!!!')

    print('Vamos jogar novamente...')

    # quantas vezes venceu
    contador += 1

    print('')

# jogador perde
print(f'GAME OVER !!!')

# saída final
print(f'Você jogou {njogador} e o computador {computador}')

# resultado: impar ou par
if resultado == 0:
    print(f'Total de {soma}, deu PAR!')
if resultado == 1:
    print(f'Total de {soma}, deu IMPAR!')

# contagem de vitórias
print('')
print(f'Você venceu um total de {contador} vezes.')
print('\033[36m-=\033[m'*20)
