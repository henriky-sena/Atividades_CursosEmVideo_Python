c = float(input('Insira o valor disponível em reais: R$'))

# US$ 1 = R$ 5.53     -    13/01/2022

d = 5.53
q = c/d

print('')
print('-$-'*11)
print('Você poderá comprar: US${:.2f} dólares'.format(q))
print('-$-'*11)
print('')

# não sei se ta certo mas acho que sim
