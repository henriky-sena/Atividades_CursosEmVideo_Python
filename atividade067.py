"""Exercício Python 067:

Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário.

O programa será interrompido quando o número solicitado for negativo. """


while True:
    numero = int(input('Digite um número para ver sua tabuada: '))
    print('-='*20)

    # stop
    if numero < 0:
        break

    # tabuada
    for contador in range(1, 11):
        resultado = contador * numero
        print(f'{numero} * {contador:2} = {resultado}')

    print('-=' * 20)
print('Programa finalizado. Volte sempre :)')
