lista = []
for valor in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
if lista.count(max(lista)) >= 2:
    print(f'O maior valor digitado foi {max(lista)} nas posições {lista.index(max(lista))+1} e {lista.index(max(lista))+1}')
else:
    print(f'O maior valor digitado foi {max(lista)} na posição {lista.index(max(lista)) + 1}')
if lista.count(min(lista)) >= 2:
    print(f'O menor valor digitado foi {min(lista)} nas posições {lista.index(min(lista))+1} e {lista.index(min(lista))+1}')
else:
    print(f'O menor valor digitado foi {min(lista)} na posição {lista.index(min(lista)) + 1}')
