print('\033[36m△▽\033[m'*20)

print('        \033[36mANALISADOR DE TRIÂNGULOS   \033[m ')

# dados:
a = float(input('\033[36m▹\033[m Primeira reta: '))
b = float(input('\033[36m▹\033[m Segunda reta: '))
c = float(input('\033[36m▹\033[m Terceira reta: '))
# formula para ter um triângulo:  a < b + c

# bloco:
if a < b + c and b < a + c and c < b + a:
    print('As retas \033[36mPODEM\033[m formar um triângulo!')
    if a == b and b == c:
        print('EQUILÁTEO: todos os lados são iguais')
    elif a != b == c or b != a == c or c != a == b:
        print('ISÓSCELES: dois lados são diferentes')
    elif a != b and b != c:
        print('ESCALENO: todos os lados são diferentes')
else:
    print('As retas \033[36mNÃO PODEM\033[m formar um triângulo!')

print('\033[36m△▽\033[m'*20)
