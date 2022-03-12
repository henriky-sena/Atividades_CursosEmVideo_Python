"""Exercício Python 090:

Faça um programa que leia nome e média de um aluno, guardando também a situação num dicionário.
No final, mostre o conteúdo da estrutura na tela."""

dados = dict()
dados['nome'] = str(input('Nome do aluno: '))
dados['média'] = float(input(f'Média de {dados["nome"]}: '))

print()

if dados['média'] >= 7:
    dados['situação'] = 'APROVADO(A)'

elif 5 <= dados['média']:
    dados['situação'] = 'RECUPERAÇÃO'

else:
    dados['situação'] = 'REPROVADO(A)'

# nesse caso, prefiro imprimir dessa forma
print(f'{dados["nome"]} teve média {dados["média"]}')
print(f'{dados["situação"]}')

# GUANABARA
'''
for k, v in dados.items():
    print(f'{k} é igual a {v}')
'''