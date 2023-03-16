soma = 0
for c in range(0, 500):
    if c % 2 == 1 and c % 3 == 0:
        soma = soma + c

print('A soma de todos os números impares multiplos de 3 de 0 a 500 é : {}'.format(soma))
