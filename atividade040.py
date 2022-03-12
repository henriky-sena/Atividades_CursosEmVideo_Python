n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print('')

# calculos:
m = (n1 + n2)/2

# blocos:
if m < 5.0:
    print('\033[31mREPROVADO\033[m')
elif 5.0 <= m <= 6.9:       # elif m >= 5.0 and m <= 6.9:   meu comando
    print('\033[31mRECUPERAÇÃO\033[m')    # não to entendendo pq ele simplificou
elif m >= 7.0:
    print('\033[32mAPROVADO\033[m')
print('Sua média foi de {:.1f}'.format(m))

