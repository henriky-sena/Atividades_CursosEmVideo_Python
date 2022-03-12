primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

'''precisamos calculuar o N-ésimo termo da PA
aqui no caso é o 10º termo, mas poderia ser o 20º, o 15º e assim por diante
é só mudar o 10 para o número desejado
aqui está 10 por causa do exercício'''

# cálculo do N-ésimo termo da PA
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print(c, end=' ➞ ')
print('Acabou!')
