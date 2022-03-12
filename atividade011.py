print('//'*20)
print('')

l = float(input('Digite a largura da parede em metros: '))
a = float(input('Agora a altura da parede em metros: '))

print('')

# calculos em m²
a2 = l * a
L = 2
apl = a2/L                  # area por litro
lt = apl/L                  # lata de tinta

# cada litro de tinta pinta uma área de 2m²

print('A área total da parede é de: {:.2f} m²'.format(a2))
print('Você precisará de {:.1f} L de tinta para pintar essa parede, ou seja, {:.1f} latas de tinta de 2 L!'.format(apl, lt))

print('')
print('//'*20)
