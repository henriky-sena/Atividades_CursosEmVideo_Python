from datetime import date
a = date.today().year

n = int(input('Digite o ano de nascimento: '))
print('')

i = a - n

print('O atleta tem {} anos.'.format(i))

if i <= 9:
    print('Classificação: MIRIM')
elif i <= 14:                         # não simplificado
    print('Classificação: INFANTIL')
elif i <= 19:                         # simplificado
    print('Classificação: JUNIOR')
elif i <= 25:                         # simplificado
    print('Classificação: SENIOR')
else:                                 # acima de 25
    print('Classificação: MASTER')
