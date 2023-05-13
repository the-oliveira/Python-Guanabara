from random import randint
from time import sleep
lista = []
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


