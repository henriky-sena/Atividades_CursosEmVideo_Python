"""Exercício Python 53:

Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

Exemplos de palíndromos:
- APOS A SOPA
- A SACADA DA CASA
- A TORRE DA DERROTA
- O LOBO AMA O BOLO
- ANOTARAM A DATA DA MARATONA."""

frase = str(input('Insira uma frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)  # tbm poderia ser feito assim: junto = frase.replace(' ','')
inverso = ''

# explicando o conceito:
'''
len() : para informar para o (for) o tamanho da string
(1º) - 1: onde ele vai começar, pegando todas as letras
(2º) -1: onde ele vai terminar, pegando todas as letras
(3º) -1: mandando ele contar de trás para frente (voltando - um passo negativo)
 ↑
 ↑   
  ↖  ⇽   ⇽   ⇽   ⇽   ⇽   ⇽   1º  2º  3º '''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))

if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('A frase digitada não é um Palíndromo.')

# macete do fatiamento do Python:
'''
inverso = junto[::-1]

print('O inverso de {} é {}.'.format(junto, inverso))

if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('A frase digitada não é um Palíndromo.')
'''
