"""Exercício Python 083:

Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
e fechados na ordem correta."""

'''RESOLUÇÃO GUANABARA (achei bem confuso mas entendi no final)'''

# toda expressão é uma str
expressao = str(input('Digite a expressão: '))
lista = []

# varre a expressão em busca de parenteses
for simbolo in expressao:

    # se achar um parentese abrindo
    if simbolo == '(':

        # adiciona a lista (lista = ['('])
        lista.append('(')

    # se achar um parentese fechando
    elif simbolo == ')':

        # se o tamanho da lista for maior que 0
        if len(lista) > 0:

            # ele deleta o último valor (o último valor ser um '(')
            # seria como se o '(' neutralizasse um ')'
            # então eles vão se neutralizando até não restar nenhum ()
            lista.pop()

        # se o tamanho da lista for igual a 0
        elif len(lista) == 0:

            # ele adiciona um parentese fechando
            lista.append(')')

            # e logo após da o break
            break

if len(lista) == 0:
    print('Expressão correta')
    # porque todos parenteses estaram neutralizados

elif len(lista) > 0:
    print('Expressão incorreta')
    # ainda haverá parenteses em aberto
