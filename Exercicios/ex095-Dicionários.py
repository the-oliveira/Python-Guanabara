dados = []
lista = []
totalgols = 0
jogador = {'nome':'', 'partidas':''}
while True:
    jogador['nome'] = str(input('Qual o nome do jogador? '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} disputou? '))
    jogador['partidas'] = partidas
    for p in range(0, partidas):
        gols = int(input(f'Quantos gols na partida {p+1}? '))
        totalgols += gols
        jogador['total'] = totalgols
    lista.append(jogador.copy())
    dados.clear()
    continuar = str(input('Quer Continuar? [S/N] ')).upper().split()[0]
    while continuar not in "SN":
        continuar = str(input('Quer Continuar? [S/N] ')).upper().split()[0]
    if continuar == 'N':
        break
print(lista)
for p, g in lista:


