v = float(input('Digite a velocidade do veículo em Km/h: '))
m = (v - 80) * 7.00

if v > 80:
    print('\033[31mMULTADO!\033[m você excedeu o limite de velocidade de 80Km/h!')
    print('O valor da multa será \033[31mR${:.2f}\033[m'.format(m))
print('')
print('Dirija com segurança! Tenha um bom dia!')
