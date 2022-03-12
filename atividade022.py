print('-='*30)
print('Olá, seja bem vindo!')
nome = str(input('Digite o seu nome completo: ')).strip()
print('')

print('Seu nome em letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas: {}'.format(nome.lower()))
print('Total de letras do seu nome: {}'.format(len(nome.replace(' ', ''))))
dividido = nome.split()
print('E por fim, quantas letras tem seu primeiro nome: {}!'.format(len(dividido[0])))

print('')

print('Até logo {}!'.format(nome))
print('-='*30)
