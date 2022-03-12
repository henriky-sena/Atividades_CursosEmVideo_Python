"""Exercício Python 095:

Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador."""

time = []

jogador = {}
gols = []

while True:

    jogador['nome'] = str(input('NOME: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for p in range(0, partidas):
        gols.append(int(input(f'Quantos gols {jogador["nome"]} fez na {p+1}ª partida ? ')))


    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    gols.clear()

    op = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while 'S' != op != 'N':
        print('RESPOSTA INVÁLIDA')
        op = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    if op == 'N':
        break

print(time)

# tabela
print('=='*20)
print(f'{"cod":<5}{"nome":<8}{"gols":<15}{"total":>8}')
print('=='*20)
for i, v in enumerate(time):
    print(f'{i:^3}{v["nome"]:<10}{str(v["gols"]):<15}{v["total"]:>8}')
print('=='*20)

while True:
    busca = int(input('Buscar dados de qual jogador? [999 para encerrar]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print('CÓDIGO INVÁLIDO!')
    else:
        print(f' -- JOGADOR {time[busca]["nome"]} --')

        for i, g in enumerate(time[busca]["gols"]):
            print(f' > Na {i+1}ª partida fez {g} gols;')

    print('=='*20)
print('<< PROGRAMA ENCERRADO >>')

# :)
