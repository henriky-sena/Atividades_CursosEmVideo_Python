"""Exercício Python 071:

Crie um programa que simule o funcionamento de um caixa eletrônico.

No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro);
o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

# RESOLUÇÂO GUANABARA

valor = int(input('Quanto gostaria de sacar? R$ '))
print('')
cedula = 50
total = valor

contador_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        contador_cedula += 1
    else:
        if cedula > 0:
            print(f'Total de {contador_cedula} de R$ {cedula:.2f}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        contador_cedula = 0
        if total == 0:
            break

print('')
print('Tenha um ótimo dia !')
