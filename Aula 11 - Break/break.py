n = s = 0
while True:
    n = int(input('Digite um número (999 para finalizar): '))
    if n == 999:
        break
    s += n
print(f'A soma dos números digitados é igual a {s}')