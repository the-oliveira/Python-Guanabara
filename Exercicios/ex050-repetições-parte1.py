soma = 0
for c in range (0, 6):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
print('A soma dos valores pares é de : {}'.format(soma))
