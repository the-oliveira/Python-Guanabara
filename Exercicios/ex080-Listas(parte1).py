lista = []
for n in range(0, 5):
    num = int(input('Digite um valor: '))
    if n == 0:
        lista.append(num)
        print(f'Primeiro número adicionado! Vamos mante-lo na posição {lista.index(num)} por enquanto!')
    else:
        if num >= max(lista):
            lista.append(num)
            print(f'Número adicionado ao final da lista.. posição {lista.index(num)}')
        elif num <= min(lista):
            lista.insert(0, num)
            print(f'Número adicionado no inicio da lista.. posição {lista.index(num)}')
        else:
            lista.append(num)
            print(f'Número adicionado na posição: {lista.index(num)}')
print(sorted(lista))
