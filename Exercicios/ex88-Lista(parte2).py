from random import randint
from time import sleep
lista = []
dados = []
jogos = int(input('Deseja gerar quantos jogos? '))
for x in range(0, jogos):
    for n in range(0, 6):
        numero = randint(1, 60)
        if numero in lista:
            sleep(0)
        else:
            dados.append(numero)
            lista.append(dados[:])
        dados.clear()
        lista.sort()
    print(f'Jogo número {x+1}: {lista}')
    sleep(1)
    lista.clear()
