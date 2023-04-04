from math import factorial
n = int(input('Digite um número: '))
contador = n
mult = 1
print(f'Vamos calcular o fatorial de {n}! ')
'''while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    mult *= contador
    contador -= 1
print(mult)'''
#Utilizando o for para realizar o mesmo programa

for c in range(n,0,-1):
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else' = ', end='')
    contador -= 1
print(factorial(n))