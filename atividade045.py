from random import randint
from time import sleep
c = randint(1, 3)

print('\033[35m=-\033[m'*14)
print('          JOKENPÔ')
print('')

print('\033[35m[ 1 ]\033[m PEDRA')
print('\033[35m[ 2 ]\033[m PAPEL')
print('\033[35m[ 3 ]\033[m TESOURA')
j = int(input('Escolha sua jogada: '))
print('')

print(end='\033[35mJO')
sleep(0.5)
print(end=' KEN ')
sleep(0.5)
print('PÔ\033[m')
sleep(1)

print('')

if j == 1 and c == 3:
    print('VOCÊ GANHOU !!!')
elif j == 3 and c == 1:
    print('O COMPUTADOR VENCEU!')
elif j == 3 and c == 2:
    print('VOCÊ GANHOU !!!')
elif j == 2 and c == 3:
    print('O COMPUTADOR VENCEU!')
elif j == 2 and c == 1:
    print('VOCÊ GANHOU !!!')
elif j == 1 and c == 2:
    print('O COMPUTADOR VENCEU!')
elif j == c:
    print('EMPATE!!')
else:
    print('Por favor, reinicie o programa e insira um número válido.')
print('\033[35m=-\033[m'*14)
