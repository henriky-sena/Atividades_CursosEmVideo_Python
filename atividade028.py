from random import randint
from time import sleep      # faz o computador "dormir"
computador = randint(0, 5)       # faz o computador "pensar"

print('\033[31m-=-\033[m'*20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('\033[31m-=-\033[m'*20)
jogador = int(input('Em que número pensei? '))        # jogador responde
print('\033[31mPROCESSANDO...\033[m')
sleep(2)

if jogador == computador:
    print('Parabéns! Você \033[31mACERTOU\033[m.')
else:
    print('Você \033[31mERROU\033[m, eu pensei no número \033[31m{}\033[m!'.format(computador))
print('Até a proxima!')
