"""Exercício Python 65:

Crie um programa que leia vários números inteiros pelo teclado.

No final da execução:

- Mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
- O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

# tentativa
'''
op = 'SN'
soma = 0
quantidade = 0

maior = 0
menor = 0
media = 0


while op != 'N':
    if 'S' in op:
        valor = int(input('Digite um valor: '))
        op = str(input('Deseja continuar? [S/N]: ')).strip().upper()

        # quantos números
        quantidade = quantidade + 1

        # soma dos valores
        soma = soma + valor

        # média dos valores
        media = soma / quantidade

        # maior e menor
        if quantidade == 1:
            maior = valor
            menor = valor
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    else:
        print('Opção inválida')

print('')
print('Foram digitados {} valores;
A soma de todos os valores é igual a {};
A média dos valores é de {};'.format(quantidade, soma, media))
'''


op = 'S'
soma = quant = media = maior = menor = 0    # não gosto de deixar assim não :[

while op in 'S':
    n = int(input('Digite um número: '))

    # soma
    soma += n

    # quantidade
    quant += 1

    # maior / menor
    if quant == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    op = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

media = soma / quant

print('')

print('Você digitou {} números;'. format(quant))
print('A média dos números foi de {:.2f};'.format(media))
print('E por fim, o maior número foi {} e o menor {}.'.format(maior, menor))
