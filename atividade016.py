import math

n = float(input('Digite um número real: '))
print('A parte inteira de {} é {}'.format(n, math.trunc(n)))

# ambas funcionam :D

n = float(input('Digite um valor real: '))
print('A parte inteira de {} é {}'.format(n, int(n)))
