"""Exercício Python 62:

Melhore o DESAFIO 61;
pergunte para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos."""

# dados do usuário
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

# variáveis
termo = primeiro
contador = 1
total = 0
mais = 10

# estruturas aninhadas - while dentro de while
while mais != 0:
    total += mais
    while contador <= total:
        print('{} ➞ '.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer a mais: '))
print('Progressão finalizada com {} termos exibidos.'.format(contador - 1))    # Guanabara: total
