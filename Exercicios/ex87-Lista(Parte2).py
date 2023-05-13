lista = [[], [], []]
par = somacoluna = maior = 0
for l in range(0,3):
    for c in range(0,3):
        lista[l].append(int(input(f'Digite o valor para a posição {l}.{c} ')))
for l in range(0,3):
    for c in range(0,3):
        print(f'[ {lista[l][c]} ]', end=' ')
        if lista[l][c] % 2 == 0:
            par += lista[l][c]
    print()
print(f'A soma dos números pares foi: {par}')
for c in range(0,3):
    if maior == 0:
        maior = lista[1][c]
    elif lista[1][c] > maior:
        maior = lista[1][c]
print(f'O maior número na segunda linha é {maior}')
for l in range(0,3):
    somacoluna += lista[l][2]
print(f'A soma da terceira coluna é igual a: {somacoluna}')
