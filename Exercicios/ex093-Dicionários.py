dados = []
jogador = {}
jogador['Nome'] = str(input('Qual o nome do jogador? '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} disputou? '))
jogador['Partidas'] = partidas
for p in range(0, partidas):
    dados.append(int(input(f'Quantos gols na partida {p+1}? ')))
jogador['Gols'] = dados[:]
jogador['Total'] = sum(dados)
print('=' * 50)
print(jogador)
print('=' * 50)
print(f'O jogador {jogador["Nome"]} disputou {jogador["Partidas"]} partidas, marcando: ')
for g in range(0, partidas):
    print(f'   - Na partida {g+1} marcou {jogador["Gols"][g]} gols')
print(f'Ao todo foram {jogador["Total"]} gols até o momento!')
print('=' * 50)
for k, v in jogador.items():
    print(f' - {k}: {v}')
print('=' * 50)