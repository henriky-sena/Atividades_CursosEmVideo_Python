"""Entendi o conceito hehehe"""

print('=='*20)
print('{:^40}'.format('BANCO AURORA'))
print('=='*20)

valor = int(input('Quanto deseja sacar? R$ '))
print('')

total = valor
nota = 50
contador_notas = 0

while True:
    if total >= nota:
        total -= nota
        contador_notas += 1
    else:
        if contador_notas > 0:
            print(f'Total de {contador_notas} notas de R$ {nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        contador_notas = 0
        if total == 0:
            break
print('')
print('Tenha um bom dia!')
