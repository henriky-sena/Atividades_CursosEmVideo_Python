"""Entendi o conceito do exercício 056 :)

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas:
No final do programa, mostre:
> a média de idade do grupo; ✓
> qual é o nome do homem mais velho; ✓
> quantas mulheres têm menos de 20 anos. ✓
"""

# variáveis:
media = 0
homemvelho = ''
maioridade = 0
mulheresmenos20 = 0

# dados
for pessoas in range(1, 5):
    print('---- {}ª PESSOA ----'.format(pessoas))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    # média do grupo ✓
    media += idade
    mediat = media / pessoas

    # nome do homem mais velho ✓
    if sexo == 'M' and pessoas == 1:
        homemvelho = nome
        maioridade = idade
    if sexo == 'M' and idade > maioridade:
        maioridade = idade
        homemvelho = nome

    # mulheres com menos de 20 anos ✓
    if sexo == 'F' and idade < 20:
        mulheresmenos20 += 1

print('')

# saídas
print('A média da idade do grupo é de {} anos;'.format(mediat))
print('O homem mais velho se chama {} e tem {} anos;'.format(homemvelho, maioridade))
print('E total de mulheres com menos de vinte anos é de {}.'.format(mulheresmenos20))
