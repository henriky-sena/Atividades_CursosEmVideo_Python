print('Olá, Seja bem vindo ao Programa de Financiamento de Imóveis!')
print('')

valor = float(input('Qual o valor total do imóvel? '))
salario = float(input('Qual o valor do seu salário? '))
ano = int(input('Em quantos anos você pretende pagar o imóvel? '))
print('')

parcela = valor / (ano * 12)
totalsal = salario * (30/100)

print('O valor das parcelas serão de R${:.2f}'.format(parcela))

if parcela <= totalsal:
    print('Você poderá financiar este imóvel!')
else:
    print('Infelizmente você não poderá financiar este imóvel!')
