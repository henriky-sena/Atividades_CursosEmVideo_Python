"""Exercício Python 083:

Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
e fechados na ordem correta."""

'''RESOLUÇÃO GUANABARA (agora eu sei hehe)'''

expressao = str(input('Digite a expressão: '))
listinha = []

for simbolo in expressao:

    if simbolo == '(':
        listinha.append('(')

    elif simbolo == ')':
        if len(listinha) > 0:
            listinha.pop()
        elif len(listinha) == 0:
            listinha.append(')')

if len(listinha) == 0:
    print('Operação correta')
else:
    print('Operação incorreta')
