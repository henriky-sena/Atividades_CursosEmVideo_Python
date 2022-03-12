m = float(input('Digite um valor em metros: '))

# 1 m = 100 cm
# 1 m = 1000 mm

print('-='*16)              # mera formatação

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mmm = m * 1000

print('{} m equivale a {:.3f} km'.format(m, km))
print('{} m equivale a {:.2f} hm'.format(m, hm))
print('{} m equivale a {:.2f} dam'.format(m, dam))
print('{} m equivale a {:.2f} dm'.format(m, dm))
print('{} m equivale a {:.2f} cm'.format(m, cm))
print('{} m equivale a {:.2f} mm'.format(m, mmm))

print('-='*16)              # mera formatação
