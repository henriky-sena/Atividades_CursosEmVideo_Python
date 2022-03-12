"""Exercício Python 083:

Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
e fechados na ordem correta."""

# esse jeito além de ser muito mais fácil de entender é mais facil de fazer
expressao = str(input('Digite a expressão: '))

parentese_inicial = expressao.count('(')
parentese_final = expressao.count(')')

if expressao.index('(') < expressao.index(')'):
    if parentese_inicial == parentese_final:
        print('Expressão válida')

    elif parentese_inicial != parentese_final:
        print('Expressão inválida')
else:
    print('Expressão inválida')
