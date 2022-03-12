print('\033[31m-=\033[m'*15)
print('            \033[1mI M C\033[m          ')
print('\033[31m-=\033[m'*15)

p = float(input('Digite seu peso em Kg: '))
a = float(input('Digite sua altura em metros: '))

imc = p / (a ** 2)

print('')
print('Seu IMC é de \033[31m{:.1f}\033[m - '.format(imc), end='')

if imc < 18.5:
    print('\033[31mABAIXO DO PESO\033[m')
elif 18.5 <= imc < 25:
    print('\033[31mPESO IDEAL\033[m')
elif 25 <= imc < 30:
    print('\033[31mSOBREPESO\033[m')
elif 30 <= imc <= 40:
    print('\033[31mOBESIDADE\033[m')
elif imc > 40:
    print('\033[31mOBESIDADE MÓRBIDA\033[m')
