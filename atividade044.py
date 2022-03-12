print('\033[32m△▽\033[m'*25)
print('{:^50}'.format('LOJAS SAMAMBAIA FELIZ'))
print('\033[32m△▽\033[m'*25)

print('')

v = float(input('Insira o valor do produto: R$ '))
print('')

print('Opções de pagamento:')
print('\033[32m▹\033[m [ 1 ] à vista em dinheiro/ cheque: (10% de desconto)')
print('\033[32m▹\033[m [ 2 ] à vista no cartão: (5% de desconto)')
print('\033[32m▹\033[m [ 3 ] x2 no cartão: (preço normal)')
print('\033[32m▹\033[m [ 4 ] x3 ou mais no cartão: (20% de juros)')
print('')

o = int(input('Digite a opção desejada: '))

# cálculo [ 1 ]:
t1 = v - (v * (10 / 100))

# cálculo [ 2 ]:
t2 = v - (v * (5 / 100))

# cálculo [ 3 ]:
t3 = v
vp1 = v / 3

# cálculo [ 4 ]:
t4 = v + (v * (20 / 100))

if o == 1:
    print('O valor total será de R$ {:.2f}'.format(t1))
elif o == 2:
    print('O valor total será de R$ {:.2f}'.format(t2))
elif o == 3:
    print('O valor total será de R$ {:.2f}'.format(t3))
    print('Com parcelas de R$ {:.2f}'.format(vp1))
elif o == 4:
    p = int(input('Em quantas vezes gostaria de pagar? '))
    vp2 = t4 / p
    print('O valor total será de R$ {:.2f}'.format(t4))
    print('Sua compra será parcela em x{} de R$ {:.2f}'.format(p, vp2))
else:
    print('Digite uma opção válida.')

print('')

print('\033[32mObrigado por sua escolha e tenha um ótimo dia! :)\033[m')
