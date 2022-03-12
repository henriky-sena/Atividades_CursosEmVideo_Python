"""Exercício Python 56:

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas:
No final do programa, mostre:
> a média de idade do grupo; ✓
> qual é o nome do homem mais velho;
> quantas mulheres têm menos de 20 anos.
"""

# fiz sozinho = ✓

# variáveis:
soma = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

# bloco:
for pessoa in range(1, 5):
    print('---- {}ª PESSOA ----'.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    # média das idades: ✓
    soma += idade
    media = soma / pessoa

    # nome do homem mais velho:
    if pessoa == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    # mulheres com menos 20 anos:
    if sexo == 'F' and idade < 20:
        totmulher20 += 1

print('')

# saídas:
print('A média de idade do grupo é de {} anos;'.format(media))
print('O homem mais velho tem {} anos e se chama {};'.format(maioridadehomem, nomevelho))
print('E ao todo, são {} mulheres com menos de 20 anos.'.format(totmulher20))
