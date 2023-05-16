dados = []
totalgols = 0
jogador = {'nome':'', 'partidas':''}
jogador['nome'] = str(input('Qual o nome do jogador? '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} disputou? '))
jogador['partidas'] = partidas
for p in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {p+1}? '))
    dados.append(gols)
    totalgols += gols
jogador['gols'] = dados
jogador['total'] = totalgols
print(jogador)
print(f'O jogador {jogador["nome"]} disputo {jogador["partidas"]}, marcando: ')
for g in range(0, partidas):
    print(f'No jogo {g+1} marcou {jogador["gols"][g]}')
