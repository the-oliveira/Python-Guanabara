dados = []
jogador = {}
lista = []
while True:
    jogador['Nome'] = str(input('Qual o nome do jogador? '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} disputou? '))
    jogador['Partidas'] = partidas
    for p in range(0, partidas):
        dados.append(int(input(f'Quantos gols na partida {p+1}? ')))
    jogador['Gols'] = dados[:]
    jogador['Total'] = sum(dados)
    lista.append(jogador.copy())
    jogador.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Comando inválido. Deseja continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break
for n, p in enumerate(lista):
    for k, v in p.items():
        print(f'{k} ', end=' ')
    print()
    for k, v in p.items():
        print(f'{v} ', end=' ')
    print()
while True:
    info = int(input('Digite um jogador que queira ver os dados: (999 para encerrar): '))
    if info == 999:
        break
    else:
        print(f'Informações do jogador {lista[info]["Nome"]}')
        for j, p in enumerate(lista):
            print(f'  - No jogo {j+1} fez {lista[info]["Gols"][j]}')
print('Fim do programa')


