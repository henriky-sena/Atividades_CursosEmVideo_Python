n = int(input('Digite um número: '))

if (n % 2) == 0:
    print('O numéro {} é \033[35mPAR\033[m!'.format(n))
else:
    print('O número {} é \033[35mIMPAR\033[m!'.format(n))
