def maior(*num):
    print('Vamos analisar os números informados!')
    for n in num:
        print(f'{n} ', end=' ')
    print()
    if len(num) == 0:
        print('Foram informado 0 números, portanto não possuí maior valor.')
    else:
        print(f'O maior número da lista é {max(num)} e foram digitados {len(num)} numeros.')
    print()


maior(2, 3, 32, 2, 1, 1, 2, 3, 4, 4, 4, 1, 1, 2, 2)
maior(3, 4, 5, 6, 1, 2, 0, 39, 1)
maior()
