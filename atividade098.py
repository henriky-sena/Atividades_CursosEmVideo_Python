"""Exercício Python 098:

Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo.

Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""

from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:       # o ideal é testar os dados logo no início do programa
        passo *= -1

    if passo == 0:      # para que não dê problema no meio dele
        passo = 1
    print(f'> Contagem de {inicio} até {fim}, de {passo} em {passo}:')
    sleep(1.5)


    if inicio < fim:
        c = inicio
        while c <= fim:
            sleep(0.3)
            print(f'{c} ', end='')
            c += passo
        print('FIM!')

    elif inicio > fim:
        c = inicio
        while c >= fim:
            sleep(0.3)
            print(f'{c} ', end='')
            c -= passo
        print('FIM!')
    print()


# a)
contador(1, 10, 1)

# b)
contador(10, 0, 2)

# c)
print('> Agora sua vez! personalize a contagem:')
i = int(input('   - Início: '))
f = int(input('   - Final: '))
p = int(input('   - Passo: '))

contador(i, f, p)
