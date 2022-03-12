""" Exercício Python 075:

Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.

No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))

# tbm poderia ser feito colocando os 4 input dentro da tupla direto
tupla = n1, n2, n3, n4
print(f'Você digitou os números: {tupla}')
print('')

# quantas vezes o número 9 aparece
print(f'O valor 9 apareceu um total de {tupla.count(9)} vezes;')

# posição do primeiro número 3
if 3 in tupla:
    print(f'O primeiro valor 3 aparece na {tupla.index(3)+1}ª posição;')
else:
    print('O valor 3 não foi digitado em nenhuma posição;')

# valores que são pares
print(f'Os valores pares digitados foram: ', end='')
'''
# jeito que eu fiz (funciona pórem gasta mais linhas)
print('Os valores pares digitados foram ', end='')
if n1 % 2 == 0:
    print(n1, end=' ')
if n2 % 2 == 0:
    print(n2, end=' ')
if n3 % 2 == 0:
    print(n3, end=' ')
if n4 % 2 == 0:
    print(n4)'''
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
