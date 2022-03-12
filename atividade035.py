print('\033[33m△▽\033[m'*20)

print('   \033[36m▹   ANALISADOR DE TRIÂNGULOS   ◃\033[m ')

print('')

a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Agora o comprimento da segunda reta: '))
c = float(input('E por fim, o comprimento da terceira reta: '))
print('')

# blocos:
if a < b + c and b < a + c and c < a + b:
    print('As retas \033[32mPODEM\033[m formam um triângulo!')
else:
    print('As retas \033[31mNÃO PODEM\033[m formar um triângulo!')
print('\033[33m△▽\033[m'*20)
