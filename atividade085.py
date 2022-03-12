""" Exercício Python 085:

Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os numa lista única que mantenha separados os valores pares e ímpares.

No final, mostre os valores pares e ímpares em ordem crescente."""

lista_geral = [[], [], []]

print('\033[36m△▽\033[m'*25)
print('{:^51}'.format(' PAR E IMPAR '))
print('\033[36m△▽\033[m'*25)

for contador in range(1, 8):
    numero = int(input(f'\033[36m▹\033[m Digite o {contador}º valor: '))
    lista_geral[0].append(numero)

for valor in lista_geral[0]:
    if valor % 2 == 0:
        lista_geral[1].append(valor)    # lista par

    else:
        lista_geral[2].append(valor)    # lista impar

lista_geral[0].sort()
lista_geral[1].sort()
lista_geral[2].sort()

print()

print(f'\033[36m_\033[mOs valores inseridos foram: {lista_geral[0]}')
print(f'\033[36m_\033[mOs valores pares foram: {lista_geral[1]}')
print(f'\033[36m_\033[mOs valores impares foram: {lista_geral[2]}')
print('\033[36m△▽\033[m'*25)
