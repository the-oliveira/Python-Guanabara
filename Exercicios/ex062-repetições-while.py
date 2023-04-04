ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termos = 0
continuar = 10
total = 0
contador = 0
while continuar != 0:
    total += continuar
    while termos < total:
        print(f'{ptermo + termos * razao }', end=' - ')
        termos += 1
    print('Parando...')
    continuar = int(input('Deseja ver mais quantos termos? '))
print(f'Fim do programa, você viu {total} termos desta PA.')
