print('-='*30)
p = float(input('Digite o preço do produto: '))
d = int(input('Quanto será o desconto em porcentagem? (apenas números): '))
print('')

vd = p * (d/100)            # valor desconto
vf = p - vd                 # valor final

print('O preço R${:.2f}, com {}% de desconto, é reduzido para R${:.2f}'.format(p, d, vf))
print('Você economizará R${:.2f}!'.format(vd))
print('-='*30)
