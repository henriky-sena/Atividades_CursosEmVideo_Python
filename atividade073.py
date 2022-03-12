"""Exercício Python 073:

Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense."""

time = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
        'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos',
        'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará',
        'Vasco', 'Sport', 'América-MG', 'Vitória', 'Paraná')

# lista dos times
print('-='*60)
print(f'''\033[32m - Lista de times do Brasileirão 2022:\033[m {time}''')
print('-='*60)

# os cinco primeiros
print(f'''\033[32m - Os 5 primeiros times:\033[m {time[:5]}''')
print('-='*60)

# os 4 últimos
print(f'''\033[32m - Os 4 últimos times:\033[m {time[-4:]}''')
print('-='*60)

# ordem alfabética
print(f'''\033[32m - Os times em ordem alfabética:\033[m {sorted(time)}''')
print('-='*60)

# posição Chapecoense
print(f'\033[32m - O Chapecoense está na\033[m {time.index("Chapecoense")+1}ª\033[32m posição.\033[m')
print('-='*60)
