"""Exercício Python 58:

Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint
from time import sleep
computador = randint(0, 10)

print(computador)

print('\033[36m-=\033[m'*26)
print('{:^67}'.format('\033[36m▸\033[m T E N T E   A D I V I N H A R \033[36m◂\033[m'))
print('\033[36m-=\033[m'*26)
print('')

print('Vou pensar em um número...')
jogador = int(input('\033[36m▸\033[m Em que número pensei? '))

print('')
print('\033[36mPROCESSANDO...\033[m')
sleep(1)
print('')

tentativas = 0

while jogador != computador:
    # menos
    if jogador < computador:
        print('Você errou \033[36m:/\033[m  \n'
              'Vou te dar mais uma chance, tente um número maior...')
        jogador = int(input('\033[36m▸\033[m Em que número pensei? '))
        tentativas += 1
        print('')
        print('\033[36mPROCESSANDO...\033[m')
        sleep(1)
        print('')

    # mais
    elif jogador > computador:
        print('Você errou \033[36m:/\033[m  \n'
              'Vou te dar mais uma chance, tente um número menor...')
        jogador = int(input('\033[36m▸\033[m Em que número pensei? '))
        tentativas += 1
        print('')
        print('\033[36mPROCESSANDO...\033[m')
        sleep(1)
        print('')

if jogador == computador:
    print('PARABÉNS \033[36m:D\033[m \n'
          'VOCÊ ACERTOU!!!')
    tentativas += 1
    print('')

    print('Você precisou de \033[36m{}\033[m tentativas para acertar.'.format(tentativas))
    print('\033[36m-=\033[m' * 26)
