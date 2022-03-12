from datetime import date

a = int(input('Informe o ano para ser analisado, digite 0 para analisar o ano atual: '))

if a == 0:                      # para analisar o ano atual
    a = date.today().year

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:     # expressão para saber se o ano é bissexto
    print('O ano \033[31m{}\033[m é um ano bissexto!'.format(a))
else:
    print('O ano \033[31m{}\033[m não é um ano bissexto!'.format(a))
