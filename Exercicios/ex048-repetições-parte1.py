soma = 0
for c in range(0,500):
    n = c
    if n % 3 == 0:
        soma = soma + n

print('A soma de todos os números impares multiplos de 3 de 0 a 500 é : {}'.format(soma))
