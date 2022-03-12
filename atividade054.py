"""Exercício Python 54:

Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

from datetime import date
a = date.today().year

s1 = 0
s2 = 0

for c in range(1, 8):
    n = int(input('Ano de nascimento da {}ª pessoa: '.format(c)))
    i = a - n
    if i >= 21:
        s1 = s1 + 1
    else:
        s2 = s2 + 1
print('Ao todo, {} pessoas são maiores de idade.'.format(s1))
print('E {} pessoas são menores de idade.'.format(s2))

# para lembrar:
'''QUANDO VC NAO CONSEGUIR FAZER DE UM JEITO FAÇA DE OUTRO, MAS FAÇA!!!

n1 = int(input('Digite a data de nascimento: '))
n2 = int(input('Digite a data de nascimento: '))
n3 = int(input('Digite a data de nascimento: '))
n4 = int(input('Digite a data de nascimento: '))
n5 = int(input('Digite a data de nascimento: '))
n6 = int(input('Digite a data de nascimento: '))
n7 = int(input('Digite a data de nascimento: '))

if a - n1 >= 18:
    print('Quem nasceu em {} tem {} anos; já atigiu a maioridade.'.format(n1, a - n1))
elif a - n1 < 18:
    print('Quem nasceu em {} tem {} anos; ainda não atingiu a maioridade.'.format(n1, a - n1))

if a - n2 >= 18:
    print('Quem nasceu em {} tem {} anos; já atigiu a maioridade.'.format(n2, a - n2))
elif a - n2 < 18:
    print('Quem nasceu em {} tem {} anos; ainda não atingiu a maioridade.'.format(n2, a - n2))

if a - n3 >= 18:
    print('Quem nasceu em {} tem {} anos; já atigiu a maioridade.'.format(n3, a - n3))
elif a - n3 < 18:
    print('Quem nasceu em {} tem {} anos; ainda não atingiu a maioridade.'.format(n3, a - n3))

if a - n4 >= 18:
    print('Quem nasceu em {} tem {} anos; já atigiu a maioridade.'.format(n4, a - n4))
elif a - n4 < 18:
    print('Quem nasceu em {} tem {} anos; ainda não atingiu a maioridade.'.format(n4, a - n4))

if a - n5 >= 18:
    print('Quem nasceu em {} tem {} anos; já atigiu a maioridade.'.format(n5, a - n5))
elif a - n5 < 18:
    print('Quem nasceu em {} tem {} anos; ainda não atingiu a maioridade.'.format(n5, a - n5))

if a - n6 >= 18:
    print('Quem nasceu em {} tem {} anos; já atigiu a maioridade.'.format(n6, a - n6))
elif a - n6 < 18:
    print('Quem nasceu em {} tem {} anos; ainda não atingiu a maioridade.'.format(n6, a - n6))

if a - n7 >= 18:
    print('Quem nasceu em {} tem {} anos; já atigiu a maioridade.'.format(n7, a - n7))
elif a - n7 < 18:
    print('Quem nasceu em {} tem {} anos; ainda não atingiu a maioridade.'.format(n7, a - n7))'''
