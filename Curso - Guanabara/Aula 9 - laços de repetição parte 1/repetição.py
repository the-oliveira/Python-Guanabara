from random import randint
soma = 0

for c in range(0, 10):
    n = randint(0, 100)
    print('Valor randomizado de 1 a 100: {}'.format(n))
    soma += n
print('Soma dos números: {}'.format(soma))