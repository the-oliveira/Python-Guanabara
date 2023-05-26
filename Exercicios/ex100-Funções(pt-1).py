from random import randint
sort = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), ]
numeros = [sort[:]]
soma = 0

def sorteio():
    print(f' Os números sorteados foram: ', end=' ')
    for n in numeros:
        print(f'{n}', end=' ')

def somapares():



sorteio()
somapares()