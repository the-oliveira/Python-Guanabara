lista = [[], [], []]
for l in range(0,3):
    for c in range(0,3):
        lista[l].append(int(input(f'Digite o valor para a posição {l}.{c} ')))
for l in range(0,3):
    for c in range(0,3):
        print(f'{lista[l][c]}', end=' ')
    print()

