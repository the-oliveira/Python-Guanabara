dados = []
jogador = {}
lista = []
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Qual o nome do jogador? '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} disputou? '))
    jogador['Partidas'] = partidas
    for p in range(0, partidas):
        dados.append(int(input(f'Quantos gols na partida {p+1}? ')))
    jogador['Gols'] = dados[:]
    jogador['Total'] = sum(dados)
    lista.append(jogador.copy())
    dados.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Comando inválido. Deseja continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break
print('Cod ', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()
for k, v in enumerate(lista):
    print(f'{k:>4} ', end=' ')
    for d in v.values():
        print(f'{str(d):<13} ', end=' ')
    print()
while True:
    info = int(input('Digite um jogador que queira ver os dados: (999 para encerrar): '))
    if info == 999:
        break
    if info >= len(lista):
        print(f'Jogador não encontrado, tente novamente!')
        info = int(input('Digite um jogador que queira ver os dados: (999 para encerrar): '))
    else:
        print(f'Informações do jogador {lista[info]["Nome"]}')
        for i, g in enumerate(lista[info]["Gols"]):
            print(f'  - No jogo {i+1} fez {g}')
print('Fim do programa')


