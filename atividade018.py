import math

a = float(input('Digite o ângulo: '))
print('')

r = math.radians(a)

s = math.sin(r)
print('Seno: {:.3f}'.format(s))

c = math.cos(r)
print('Cosseno: {:.3f}'.format(c))

t = math.tan(r)
print('Tangente: {:.3f}'.format(t))
