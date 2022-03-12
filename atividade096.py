"""Exercício Python 096:

Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento)
e mostre a área do terreno.
"""

# area = largura * altura

print('--'*17)
print('   == CONTROLE DE TERRENOS ==  ')

print('--'*17)
def area(largura, comprimento):     # na linha 'def' se declara apenas os parametros que serão utilizados
    a = largura * comprimento       # depois o que será feito com esse def
    print(f'> A área de {l} x {c} é {a:.1f}m²')       # e então o que sairá dele


# PROGRAMA PRINCIPAL
l = float(input('> Largura em metros: '))       # depois pega duas variáveis quaisquer
c = float(input('> Comprimento em metros: '))   # elas serão igualadas aos parâmetros ja estabelecidos
print()

area(largura=l, comprimento=c,)                 # dessa forma.
print('--'*17)
