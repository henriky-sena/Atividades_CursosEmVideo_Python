""" Entendi o conceito hehehe  :) """

#  0 –  1 –  1 – 2 – 3 – 5 – 8
# t1 - t2 - t3

t = int(input('Quantos termos você quer mostrar? '))

t1 = 0
t2 = 1
t3 = t1 + t2

print('{} ⇀ {}'. format(t1, t2), end='')
contador = 3

while contador <= t:
    t3 = t1 + t2
    print(' ⇀ {}'.format(t3), end='')

    t1 = t2
    t2 = t3

    contador += 1
print(' ⇀ FIM')
