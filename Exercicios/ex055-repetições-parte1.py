lista = []
for p in range(0, 5):
    peso = float(input(f'Digite o peso da {p}ª pessoa: '))
    lista += [peso]

lista.sort()
print(f'O maior peso entre as cinco pessoas foi de {lista[4]}kg')
print(f'O menor peso entre as cinco pessoas foi de {lista[0]}kg')