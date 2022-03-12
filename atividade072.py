"""Exercício Python 072:

Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso."""

numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
          'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
          'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    print('-=' * 20)
    usuario = int(input('Digite um número de 0 a 20: '))

    while usuario < 0 or usuario > 20:
        usuario = int(input('Tente novamente. Digite um número de 0 a 20: '))

    print('')
    print(f'Você digitou o número {numero[usuario]}.')
    print('')
    op = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while 'S' != op != 'N':
        print('Digite uma opção válida!')
        print('')
        op = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if op == 'N':
        break

print('-='*20)
print('Programa encerrado! Volte sempre :)')
print('-='*20)
