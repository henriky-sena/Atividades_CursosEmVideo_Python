c = float(input('Escreva a temperatura em ºC: '))

# formula ºC para ºF -  (1 °C × 9/5) + 32 = 33,8 °F

f = c * 1.8 + 32

print('A temperatura de {} ºC, corresponde a {:.1f} ºF!'.format(c, f))
