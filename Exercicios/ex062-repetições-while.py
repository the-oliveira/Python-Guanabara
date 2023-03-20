ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termos = 0

while termos < 10:
    print(f'{ptermo + termos * razao }', end=' - ')
    termos += 1
    if termos == 10:
        ltermo = ptermo
        continuar = str(input('Deseja ver mais termos? [S/N]: ')).lower().strip()
        if continuar == 's':
            ntermos = int(input('Quantos termos deseja ver a mais? '))
        else:
            print('Fim do programa!')
            exit()

print('Final!')