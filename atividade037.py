n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
o = int(input('Sua opção: '))

if o == 1:
    print('{} convertido para BINÁRIO é {}.'.format(n, bin(n)[2:]))      # 0b para binário
elif o == 2:
    print('{} convertido para OCTAL é {}.'.format(n, oct(n)[2:]))        # 0o para octal
elif o == 3:
    print('{} convertido para HEXADECIMAL é {}.'.format(n, hex(n)[2:]))  # 0x para hexadecimal
else:
    print('Opção inválida, tente novamente.')
