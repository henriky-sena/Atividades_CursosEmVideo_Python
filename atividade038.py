print('\033[34m=-\033[m'*15)

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('')

if n1 > n2:
    print('O \033[34mprimeiro\033[m valor é maior.')
elif n2 > n1:
    print('O \033[34msegundo\033[m valor é maior.')
elif n1 == n2:
    print('Não existe valor maior;')
    print('Os valores são \033[34miguais\033[m.')

print('\033[34m=-\033[m'*15)
