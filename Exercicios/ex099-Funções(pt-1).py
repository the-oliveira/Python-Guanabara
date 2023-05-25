def maior():
    numeros = [10, 30, 20, 11, 0, 2, 1, 2, 200, 10, 10]
    numeros.sort()
    print('=' * 60)
    print(f'O maior número da lista é {numeros[-1]} e foram digitados {len(numeros)} numeros.')
    print('=' * 60)


maior()