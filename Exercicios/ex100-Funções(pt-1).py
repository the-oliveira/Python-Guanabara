from random import randint
from time import sleep
numeros = []
def sorteio(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)
    print(f'Os números sorteados foram: ')
    for n in numeros:
        sleep(0.5)
        print(f'{n}', end=' ')
    print()

def somapar():
    print('Vamos somar os números pares sorteados!')
    soma = 0
    print('São eles: ', end=' ')
    for n in numeros:
        if n % 2 == 0:
            sleep(0.5)
            print(f'{n} ', end=' ')
            soma += n
    print()
    print(f'A soma dos números pares foi igual a: {soma}')


sorteio(numeros)
print()
somapar()

