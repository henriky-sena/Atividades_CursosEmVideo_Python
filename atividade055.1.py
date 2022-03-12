""" Parabéns você entendeu o conceito :) """
menor = 0
maior = 0
for pessoa in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}Kg.'.format(maior))
print('O menor peso lido foi {}Kg.'.format(menor))
