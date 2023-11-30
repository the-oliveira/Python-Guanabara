lista = []
for valor in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(lista)
if lista.count(max(lista)) >= 2:
    print(f'O maior valor digitado foi {max(lista)} nas posições: ', end='')
    for p, v in enumerate(lista):
        if v == max(lista):
            print(f'{p}..', end='')
else:
    print(f'O maior valor digitado foi {max(lista)} na posição {lista.index(max(lista))}')
print()
if lista.count(min(lista)) >= 2:
    print(f'O menor valor digitado foi {min(lista)} nas posições: ', end='')
    for p, v in enumerate(lista):
        if v == min(lista):
            print(f'{p}..', end='')
else:
    print(f'O menor valor digitado foi {min(lista)} na posição {lista.index(min(lista))}')
