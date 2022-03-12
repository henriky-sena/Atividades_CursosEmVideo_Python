"""Exercício Python 099:

Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""

from time import sleep

def maior(* numero):                        # pelo que entendi:
    contador = 0
    m = 0                                   # todo o comando 'importante 'fica no def (nao sei pq ficou dessa cor fdkjhkj)
    print('\nAnalisando os valores...')     # e o que fica no 'PROGRAMA PRINCIPAL' é apenas as referências que os defs usam
    for n in numero:
        print(f'{n} ', end='')
        sleep(0.3)
        if contador == 1 or n > m:
            m = n
        contador += 1
    print(f'- Foram informados {contador} valores;')
    print(f'> O maior valor foi {m}.')


# PROGRAMA PRINCIPAL
maior(6, 8, 3, 4, 7, 11)
maior(4, 7, 8)
maior(1, 2)
maior(6)
maior()
