"""Exercício Python 099:

Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""

from time import sleep

def maior(* numeros):
    contador = 0
    m = 0

    print(f'\nAnalisando os valores...')

    for n in numeros:
        contador += 1
        sleep(0.3)
        print(f'{n} ', end='')

        if contador == 1 or n > m:
            m = n
    print(f'- Foram informados {contador} valores')
    print(f'> O maior valor infromado foi {m};')


maior(6, 8, 3, 4, 7, 11)
maior(4, 7, 8)
maior(1, 2)
maior(6)
maior()

# 1ª tentativa:
'''
# claramente não é o método mais adequado,
# mas fiquei feliz que depois de muito esforço
# cheguei no resultado que tinha em mente :)

from time import sleep

def bonitinho():
    print('-=' * 25)


def maior():
    if len(lista) > 0:
        print(f'> O maior valor informado foi {max(lista)}')

    else:
        print('> Foram informados 0 valores, portanto, o maior valor é 0')

def mostrar_lista():
    bonitinho()
    print('VALORES INFORMADOS: ', end='')
    for n in lista:
        print(f'{n} ', end='')
        sleep(0.3)
    print()
    print(f'Analisando os {len(lista)} valores informados...')
    maior()


# PROGRAMA PRINCIPAL
lista = [6, 8, 3, 4, 7, 11]
mostrar_lista()

lista = [4, 7, 8]
mostrar_lista()

lista = [1, 2]
mostrar_lista()

lista = [6]
mostrar_lista()

lista = []
mostrar_lista()
bonitinho()
'''

# :)
