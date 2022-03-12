n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 < n2 and n1 < n3:
    print('O menor número é \033[36m{}\033[m'.format(n1))
if n2 < n1 and n2 < n3:
    print('O menor número é \033[36m{}\033[m'.format(n2))
if n3 < n1 and n3 < n2:
    print('O menor número é \033[36m{}\033[m'.format(n3))

if n1 > n2 and n1 > n3:
    print('O maior número é \033[36m{}\033[m'.format(n1))
if n2 > n1 and n2 > n3:
    print('O maior número é \033[36m{}\033[m'.format(n2))
if n3 > n1 and n3 > n2:
    print('O maior número é \033[36m{}\033[m'.format(n3))
print('')

# resolução Guanabara:
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print('\033[35mO menor valor é\033[m \033[32m{}\033[m'.format(menor))
print('\033[35mO maior valor é\033[m \033[32m{}\033[m'.format(maior))
