from random import randint
total = []
jogador1 = {'Jogador': 1, 'tirou': randint(0, 6)}
jogador2 = {'Jogador': 2, 'tirou': randint(0, 6)}
jogador3 = {'Jogador': 3, 'tirou': randint(0, 6)}
jogador4 = {'Jogador': 4, 'tirou': randint(0, 6)}
jogador5 = {'Jogador': 5, 'tirou': randint(0, 6)}
jogador6 = {'Jogador': 6, 'tirou': randint(0, 6)}
total.append(jogador1)
total.append(jogador2)
total.append(jogador3)
total.append(jogador4)
total.append(jogador5)
total.append(jogador6)
for p in total:
    for k, v in p.items():
        print(f'{k} {v}', end=' ')
    print()
print('Ranking dos jogadores: ')
