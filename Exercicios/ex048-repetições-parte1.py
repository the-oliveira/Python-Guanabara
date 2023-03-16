soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 2 == 1 and c % 3 == 0:
        soma = soma + c
        cont = cont + 1

print('A soma dos {} números impares multiplos de 3 de 1 a 500 é : {}'.format(cont, soma))
