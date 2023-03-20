n = int(input('Digite um número: '))
contador = n
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    contador -= 1


