print('- '*27)
si = float(input('Digite o sálario atual do funcionário: R$'))
ap = int(input('Digite o aumento em porcentagem (apenas números): '))
print('')

vap = si * (ap/100)             # valor aumento porcentagem
vf = si + vap                   # valor final

# print('O valor do sálario R${:.2f}, teve um aumento de {}%'.format(si, ap))
print('O salário atual é de R${:.2f}'.format(vf))
print('- '*27)
