ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termos = 0
while termos < 10:
    print(f'{ptermo + termos * razao }', end=' - ')
    termos += 1
print('Final!')
