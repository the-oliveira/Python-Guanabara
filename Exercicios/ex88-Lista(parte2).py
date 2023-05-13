from random import randint
from time import sleep
lista = []
print('='*40)
print('     VAMOS TESTAR A SUA SORTE!     ')
print('='*40)
jogos = int(input('Deseja gerar quantos jogos? '))
for x in range(0, jogos):
    while len(lista) != 6:
        numero = randint(1, 60)
        if numero in lista:
            sleep(0)
        else:
            lista.append(numero)
        lista.sort()
    print(f'Jogo número {x+1}: {lista}')
    sleep(1)
    lista.clear()
print('='*40)
print('               BOA SORTE!               ')
print('='*40)