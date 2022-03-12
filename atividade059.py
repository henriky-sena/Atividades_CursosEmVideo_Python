"""Exercício Python 059:

Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

O seu programa deverá realizar a operação solicitada em cada caso."""

from time import sleep

print('\033[34m-=\033[m'*30)
v1 = int(input('\033[34m▹\033[m Digite o primeiro valor: '))
v2 = int(input('\033[34m▹\033[m Digite o segundo valor: '))
print('\033[34m-=\033[m'*30)

# a gambiarra pro while não bugar
op = 0

# se op == 5 pare
while op != 5:
    print('''\033[34m▹\033[m [ 1 ] SOMAR
\033[34m▹\033[m [ 2 ] MULTIPLICAR
\033[34m▹\033[m [ 3 ] MAIOR
\033[34m▹\033[m [ 4 ] NOVOS NÚMEROS
\033[34m▹\033[m [ 5 ] SAIR DO PROGRAMA''')
    op = int(input('Digite a opção desejada: '))

    # soma
    if op == 1:
        soma = v1 + v2
        print('')
        print('A soma dos valores {} e {} é igual a {}'.format(v1, v2, soma))
        print('\033[34m-=\033[m'*30)

    # multiplicação
    elif op == 2:
        mult = v1 * v2
        print('')
        print('A multiplicação dos valores {} e {} é igual a {}'.format(v1, v2, mult))
        print('\033[34m-=\033[m'*30)

    # número maior
    elif op == 3:
        print('')
        if v1 > v2:
            print('O maior valor entre os valores digitados é {}'.format(v1))
        elif v2 > v1:
            print('O maior valor entre os valores digitados é {}'.format(v2))
        elif v1 == v2:
            print('Os valores digitados são iguais')
        print('\033[34m-=\033[m'*30)

    # novos números
    elif op == 4:
        print('\033[34m-=\033[m' * 30)
        print('\033[34m▹\033[m NOVOS VALORES \033[34m◃\033[m')
        v1 = int(input('Digite o primeiro valor: '))
        v2 = int(input('Digite o segundo valor: '))
        print('\033[34m-=\033[m'*30)

    elif op == 5:
        print('Finalizando...')

    else:
        print('Opção inválida, tende novamente.')
        print('')
        print('\033[34m-=\033[m' * 30)
    sleep(2)

print('')
print('Até logo :)')

print('\033[34m-=\033[m'*30)
