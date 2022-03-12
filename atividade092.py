"""Exercício Python 092:

Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-o (com idade) em um dicionário.

Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""

from datetime import date
ano = date.today().year


dados = dict()

dados['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
dados['carteira'] = int(input('Carteira de Trabalho (digite 0 caso não tenha): '))


idade = ano - ano_nascimento
aposentadoria = idade + 35


if dados['carteira'] != 0:
    dados['contratação'] = int(input('Ano de contração: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = idade + 35

    print()
    print(f'{dados["nome"]} tem {idade} anos;')
    print(f'Com 35 anos de contribuição, {dados["nome"]} se aposenta-rá com {aposentadoria} anos.')

else:
    print()
    print(f'{dados["nome"]} tem {idade} anos;')
    print('Ainda não possui anos de contribuição para aposentadoria.')
