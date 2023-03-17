n = int(input('Digite um número: '))
div = 0
for c in range(1, n + 1):
    if n % c == 0:
        print(f'\033[1:31m{c} \033[m', end='')
        div = div + 1
    else:
        print(f'\033[1:32m{c} \033[m', end='')

print(f'\nO número {n} foi divisível {div} vezes, portanto:')

if div == 2:
    print('Ele \033[1:32mÉ PRIMO\033[m')
else:
    print('Ele \033[1:31mNÃO É PRIMO\033[m')
    