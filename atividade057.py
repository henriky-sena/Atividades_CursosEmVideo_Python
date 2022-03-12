"""Exercício Python 57:

Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
print('')

while 'M' != sexo != 'F':
    print('Respota inválida')
    print('')

    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
if sexo == 'M':
    print('Olá, rapaz!')
elif sexo == 'F':
    print('Olá, senhorita!')
