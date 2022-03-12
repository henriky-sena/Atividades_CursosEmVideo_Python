"""Embora tenha entendido o conceito, prefido essa forma de fazer, é mais 'objetiva'"""

print('=='*20)
print('{:^40}'.format('BANCO AUVORECER'))
print('=='*20)

valor = int(input('Quando gostaria de sacar? R$ '))

print('')

cont_50 = 0
cont_20 = 0
cont_10 = 0
cont_1 = 0

while True:                         # EXPLICAÇÃO:
    while valor - 50 >= 0:          # enquanto valor menos nota for maior ou igual a 0:
        valor -= 50                        # faça valor menos nota (no caso 50)
        cont_50 += 1
    while valor - 20 >= 0:          # após ele sair do looping de 50, ele entra no de 20:
        valor -= 20                        # que é a mesma coisa até ele sair novamente
        cont_20 += 1
    while valor - 10 >= 0:          # e assim por diante passando por todos os valores:
        valor -= 10
        cont_10 += 1
    while valor - 1 >= 0:
        valor = valor - 1           # quando o valor chegar a 0, ele sai do looping:
        cont_1 += 1                 # saindo do looping ele encontra o break que então
    break                           # finaliza o programa.

print('TOTAL DE CÉDULAS:')
if cont_50 > 0:
    print(f'{cont_50} notas de R$ 50.00')
if cont_20 > 0:
    print(f'{cont_20} notas de R$ 20.00')
if cont_10 > 0:
    print(f'{cont_10} notas de R$ 10.00')
if cont_1 > 0:
    print(f'{cont_1} notas de R$ 1.00')
