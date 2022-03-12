# 1574

n = int(input('Digite um número de 0 a 9999: '))
print('O número que você escolheu foi {}!'.format(n))
print('')
u = n // 1 % 10
d = n // 10 % 10            # então ta bom
c = n // 100 % 10
m = n // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
