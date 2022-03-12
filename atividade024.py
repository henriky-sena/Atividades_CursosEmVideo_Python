c = str(input('Digite o nome da sua cidade: ')).strip()

s = c.title()
s.split()
s = 'Santo' in s[0:5]

print('A cidade {}, começa com Santo? {}'.format(c, s))

# resolução do Guanabara de apenas 2 linhas:
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
