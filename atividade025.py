n = str(input('Digite um nome: ')).strip()      # é sempre bom colocar o .strip()

p = n.upper()
s = 'SILVA' in p

print('No nome {}, possui o nome Silva? {}'.format(n, s))

# Resolução Guanabara de apenas 2 linhas:
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
