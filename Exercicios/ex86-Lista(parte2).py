lista = [[], [], []]
for l in range(0,3):
    for c in range(0,3):
        lista[l].append(int(input(f'Digite o valor para a posição {l}.{c} ')))
print(lista[0])
print(lista[1])
print(lista[2])
