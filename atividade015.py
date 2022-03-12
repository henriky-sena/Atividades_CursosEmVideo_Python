print('-='*20)
print('Bem vindo a central de aluguel de carros!')
print('')

d = int(input('Informe a quantidade de dias alugados: '))
km = float(input('Agora a quantidade de Km percorridos: '))
print('')

# dia: R$60             # prestar mais atenção nos dados
# km: R$0.15

v = (d * 60) + (km * 0.15)
print('Você pagará R${:.2f}!'.format(v))

print('-='*20)
