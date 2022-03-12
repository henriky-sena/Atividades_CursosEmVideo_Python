print('\033[33mꕤ\033[m \033[35mꕤ\033[m '*8)
n = str(input('Olá! Por gentileza, digite seu nome completo: ')).strip()
print('')
nome = n.split()

print('O seu primeiro nome é \033[35m{}\033[m;'.format(nome[0]))
print('E seu último nome é \033[35m{}\033[m.'.format(nome[len(nome) - 1]))
print('')

print('\033[33mAté breve\033[m \033[33m{}!\033[m'.format(nome[0] + ' ' + nome[len(nome) - 1]))
print('\033[35mꕤ\033[m \033[33mꕤ\033[m '*8)
