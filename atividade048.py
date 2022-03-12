s = 0
c = 0
for n in range(1, 501):
    if n % 2 == 1:
        if n % 3 == 0:
            s += n
            c += 1
print('A soma dos {} solicitados é igual a {}.'.format(c, s))
