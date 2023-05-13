lista = [[], [], []]
par = terceira = maior = 0
for l in range(0,3):
    for c in range(0,3):
        lista[l].append(int(input(f'Digite o valor para a posição {l}.{c} ')))
for l in range(0,3):
    for c in range(0,3):
        print(f'[ {lista[l][c]} ]', end=' ')
        if lista[l][c] % 2 == 0:
            par += lista[l][c]
        if maior == 0:
            maior += lista[l][c]
        elif lista[l][c] > maior:
            maior += lista[l][c]
    print()
print(f'A soma dos números pares foi: {par}')
