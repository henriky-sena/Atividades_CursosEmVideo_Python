d = float(input('Qual a distância da viagem em Km? '))

# p = d * 0.5 if d <= 200 else d * 0.45     -     o comando if else simplificado

if d <= 200:
    print('Você pagará \033[34mR${:.2f}\033[m!'.format(d * 0.5))
else:
    print('Você pagará \033[34mR${:.2f}\033[m!'.format(d * 0.45))
