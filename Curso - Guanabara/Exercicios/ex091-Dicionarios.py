from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Jogador 1': randint(1, 6),
             'Jogador 2': randint(1, 6),
             'Jogador 3': randint(1, 6),
             'Jogador 4': randint(1, 6)}
ranking = []
print('=' * 30)
print('VALORES SORTEADOS: ')
for k, v in jogadores.items():
    sleep(1)
    print(f'   - {k} tirou {v}')
print()
print('RANKING DOS JOGADORES: ')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for p, j in enumerate(ranking):
    sleep(0.5)
    print(f'{p+1}º - {j[0]} que tirou {j[1]}')
