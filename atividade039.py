from datetime import date   # importando o ano atual do computador
atual = date.today().year

print('\033[32m\\\033[m'*37)    # formatação

nasc = int(input('Informe o ano de seu nascimento: '))
s = int(input('''
Informe seu gênero:
[ 1 ] Masculino
[ 2 ] Feminino
Digite a opção: '''))

# calculos:
idade = atual - nasc
falta = 18 - idade
passou = idade - 18

print('')   # formatação

# blocos:
if s == 1:
    if idade < 18:
        print('Você ainda irá se alistar!')
        print('Faltam {} ano(s) para você se alistar.'.format(falta))
        ano = atual + falta
        print('Seu alistamento será em {}'.format(ano))
    elif idade == 18:
        print('Está na hora de se alistar!')
    elif idade > 18:
        print('Já passou da hora de se alistar!')
        print('Passaram-se {} ano(s) do seu alistamento.'.format(passou))
        ano = atual - passou
        print('Seu alistamento foi em {}'.format(ano))
elif s == 2:
    print('Você não precisa se alistar!')
else:
    print('Digite uma opção válida.')

# print('Seu alistamento foi em {}'.format())
print('\033[32m\\\033[m'*37)    # formatação
