import math

c1 = float(input('Insira o valor do cateto oposto: '))
c2 = float(input('Insira o valor do cateto adjacente: '))
hip = math.hypot(c1, c2)
print('A hipotenusa desse triângulo retângulo é de: {:.2f}'.format(hip))
