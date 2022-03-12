s = float(input('Digite o salário atual: R$'))

# c1 = para salários de 1250.00, 10% de aumento
# c2 = para salários menores que 1250.00, 15 % de aumento

c1 = s + (s * 10 / 100)
c2 = s + (s * 15 / 100)

if s > 1250.00:
    print('O novo salário será de \033[32mR${:.2f}\033[m'.format(c1))
if s <= 1250.00:
    print('O novo salário será de R${:.2f}'.format(c2))
