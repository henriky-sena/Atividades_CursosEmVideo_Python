
# da primeira forma que eu tinha feito tava certo além de ser mais eficiente
for c in range(2, 51, 2):
    print(c, end=' ')
print('Acabou!')

# mesmo resultado só que a primeira gasta menos 'eneriga'
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
print('Acabou!')
